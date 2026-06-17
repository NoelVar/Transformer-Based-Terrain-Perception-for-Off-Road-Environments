from collections import defaultdict
from tqdm import tqdm
from PIL import Image
from pathlib import Path
import numpy as np

def rgb2id(df, rgb_to_id):
    encoded_rgb2id = encode_rgb(rgb_to_id)
    output_root = Path("../../data/processed/rugd/annotations_with_id")

    for mask in tqdm(df["annotation_path"]):
        mask_img = Image.open(mask)
        mask_array = np.array(mask_img)[:, :, :3].astype(np.int32)

        encoded = (
            mask_array[:, :, 0]
            + mask_array[:, :, 1] * 256
            + mask_array[:, :, 2] * (256 ** 2)
        )

        id_mask = encoded_rgb2id[encoded]
        id_mask = id_mask.astype(np.uint8)
        
        output_path = output_root / Path(mask).parent.name / Path(mask).name
        output_path.parent.mkdir(parents=True, exist_ok=True)
        Image.fromarray(id_mask).save(output_path)

def encode_rgb(rgb_to_id):
    look_up_table = np.zeros(256 ** 3, dtype=np.int32)
    
    for (r, g, b), value in rgb_to_id.items():
        # https://www.ibm.com/docs/en/spss-statistics/32.0.0?topic=guide-setting-color-values-python
        encoded_key = r + (g * 256) + (b * (256 ** 2))
        look_up_table[encoded_key] = value
    
    return look_up_table