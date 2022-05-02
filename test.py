from Image import Image
from ImageList import ImageList


image_list = ImageList()

image1 = Image('2123', 'red_circle')

image1.add_classification('blue_square')

image1.add_classification('red_circle')

image_list.add_image(image1)

image2 = Image('2123', 'red_circle')

image2.add_classification('blue_square')

image_list.add_image(image2)

print(image_list.evaluate_classification_accuracy('red_circle'))