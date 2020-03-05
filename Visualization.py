import torch
import torch.nn as nn
from torch.autograd import Variable
from torch.utils.data import DataLoader
from torchvision import datasets,transforms
import torchvision.models as models
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))
from tensorboardX import SummaryWriter
writer = SummaryWriter('log')
#alexnet = models.alexnet(pretrained=False)
#print(alexnet)
#x = torch.rand(8, 3, 256, 512)  # 假设输入20张1*28*28的图片
#with SummaryWriter(comment='AlexNet') as w:
#    w.add_graph(alexnet, x)

VGG= models.vgg11(pretrained=False)
print(VGG)
x = torch.rand(1, 3, 28, 28)  # 假设输入20张1*28*28的图片
with SummaryWriter(comment='VGG') as w:
    w.add_graph(VGG, x)

print('Done！')