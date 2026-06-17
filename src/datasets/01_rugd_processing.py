from pathlib import Path
import pandas as pd
import json

def data_processing():
    '''
    - Conducting data preprocessing
    - Saving processed data split into .txt files
    '''
    # Retrieving data
    images_root = Path("../../data/RUGD/images")
    annotations_root = Path("../../data/processed/annotations_with_id")

    data = []
    for scene_dir in images_root.iterdir():
        if not scene_dir.is_dir():
            continue

        scene_name = scene_dir.name
        annotation_scene_dir = annotations_root / scene_name

        for image_path in scene_dir.glob("*.png"):
            annotation_path = annotation_scene_dir / image_path.name
            data.append({
                "image_path": str(image_path),
                "annotation_path": str(annotation_path),
                "scene": scene_name
            })

    df = pd.DataFrame(data)
    
    # Calculation training/testing/validation sets using original RUGD paper distribution
    train_scenes = ["park-2", "trail", "trail-3", "trail-4", "trail-6", "trail-9", "trail-10", "trail-11", "trail-12", "trail-14", "trail-15", "village"]
    test_scenes = ["creek", "park-1", "trail-7", "trail-13"]
    val_scenes = ["park-8", "trail-5"]

    training = []
    testing = []
    validation = []

    for scene in train_scenes:
        scene_data = df[df["scene"] == scene]
        training.extend(scene_data.to_dict("records"))

    for scene in test_scenes:
        scene_data = df[df["scene"] == scene]
        testing.extend(scene_data.to_dict("records"))

    for scene in val_scenes:
        scene_data = df[df["scene"] == scene]
        validation.extend(scene_data.to_dict("records"))

    print(f"Number of elements in df: {len(df)}")
    print(f"Training: {len(training)} - Does it match original distribution: {len(training) == 4779}")
    print(f"Testing: {len(testing)} - Does it match original distribution: {len(testing) == 1924}")
    print(f"Validation: {len(validation)} - Does it match original distribution: {len(validation) == 733}")

    # Defining writing function
    def writing_files(split_path, split): 
        '''
        - Writing images/annotations to defined files
        - Writes paths of the images/annotations into the files
        '''
        try:
            with open(f"../../data/processed/rugd/{split_path}.txt", "w") as file:
                for d in split:
                    img = f"{d['scene']}/{Path(d['image_path']).stem}"
                    file.write(img + "\n")  
                      
        except Exception as e: print(e)

    # Writing data split in files, with appropriate paths
    writing_files("train", training)
    writing_files("test", testing)
    writing_files("val", validation)

data_processing()