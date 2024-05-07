from lib.objects.image.image import Image
import cv2


class Color:
    """
    Class representing color manipulation methods for an image.
    """

    def __init__(self, image: Image):
        """
        Initialize the Color class with the specified image.
        :param image: Image, the image to manipulate
        """
        self.__image = image

    def to_gray(self):
        """
        Convert the current image to grayscale.
        :return: Color, the current Color object
        """
        self.__image.set(
            cv2.cvtColor(self.__image.get(), cv2.COLOR_BGR2GRAY)
        )
        return self


if __name__ == "__main__":
    image = Image()
    color = Color(image)
    image.read('/path/to/your/image')
    color.to_gray()
    image.show().wait_key()

