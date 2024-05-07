from lib.objects.image.image import Image
import cv2


class Thresh:
    """
    Class representing thresholding methods for an image.
    """

    def __init__(self, image: Image):
        """
        Initialize the Thresh class with the specified image.
        :param image: Image, the image to manipulate
        """
        self.__image = image

    def binary(self, thresh: int = 127, max_value: int = 255):
        """
        Apply a binary threshold to the current image.
        :param thresh: int, the threshold value
        :param max_value: int, the maximum value for pixel intensities
        :return: Thresh, the current Thresh object
        """
        self.__image.set(
            cv2.threshold(
                self.__image.get(),
                thresh,
                max_value,
                cv2.THRESH_BINARY
            )[1]
        )

    def binary_inv(self, thresh: int = 127, max_value: int = 255):
        """
        Apply a binary inverse threshold to the current image.
        :param thresh: int, the threshold value
        :param max_value: int, the maximum value for pixel intensities
        :return: Thresh, the current Thresh object
        """
        self.__image.set(
            cv2.threshold(
                self.__image.get(),
                thresh,
                max_value,
                cv2.THRESH_BINARY_INV
            )[1]
        )


if __name__ == '__main__':
    from lib.objects.color.color import Color
    image = Image()
    color = Color(image)
    thresh = Thresh(image)
    image.read('/path/to/your/image')
    color.to_gray()
    thresh.binary_inv()
    image.show(window_name='Frame').wait_key(delay=0, shutdown_key='q')
