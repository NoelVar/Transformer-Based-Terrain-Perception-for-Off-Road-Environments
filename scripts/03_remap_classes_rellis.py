from collections import defaultdict
from tqdm import tqdm
from PIL import Image
from pathlib import Path
import numpy as np
import pandas as pd

mapping_to_4class = {
    7: 0,
    3: 1,
    1: 1,
    10: 1,
    23: 1,
    31: 1,
    33: 1,
    11: 1,
    2: 1,
    13: 1,
    22: 1,
    14: 1,
    19: 2,
    0: 2,
    6: 2,
    8: 3,
    27: 3,
    15: 3,
    5: 3,
    9: 3,
    12: 3,
    17: 3,
    18: 3,
    4: 3,
    34: 3,
    16: 3,
    20: 3,
    21: 3,
    24: 3 
}

input_root = Path("../data/RELLIS-3D/annotations")
output_root = Path("../data/processed/combined/rellis/annotations")

def read_from_file():
    data = []
    for scene_dir in input_root.iterdir():
        if not scene_dir.is_dir():
            continue

        scene_name = scene_dir.name
        complete_path = scene_dir / Path("pylon_camera_node_label_id")

        for image_path in complete_path.glob("*.png"):
            data.append({
                "path": image_path,
                "scene": scene_name    
            })

    df = pd.DataFrame(data)
    return df

def load_and_convert(df):
    look_up_table = np.zeros(256, dtype=np.uint8)

    for old_id, new_id in mapping_to_4class.items():
        look_up_table[old_id] = new_id

    for i, mask in tqdm(enumerate(df["path"])):
        mask_img = Image.open(mask)
        mask_array = np.array(mask_img)
        
        new_mask = look_up_table[mask_array]
        scene = df['scene'].iloc[i]

        write_2_file(mask, scene, new_mask)

def write_2_file(old_path, scene, new_mask):
    file_path = Path(scene) / Path("pylon_camera_node_label_id") / Path(old_path.name)
    output_path = output_root / file_path
    # print(output_path)
    # print(new_mask)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    Image.fromarray(new_mask).save(output_path)


df = read_from_file()
# print(df.head())
load_and_convert(df)