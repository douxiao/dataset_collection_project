from PIL import Image

image_size = [640480]


def create_icon():
    for size in image_size:
        '''''pri_image = Image.open("icon.png") 
        pri_image.thumbnail((size,size)) 
        image_name = "icon_%d.png"%(size) 
        pri_image.save(image_name)'''
        pri_image = Image.open('image/'+ "test.jpg")
        pri_image.resize((640, 480), Image.ANTIALIAS).save('save_image/'+"test_resize %d.jpg" % (size))


if __name__ == "__main__":
    create_icon()