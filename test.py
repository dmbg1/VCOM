from ImageList import ImageList
from Image import Image
import os

image_list = ImageList() 
for root, _, files in os.walk('./dataset'):
    for file in files:
        split_file_path = os.path.join(root, file).split(os.sep)
        img_name = split_file_path[-1]
        _type = split_file_path[-2][:-1]
        # Prevent image duplicates
        idx = image_list.contains_img(img_name)
        if idx >= 0:
            image = image_list.get_image(idx)
            image.add_type(_type)
        else:
            image = Image(img_name, _type)
            image_list.add_image(image)

print(image_list.len())