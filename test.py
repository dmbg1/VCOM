from Image import Image
from ImageList import ImageList


image_list = ImageList()
image =Image('132','23')
image_list.add_image(image)

img_list2 = image_list.copy()
print(image_list.get_image(0))
print(img_list2.get_image(0))
