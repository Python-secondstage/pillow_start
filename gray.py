import numpy as np
from PIL import Image

# 横方向のデータ生成(グラデーションの色)
row_data = np.arange(256)  # 0~255のnumpy配列を生成
# array([0, 1, 2, ..., 253, 254, 255])

# 縦方向のデータ生成
im_data = np.tile(row_data, (256, 1))  # row_dataを2次元配列にする(繰り返しは1回)
# array([[0, 1, 2, ..., 253, 254, 255],
#        [0, 1, 2, ..., 253, 254, 255],
#        ...,
#        [0, 1, 2, ..., 253, 254, 255],
#        [0, 1, 2, ..., 253, 254, 255])
# print(im_data)
print(row_data)

# 2次元配列のデータを画像に変換
im = Image.fromarray(np.uint8(im_data), "L")  # im_dataから画像を生成(データ型をint64からuint8に変換)

# 生成した画像を保存
# im.save("out_gray.png")
im.show()
