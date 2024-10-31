# 訓練紀錄與訓練指令
因為目前所知的diffusion的預訓練模型，都是以常見的RGB資料集為主，但在醫療領域經常使用的皆是灰階的資料集，例如：MRI、CT、超音波等等。
然而醫療影像其實非常需要生成式模型的支援，因為醫療影像取得有許多要過的門檻與程序，並且有醫療隱私問題，若能生成不具名且無個人特徵的醫療影像將會是一個非常大的幫助。
本次實驗使用數據集BUSI進行復現。
## Command：
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

## Parameters
```

def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=str, default=None, help="image source")
    parser.add_argument('--tags_source', type=str, default=None, help="tag files. will use --source if not specified.")
    parser.add_argument('--cond_images', type=str, default=None)
    parser.add_argument("--init_image", default=None,)
    parser.add_argument("--start_image", default=None,
                        help="starting image, for super resolution unets")
    parser.add_argument('--embeddings', type=str, default=None)
    parser.add_argument('--tags', type=str, default=None)
    parser.add_argument('--vocab', default=None)
    parser.add_argument('--size', default=256, type=int)
    parser.add_argument('--sample_steps', default=512, type=int)
    parser.add_argument('--num_unets', default=1, type=int, help="additional unet networks")
    parser.add_argument('--vocab_limit', default=None, type=int)
    parser.add_argument('--epochs', default=200, type=int)
    parser.add_argument('--imagen', default="imagen.pth")
    parser.add_argument('--output', type=str, default=None)
    parser.add_argument('--replace', action='store_true', help="replace the output file")
    parser.add_argument('--unet_dims', default=330, type=int)
    parser.add_argument('--unet2_dims', default=64, type=int)
    parser.add_argument('--dim_mults', default="(1,2,3,4)", type=tuple_type)
    parser.add_argument("--start_size", default=128, type=int)
    parser.add_argument("--sample_unet", default=None, type=int)
    parser.add_argument('--device', type=str, default="cuda")
    parser.add_argument('--text_encoder', type=str, default="t5-large")
    parser.add_argument("--cond_scale", default=1.0, type=float, help="sampling conditional scale 0-10.0")
    parser.add_argument('--no_elu', action='store_true', help="don't use elucidated imagen")
    parser.add_argument("--num_samples", default=1, type=int)
    parser.add_argument("--skip_steps", default=None, type=int)
    parser.add_argument("--sigma_max", default=80, type=float)
    parser.add_argument("--full_load", action="store_true",
                        help="don't use load_from_checkpoint.")
    parser.add_argument('--no_memory_efficient', action='store_true',
                        help="don't use memory_efficient unet1")
    parser.add_argument('--print_params', action='store_true',
                        help="print model params and exit")
    parser.add_argument("--unet_size_mult", default=4, type=int)
    parser.add_argument("--self_cond", action="store_true")

    # training
    parser.add_argument('--batch_size', default=8, type=int)
    parser.add_argument('--micro_batch_size', default=8, type=int)
    parser.add_argument('--samples_out', default="samples")
    parser.add_argument('--train', action='store_true')
    parser.add_argument('--train_encoder', action='store_true')
    parser.add_argument('--shuffle_tags', action='store_true')
    parser.add_argument('--train_unet', type=int, default=1)
    parser.add_argument('--random_drop_tags', type=float, default=0.5)
    parser.add_argument('--fp16', action='store_true')
    parser.add_argument('--bf16', action='store_true')
    parser.add_argument('--workers', type=int, default=8)
    parser.add_argument('--no_text_transform', action='store_true')
    parser.add_argument('--start_epoch', default=1, type=int)
    parser.add_argument('--no_patching', action='store_true')
    parser.add_argument('--create_embeddings', action='store_true')
    parser.add_argument('--verify_images', action='store_true')
    parser.add_argument('--pretrained', default="t5-small")
    parser.add_argument('--no_sample', action='store_true',
                        help="do not sample while training")
    parser.add_argument("--lr", default=2e-4, type=float)
    parser.add_argument('--loss', default="l2")
    parser.add_argument('--sample_rate', default=10000, type=int)
    parser.add_argument('--wandb', action='store_true',
                        help="use wandb logging")
    parser.add_argument('--is_t5', action='store_true',
                        help="t5-like encoder")
    parser.add_argument('--webdataset', action='store_true')
    parser.add_argument('--null_unet1', action='store_true',
                        help="use NullUnet() for unet1 (for superrez only model)")
    parser.add_argument('--save_frequency', default=100, type=int, help="每幾個 epoch 儲存一次模型")

    args = parser.parse_args()
```

## 引用：
* https://github.com/lucidrains/imagen-pytorch
* https://github.com/deepglugs/deep_imagen/tree/main
