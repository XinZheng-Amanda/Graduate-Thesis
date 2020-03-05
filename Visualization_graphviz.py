import torch
from torchvision.models import AlexNet
from torchviz import make_dot
import os
os.environ["PATH"] += os.pathsep + 'D:/Anaconda/Programs/envs/py35/Library/bin/graphviz/'

x = torch.rand(8, 3, 256, 512)
model = AlexNet()
y = model(x)
g = make_dot(y)

g.view()
#g.render('alexnet_model', view=False)