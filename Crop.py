import torchvision
import torch
import PIL
#img = 'E:/Code/Graduate/dataset/000002.jpg'

from PIL import Image
import numpy as np

I = Image.open('E:/Code/Graduate/dataset/000002.jpg')
torchvision.transforms.functional.ten_crop(I, 10, vertical_flip=False)
