import qcode
import clip
from PIL import Image

data = clip.get_clip()
img = qcode.adv_qrImg(data)
#img = Image.open(img)

img.show(title=data)
