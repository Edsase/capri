from PIL import Image
import re
import sys
import numpy as np

from resizeimage import resizeimage
# images = [sys.argv[1]]

images = ["C:/Users/SesayE01/Desktop/Websites/capri/sds_site/static/boston/img/surveys.jpg",
"C:/Users/SesayE01/Desktop/Websites/capri/sds_site/static/boston/img/gap.jpg",
"C:/Users/SesayE01/Desktop/Websites/capri/sds_site/static/boston/img/scoping.jpg",
"C:/Users/SesayE01/Desktop/Websites/capri/sds_site/static/boston/img/interns.jpg",
"C:/Users/SesayE01/Desktop/Websites/capri/sds_site/static/boston/img/kb.png",
"C:/Users/SesayE01/Desktop/Websites/capri/sds_site/static/boston/img/knowledge.jpg",
"C:/Users/SesayE01/Desktop/Websites/capri/sds_site/static/boston/img/stakeholder.jpg",
"C:/Users/SesayE01/Desktop/Websites/capri/sds_site/static/boston/img/training.png"]

for image_to_resize in images:
# image_to_resize = sys.argv[1]
    image_name, = re.findall("[a-zA-Z_1-9-]*\.+[a-zA-Z_-]{3}$", image_to_resize)
    print(image_name)

    save_name = image_name[:-4] + "_resized"+ image_name[-4:] 


    with Image.open(image_to_resize) as im:
        width = 270
        height = 240
        im = im.resize((width, height), Image.ANTIALIAS)
        im.save(save_name)
	