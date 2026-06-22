from mmengine.config import Config
from mmengine.registry import init_default_scope
from mmseg.registry import DATASETS

cfg = Config.fromfile('mmsegmentation/configs/_base_/datasets/rugd_rellis_4_class.py')
init_default_scope('mmseg')

dataset = DATASETS.build(cfg.train_dataloader.dataset)

print(len(dataset))
sample = dataset[0]

print(sample["inputs"].shape)
print(len(dataset.METAINFO['classes']))
print(len(dataset.METAINFO['palette']))