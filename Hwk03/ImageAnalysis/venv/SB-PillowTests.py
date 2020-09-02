from PIL import Image, ImageDraw
from SortFunctions import selectionSort
from SearchFunctions import binarySearchSub


def comparePixels(pix1, pix2):
    return pix1[0][0] > pix2[0][0]


# end def comparePixels(pix1,pix2):


def storePixels(im):
    width = int(im.size[0])
    height = int(im.size[1])

    # store ppixels inout double tuple format.
    pixel_array = []

    for i in range(width):  # for loop for x position
        for j in range(height):  # for loop for y position
            # get r and g and b values of pixel at position
            r, g, b = im.getpixel((i, j))
            pixel_array.append([(r, g, b), (i, j)])
        # end for j
    # end for i
    return pixel_array
# end def storePixels(im):

def pixelsToImage(im, pixels):
    outimg = Image.new("RGB", im.size)
    outimg.putdata([p[0] for p in pixels])
    outimg.show()
    return outimg
# end def pixelsToImage(im, pixels):

def pixelsToPoints(size, pixels):
    #defualt bakground color is black
    outimg = Image.new("RGB",  size)
    for p in pixels:
        outimg .putpixel(p[1], p[0])
    outimg.show()
    return outimg
# enddef pixelsToPoints(im, pixels):

def grayScale(im, pixels):
    draw = ImageDraw.Draw(im)
    for px in pixels:
        gray_av = int((px[0][0] + px[0][1] + px[0][2])/3)
        draw.point(px[1], (gray_av, gray_av, gray_av))
#end of def pixelsToPoints(im, pixels):

def main():
    IMG_NAME = 'tinyrose'

    # open image
    # read each pixel into memory as the image object im
    with Image.open(IMG_NAME + '.jpg') as im:

        pixels = storePixels(im)
        print("stored")

        pixelsToImage(im, pixels)

    # TODO
        # sort copy of pixles
        sorted_pixels = pixels.copy()
        selectionSort(sorted_pixels, comparePixels)
        print("sorted")
        #sorted_im = pixelsToImage(im, sorted_pixels)
        #sorted_im.save('sorted_'+ IMG_NAME + '.jpg', 'JPEG')

        #search copy for r
        # use a comprehension to find the sorted r values
        # sorted_r_values = [r[0][0] for r in sorted_pixels}
        threshold = 200
        subi = binarySearchSub([r[0][0] for r in sorted_pixels],
                               0, len(sorted_pixels)-1, threshold)
        print("Sublist of resds starts at: ", subi)

        #uses list slice notation to remove any item before subi
        pixelsToPoints(im.size, sorted_pixels[subi:])

        # grayscale pixels
        grayScale(im, pixels)
        # restore found r

    # end with Image.open(IMG_NAME + '.jpg') as im:

    # save my image data from memory to a file with a different name
    im.save('gray_' + IMG_NAME + '.jpg', 'JPEG')

    # opens with your external preiview program, shows memory representaion
    #im.show()


# end of def main():

if __name__ == "__main__":
    main()
