"""
Lab 10 task 3
"""
from more_itertools import peekable
import numpy as np

from PIL import Image, ImageOps

from arrays import Array2D

class GrayscaleImageADT:
    """ class for Grayscale Image ADT
    to work with images and compress/decomprees them with lzw  """

    def __init__(self, nrows, ncols) -> None:
        """ init values, initilize each element as 0"""
        self._image = Array2D(nrows, ncols)
        self.clear(0)


    def height(self):
        """ return image height """
        return self._image.num_rows()

    def width(self):
        """ return image width """
        return self._image.num_cols()

    def clear(self, value):
        """ clear array, set each pixel with value x"""
        assert -1 < value < 256, 'Invalid value'

        for i in range(self.height()):
            for j in range(self.width()):
                self._image.__setitem__((i,j), value)

    def getitem(self, row, col):
        """ return value on stated coords row, col"""
        assert -1<col<self.width() and-1 < row < self.height(), "Array subscript out of range"
        return self._image[row, col]

    def setitem(self, row, col, value):
        """ set given value on stated position (row, col) """
        assert -1<col<self.width() and-1 < row < self.height(), "Array subscript out of range"
        assert -1 < value < 256, 'Invalid value'
        self._image[row, col] = value

    def from_file(self, path):
        """ get information about image on stated path """

        file_image = Image.open(path)
        image_grayscale = ImageOps.grayscale(file_image)

        ncols, nrows = image_grayscale.size
        self._image = Array2D(nrows, ncols)


        pixels = image_grayscale.load()
        for row in range(nrows):
            for col in range(ncols):
                self.setitem(row, col, pixels[col, row])
