import pickle
import os
from PIL import Image
from pathlib import Path
import numpy as np
from tqdm import tqdm
from collections import defaultdict

def analyse_predictions(choosen_prediction):
    txt_root = Path('data/processed/combined/test.txt')
    cm = np.zeros((4, 4), dtype=np.int64)

    with open(txt_root, "r") as file:
        for line in tqdm(file):
            _, partial_gt_path = line.strip().split()
            image_name = f"{Path(partial_gt_path).stem}{Path(partial_gt_path).suffix}"

            gt_path = "data/processed/combined/" + partial_gt_path
            pred_path = choosen_prediction + image_name
            gt = np.array(Image.open(gt_path))
            pred = np.array(Image.open(pred_path))

            gt = gt.flatten()
            pred = pred.flatten()

            hist = np.bincount(
                4 * gt + pred,
                minlength=4 ** 2
            ).reshape(4, 4)

            cm += hist
    
    return cm

# For Baseline
# path = "results/confusion_matrix/predictions.pkl/"

#  For Baseline (Weighted):
# path = "results/confusion_matrix/weighted_predictions/"

# For SwinUpernet:
# path = "results/confusion_matrix/swin-uper-predictions/"

# For SwinUpernet (Weighted):
path = "results/confusion_matrix/swin-uper-weighted-predictions/"

cm = analyse_predictions(path)
# GET TP VALUES ACCROSS DIAGONAL -------------------
tp = np.diag(cm)

# GET FP AND FN VALUES -------------------
fp = cm.sum(axis=0) - tp
fn = cm.sum(axis=1) - tp

# CALCULATE IoU FOR EACH CLASS -------------------
iou = tp / (tp + fp + fn)

# CALCULATE RECALL AND PRECISION -------------------
precision = tp / cm.sum(axis=0)
recall = tp / cm.sum(axis=1)

# CALCULATE F1-SCORE -------------------
f1 = 2 * precision * recall / (precision + recall)

# CALCULATE OVERALL ACCURACY -------------------
accuracy = tp.sum() / cm.sum()

# Classes for visualization
classes = ['sky', 'traversable', 'non-traversable', 'obstacle']

# VISUALIZATION -------------------
print("----------------------------------------------")
for i in range(len(tp)):
    print(f"Recall |{classes[i]}|: {recall[i]:.2%}")
    print(f"Precision |{classes[i]}|: {precision[i]:.2%}")
    print(f"F1-Score |{classes[i]}|: {f1[i]:.2%}")
    print(f"IoU |{classes[i]}|: {iou[i]:.2%}")
    print("\n")

print(f"Accuracy: {accuracy:.2%}")
print("----------------------------------------------")

# NORMALISE CONFUSION MATRIX -------------------
np.set_printoptions(
    precision=3,
    suppress=True
)
cm_normalized = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

print(cm_normalized)