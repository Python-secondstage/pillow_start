import numpy as np
from PIL import Image

# HSVの場合
row_data = np.arange(256)

hue_data = np.tile(row_data, (256, 1))  # 255x255の2次元配列を生成 [0,1..,254,255],[0,1..,254,255]
sat_data = np.transpose(hue_data)  # hueの配列の行と列を入れ替え [0 0],[1,1],[254,254],[255,255]
val_data = np.full_like(hue_data, 255)  # hueと同じ構造とデータ型を生成 [255,255],[255,255]..,[255,255],[255,255]

mat_data = np.stack([hue_data, sat_data, val_data], 2)  # 3つの2次元配列を結合して3次元配列にする axisで結合の階層を指定
im = Image.fromarray(np.uint8(mat_data), "HSV")

im_rgb = im.convert("RGB")  # HSVからRGBに変換
# im_rgb.save("out_color.png")
im_rgb.show()
