"""
Lab 10.3 Grayscale image ADT
"""

from PIL import Image, ImageOps
from arrays import Array2D

class GrayscaleImageADT:
    """ class for Grayscale Image ADT
    to work with images and compress/decomprees them with lzw  """

    def __init__(self, nrows, ncols) -> None:
        """ Init values, initilize each element as 0 """
        self._image = Array2D(nrows, ncols)
        self.clear(0)
        self.compressed = []

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
        # get data from Image
        file_image = Image.open(path)
        image_grayscale = ImageOps.grayscale(file_image)
        # create Array 2D with image data
        ncols, nrows = image_grayscale.size
        self._image = Array2D(nrows, ncols)

        pixels = image_grayscale.load()
        for row in range(nrows):
            for col in range(ncols):
                self.setitem(row, col, pixels[col, row])


    def lzw_compression(self):
        """ Compress the image using lzw algorithm """
        # set initial compression values
        dict_size = 256
        dictionary = {chr(i):i for i in range(dict_size)}
        buffer = ''

        for i in range(self.height()):
            for j in range(self.width()):
                # look one symbol forward
                current_symbol = chr(self._image[i, j])
                bc = buffer + current_symbol
                # continue adding while buffer is in dict
                if bc in dictionary:
                    buffer = bc
                    continue
                # Add buffer to the result
                self.compressed.append(dictionary[buffer])
                buffer = current_symbol
                # add buffer+last to the dictionary
                dictionary[bc] = dict_size
                dict_size += 1
        # add last symbol
        if buffer: self.compressed.append(dictionary[buffer])
        return self.compressed


    def lzw_decompression(self):
        """ Decompress image from lzw compression """
        # set initial decompression values
        dict_size = 256
        decompress_dict = {i:chr(i) for i in range(dict_size)}
        buffer = chr(self.compressed.pop(0))
        result = [buffer]

        for num in self.compressed:
            if num in decompress_dict:
                entry = decompress_dict[num]
            elif num!= dict_size:
                raise KeyError('Bad compression')
            else:
                entry = buffer + buffer[0]
            result.append(entry)
            # change dicttionary
            decompress_dict[dict_size] = buffer + entry[0]
            dict_size += 1
            buffer = entry
        # create Array 2D from decompressed data
        result = ''.join(result)
        decompressed = Array2D(self.height(), self.width())
        index = 0
        for i in range(decompressed.num_rows()):
            for j in range(decompressed.num_cols()):
                decompressed[i,j] = ord(result[index])
                index += 1
        return decompressed
