from PIL import Image
from matplotlib import image
from matplotlib import pyplot
from numpy import asarray
import random
from operator import attrgetter
class Individual:
    def __init__(self,fitness,imageArray):
        self.fitness = fitness
        self.imageArray = imageArray
    def createInd(imageArray):
        for x in range(616*372):
          imageArray[x] = random.randint(0,255)
        return imageArray


def main():
    image = Image.open('test.jpg')
    data = asarray(image)
    print(data.shape)
    pix_val = list(image.getdata())
    newimg = Image.new('RGB',(616,372))
    newimg.putdata(pix_val)
    newimg.show()

    #  im = Image.open("test.jpg")
    #   im.show()

if __name__ == '__main__':
    main()