## 指令：
### Train:
```
nohup python3 first-imagen.py --train --source /mnt/c/python_code/deep_imagen-main/mix_tarin/busi/img --tags_source /mnt/c/python_code/deep_imagen-main/mix_tarin/busi/txt --start_size=64 --epochs=4000 --start_epoch=1 --imagen 4090_BUSI_64size_16batch.pt --train_unet=1 --random_drop_tags=0.3 --cond_scale=1.0 --lr 1e-4 --batch_size=16 --micro_batch_size=8  &
```
### Sample:
```
python3 first-imagen.py --imagen imagen_Unet_1size.pt --tags "meningioma" --output meningioma.png --num_samples=10 --sample_unet=1
```

## Setup:
```
python3 -m pip install imagen-pytorch
```

## Running Inference:
```
python3 imagen.py --imagen yourmodel.pth --tags "1girl, red_hair" --output red_hair.png
```

## Training:
Currently, this is set up to use danbooru-style tags such as:
```
1girl, blue_dress, super_artist
```
The dataloader expects a directory with images and tags laid out like this:
```
dataset/
   tags/img1.txt
   tags/img2.txt
   ...
   imgs/img1.png
   imgs/img2.png
```
The subdirectories doesn't really matter, only the filenames matter.

### To train:
```
python3 imagen.py --train --source /path/to/dataset --imagen yourmodel.pth
```
## gel_fetch.py

Included is a tool to fetch data from *booru-style websites and creates tag files in the expected format.


### Setup:
You will need GelbooruViewer and pybooru to run.

First clone GelbooruViewer into the deep-imagen repo:
```
cd path/to/deep-imagen/
git clone https://github.com/ArchieMeng/GelbooruViewer
```
```
python3 -m pip install git+https://github.com/LuqueDaniel/pybooru
```
## Usage
```
python3 gel_fetch.py --tags "holo" --txt holo/tags --img holo/imgs --danbooru
```
