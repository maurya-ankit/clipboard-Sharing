import qcode
import clip

from PIL import Image

data = clip.get_clip()
img = qcode.qr_img(data)
#img = Image.open(img)

img.show()
