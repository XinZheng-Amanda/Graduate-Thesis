import Augmentor
p = Augmentor.Pipeline('E:/Code/Graduate/dataset','E:/Code/Graduate/output/')
#p.flip_left_right(probability=1)
#p.flip_top_bottom(probability=1)
#p.flip_random(probability=1)
#p.rotate90(probability=1)
#p.crop_centre(probability=1,percentage_area=0.7)

#p.skew_tilt(probability=1,magnitude=1)

#.random_distortion(probability=1,grid_height=5,grid_width=16,magnitude=8)

#p.shear(probability=1,max_shear_left=20,max_shear_right=20)

#p.random_erasing(probability=1,rectangle_area=0.5)
p.random_erasing(probability=1,rectangle_area=0.8)
p.sample(1)
#p.rotate(probability=1, max_left_rotation=10, max_right_rotation=10)
#功能是生成随机擦除的图像哈！