from PIL import Image, ImageDraw
from SortFunctions import selectionSort


def comparePixels(pix1, pix2):
    return pix1[0][0] > pix2[0][0]
# end def comparePixels(pix1,pix2):


def main():
    IMG_NAME = 'rose'

    #open image
    #read each pixel into memory as the image object im
    with Image.open(IMG_NAME + '.jpeg') as im:
        width = int(im.size[0])
        height = int(im.size[1])

        #create draw object to draw to the image object
        #I will be drawingg back inot the original data in memory
        draw = ImageDraw.Draw(im)

        for i in range(width):
            for j in range(height):
                #get r and g and b values of pixel at position
                r,g,b = im.getpixel((i,j))
                draw.point((i,j), (255-r, 255-g, 255-b))    #make negative
            #end for j
        #end for i
    #end with Image.open(IMG_NAME + '.jpeg') as im:

    #save my image data from memory to a file with a different namd
    im.save('neg_' + IMG_NAME + '.jpeg', 'JPEG')

    #opens with your external preiview program, shows memory representaion
    im.show()
#end of def main():

if __name__ == "__main__":
    main()

