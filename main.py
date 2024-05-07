from lib.objects.image.image import Image
from lib.objects.color.color import Color
from lib.objects.thresh.thresh import Thresh
from lib.objects.background.background import Background

image = Image()
color = Color(image)
thresh = Thresh(image)
background = Background(image)
image.read('path/to/your/image.jpg')
image.show(window_name='Original Image').wait_key(delay=0, shutdown_key='q')
color.to_gray()
thresh.binary_inv(thresh=127, max_value=255)
background.remove()
image.show('Background Removed').wait_key(delay=0, shutdown_key='q')