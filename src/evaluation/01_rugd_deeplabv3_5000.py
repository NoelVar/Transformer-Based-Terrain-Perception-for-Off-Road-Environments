# Ref: https://mmsegmentation.readthedocs.io/en/latest/user_guides/3_inference.html
from mmseg.apis import init_model, inference_model, MMSegInferencer

img_list = [
    "creek/creek_00181.png",
    "park-1/park-1_00761.png",
    "park-2/park-2_00136.png",
    "park-8/park-8_00111.png",
    "trail/trail_00221.png",
    "trail-7/trail-7_00001.png",
    "trail-11/trail-11_00011.png",
    "trail-11/trail-11_01856.png",
    "trail-14/trail-14_00291.png",
    "village/village_00578.png",
]

config = "../../results/rugd_test/deeplabv3plus_r50-d8_4xb2-40k_rugd.py"
checkpoint = "../../results/rugd_test/iter_5000.pth"

inferencer = MMSegInferencer(model=config, weights=checkpoint, device="cpu")
for data in img_list:
    inferencer(f"../../data/processed/rugd/images/{data}", out_dir="../../results/visualisations/")