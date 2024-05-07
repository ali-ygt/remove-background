import cv2
from copy import deepcopy


class Image:
    """
    Class representing an image with methods for reading, displaying, and manipulating the image.
    """

    def __init__(self):
        """
        Initialize the Image class with default values for the image, original image, height, width, and channels.
        """
        self.__image = None
        self.__original_image = None
        self.__height = None
        self.__width = None
        self.__channels = None

    def read(self, path: str):
        """
        Read an image from the specified path and store a copy of the original image.
        :param path: str, path to the image file
        """
        self.__image = cv2.imread(path)
        if self.__image is not None:
            self.__original_image = deepcopy(self.__image)
            if self.__image.ndim == 2:
                self.__height, self.__width = self.__image.shape
            else:
                self.__height, self.__width, self.__channels = self.__image.shape

    def get(self):
        """
        Return the current image.
        :return: numpy.ndarray, the current image
        """
        return self.__image

    def get_original(self):
        """
        Return the original image.
        :return: numpy.ndarray, the original image
        """
        return self.__original_image

    def set(self, image: cv2.Mat):
        """
        Set the current image to the specified image.
        :param image: cv2.Mat, the new image
        :return: Image, the current Image object
        """
        self.__image = image
        return self

    def show(self, window_name: str = 'Frame'):
        """
        Display the current image in a window with the specified name.
        :param window_name: str, the name of the window
        :return: Image, the current Image object
        """
        cv2.imshow(window_name, self.__image)
        return self

    def wait_key(self, delay: int = 0, shutdown_key: str = 'q'):
        """
        Wait for a key press and close the window if the specified key is pressed.
        :param delay: int, delay in milliseconds before waiting for a key press
        :param shutdown_key: str, the key to close the window
        :return: None
        """
        if cv2.waitKey(delay) & 0xFF == ord(shutdown_key):
            cv2.destroyAllWindows()


if __name__ == '__main__':
    image = Image()
    image.read('/path/to/your/image')
    image.show(window_name='Frame').wait_key(delay=0, shutdown_key='q')
