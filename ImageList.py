from Image import Image
import logging


class ImageList():
    def __init__(self) -> None:
        self.images = []

    def add_image(self, image: Image) -> None:
        self.images.append(image)
    
    # Returns index that contains image with same filename or -1 if there is none
    def contains_img(self, filename: str) -> int:
        i = 0
        for image in self.images:
            i += 1
            if image.filename == filename:
                return i
        return -1 

    def evaluate_classification_accuracy(self, type_) -> float:
        if type_ != 'red_circle' and type_ != 'blue_square' and type_ != 'stop_sign':
            print ('That type doesn\'t exist so an accuracy can\'t be measured')
            return 0.0
        
        cnt_img_with_type = 0
        cnt_correctly_classified = 0
        for image in self.images:
            if type_ in image.types:
                cnt_img_with_type += 1
                if type_ in image.classifications:
                    cnt_correctly_classified += 1
        
        if cnt_img_with_type == cnt_correctly_classified and cnt_img_with_type == 0: 
            return 100.0
        return cnt_correctly_classified * 100 / cnt_img_with_type

    def get_image(self, idx: int) -> Image:
        return self.images[idx] 
    
    def len(self) -> int:
        return len(self.images)
