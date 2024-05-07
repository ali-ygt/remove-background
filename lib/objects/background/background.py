from lib.objects.image.image import Image
import numpy as np


class Background:
    """
    Class representing background manipulation methods for an image.
    """

    def __init__(self, image: Image):
        """
        Initialize the Background class with the specified image.
        :param image: Image, the image to manipulate
        """
        self.__image = image
        self.__white_dots = None
        self.__black_dots = None
        self.__coordinates_black = None
        self.__coordinates_white = None

    def count_white_dots(self):
        """
        Count the number of white dots in the current image.
        :return: int, the number of white dots
        """
        self.__white_dots = np.count_nonzero(self.__image.get() == 255)
        return self.__white_dots

    def count_black_dots(self):
        """
        Count the number of black dots in the current image.
        :return: int, the number of black dots
        """
        self.__black_dots = np.count_nonzero(self.__image.get() == 0)
        return self.__black_dots

    def coordinates_white(self):
        """
        Find the coordinates of all white dots in the current image.
        :return: ndarray, the coordinates of white dots
        """
        self.__coordinates_white = np.argwhere(self.__image.get() == 255)
        return self.__coordinates_white

    def coordinates_black(self):
        """
        Find the coordinates of all black dots in the current image.
        :return: ndarray, the coordinates of black dots
        """
        self.__coordinates_black = np.argwhere(self.__image.get() == 0)
        return self.__coordinates_black

    def remove(self):
        """
        Remove the background by comparing white and black dots.
        :return: Background, the current Background object
        """
        if self.count_black_dots() > self.count_white_dots():
            coordinates = self.coordinates_black()
            image = self.__image.get_original()
            for coordinate in coordinates:
                image[coordinate[0], coordinate[1]] = 0
            self.__image.set(image)
            return self

        else:
            coordinates = self.coordinates_white()
            image = self.__image.get_original()
            for coordinate in coordinates:
                image[coordinate[0], coordinate[1]] = 0
            self.__image.set(image)
            return self


if __name__ == "__main__":
    from lib.objects.color.color import Color
    from lib.objects.thresh.thresh import Thresh
    image = Image()
    color = Color(image)
    thresh = Thresh(image)
    bg = Background(image)
    image.read('/home/ali-ygt/Desktop/test2/assets/images/4.jpg')
    image.show(window_name='Original Image').wait_key(delay=0, shutdown_key='q')
    color.to_gray()
    thresh.binary_inv(thresh=127, max_value=255)
    bg.remove()
    image.show(window_name='Background Removed Image').wait_key(delay=0, shutdown_key='q')
