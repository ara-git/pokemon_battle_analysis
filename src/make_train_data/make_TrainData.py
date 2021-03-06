from ast import Num
import os
from PIL.Image import Image
import numpy as np
import cv2
import function_make_TrainData as functions
from keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
from keras.preprocessing.image import (
    load_img,
    img_to_array,
    ImageDataGenerator,
    array_to_img,
    save_img,
)
from keras.utils import np_utils
import pandas as pd

# ディレクトリの変更
# os.chdir(r"C:\Users\ara-d\pokemon_analisis")

# 画像確認用：
"""
cv2.imshow("",SelectTime)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

####################################
# まず、画像データに関しての加工

# 保存していた名前データを解凍する。
Names = functions.call_name_file(path="./poke_names")
print("Names:", Names)

# ここから画像ファイル（学習用）
# trainデータ（jpgファイル）がある場所を指定する。
Image_data = functions.call_img_file(path="./poke_figs", use_jpg=True)

# データをカサ増する
datagen = ImageDataGenerator(
    width_shift_range=0.05, height_shift_range=0.05, brightness_range=[0.9, 1.0]
)

num_of_additional_images = 10

##関数を実行し、データをカサ増しする
functions.make_additional_images(
    Image_data, datagen, num_of_additional_images=num_of_additional_images, save=True
)

#########################################
# ここからラベルデータに関しての加工
# one-hotラベルを作成する
one_hot_original, one_hot_shifted = functions.make_one_hot_data(
    Names, num_of_additional_images
)

# 結合して、保存する
stacked_one_hot = np.vstack([one_hot_original, one_hot_shifted])
np.save("./poke_names/one_hot_label", stacked_one_hot)
