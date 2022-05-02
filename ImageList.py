from Image import Image


class ImageList():
    def __init__(self) -> None:
        self.images = []

    def add_image(self, image: Image) -> None:
        self.images.append(image)
    
    # Returns index that contains image with same filename or -1 if there is none
    def contains_img(self, image: str) -> int:
        i = 0
        for image in self.images:
            i += 1
            if image.filename == image:
                return i
        return -1 

    def evaluate_red_circles_accuracy(self) -> float:
        cnt_img_with_red_circle = 0
        cnt_correctly_classified = 0
        for image in self.images:
            if 'red_circle' in image.types:
                cnt_img_with_red_circle += 1
                if 'red_circle' in image.classifications:
                    cnt_correctly_classified += 1
        return cnt_correctly_classified * 100 / cnt_img_with_red_circle

    def evaluate_blue_squares_accuracy(self) -> float:
        cnt_img_with_blue_square = 0
        cnt_correctly_classified = 0
        for image in self.images:
            if 'blue_square' in image.types:
                cnt_img_with_blue_square += 1
                if 'blue_square' in image.classifications:
                    cnt_correctly_classified += 1
        return cnt_correctly_classified * 100 / cnt_img_with_blue_square

    def evaluate_stop_signs_accuracy(self) -> float:
        cnt_img_with_stop_sign = 0
        cnt_correctly_classified = 0
        for image in self.images:
            if 'stop_sign' in image.types:
                cnt_img_with_stop_sign += 1
                if 'stop_sign' in image.classifications:
                    cnt_correctly_classified += 1
        return cnt_correctly_classified * 100 / cnt_img_with_stop_sign

    def get_image(self, idx: int) -> Image:
        return self.images[idx] 
    
    def len(self) -> int:
        return len(self.images)
