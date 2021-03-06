import os

import nibabel as nib
import numpy as np
import torch
import torch.nn as nn
from tqdm import tqdm

from dataset.fracnet_dataset import FracNetInferenceDataset
from dataset import transforms as tsfm
from model.unet import UNet


def _predict_single_image(model, dataloader):
    pred = np.zeros(dataloader.dataset.image.shape)
    crop_size = dataloader.dataset.crop_size
    with torch.no_grad():
        for _, sample in enumerate(dataloader):
            images, centers = sample
            images = images.cuda()
            output = model(images).sigmoid().cpu().numpy().squeeze(axis=1)

            for i in range(len(centers)):
                center_z, center_y, center_x = centers[i]
                cur_pred_patch = pred[
                    center_z - crop_size // 2:center_z + crop_size // 2,
                    center_y - crop_size // 2:center_y + crop_size // 2,
                    center_x - crop_size // 2:center_x + crop_size // 2,
                ]
                pred[
                    center_z - crop_size // 2:center_z + crop_size // 2,
                    center_y - crop_size // 2:center_y + crop_size // 2,
                    center_x - crop_size // 2:center_x + crop_size // 2,
                ] = np.amax((output[i], cur_pred_patch), axis=0)

    return pred


def predict(args):
    batch_size = 16
    num_workers = 4

    model = UNet(1, 1, n=16)
    if args.model_path is not None:
        model_weights = torch.load(args.model_path)
        model.load_state_dict(model_weights)
    model.eval()
    model = nn.DataParallel(model).cuda()

    transforms = [
        tsfm.Window(-200, 1000),
        tsfm.MinMaxNorm(-200, 1000)
    ]

    image_id_list = [x.split("-")[0] for x in os.listdir(args.image_dir)
        if "nii" in x]
    image_path_list = [os.path.join(args.image_dir, file)
        for file in os.listdir(args.image_dir)]

    progress = tqdm(total=len(image_id_list))
    for image_id, image_path in zip(image_id_list, image_path_list):
        dataset = FracNetInferenceDataset(image_path, transforms=transforms)
        dataloader = FracNetInferenceDataset.get_dataloader(dataset,
            batch_size, num_workers)
        prediction = _predict_single_image(model, dataloader)
        pred_path = os.path.join(args.pred_dir, f"{image_id}_pred.nii.gz")
        pred_image = nib.Nifti1Image(prediction, None)
        nib.save(pred_image, pred_path)

        progress.update()


if __name__ == "__main__":
    import argparse


    parser = argparse.ArgumentParser()
    parser.add_argument("--image_dir", required=True,
        help="The image nii directory.")
    parser.add_argument("--pred_dir", required=True,
        help="The directory for saving predictions.")
    parser.add_argument("--model_path", default=None,
        help="The PyTorch model weight path.")
    args = parser.parse_args()
    predict(args)
