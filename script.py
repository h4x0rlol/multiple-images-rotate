from PIL import Image
import glob

print('Change rotation\nType:\n-90 to right\n90 to left\n180 to flip over')
rotation = int(input("Rotation: "))


def rotate_img(img, rotation):
    return img.rotate(rotation, expand=1)


image_list = []
for filename in glob.glob('*.jpg'):
    im = Image.open(filename)
    image_list.append(im)


def rotate(image_list):
    for i in range(0, len(image_list)):
        img = rotate_img(image_list[i], rotation)
        path = '{}.jpg'.format(i+1)
        img.save(path)


rotate(image_list)
