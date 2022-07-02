"""
Lab 10.3 Test GrayScaleADT
"""

from grayscale_image_adt import GrayscaleImageADT

def test_adt():
    """
    Test creating grayscale and its compression
    """
    # upload photo
    test_photo = GrayscaleImageADT(1, 1)
    test_photo.from_file("test.jpg")
    # get array values
    num_rows = test_photo.height()
    num_cols = test_photo.width()
    test_array = test_photo._image
    # compress and decompress photo
    compressed_ph = test_photo.lzw_compression()
    decompressed_ph = test_photo.lzw_decompression()
    # compare initial photo with decompressed
    for i in range(num_rows):
        for j in range(num_cols):
            assert decompressed_ph[i,j] == test_array[i,j], f'Not the same numbers on {(i,j)}'
    print('Decompressed photo equels initial grayscale photo')
    # find comprassion ratio
    coeef = (len(bin(max(compressed_ph))) - 2) / 8
    ratio = round(len(compressed_ph) * coeef/ (num_cols*num_rows), 3)
    print(f"Compression ratio - {ratio}")

if __name__ == '__main__':
    test_adt()
