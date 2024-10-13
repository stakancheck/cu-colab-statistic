from PIL import Image

from mse import calculate_mse
from psnr import calculate_psnr


def encode_pixels(image: Image, binary_data: str, bits: int) -> Image:
    """
    Encode the binary data into the image using the least significant bits of the chosen color channel.
    :param image: Image to encode the data into
    :param binary_data: Binary data to encode
    :param bits: Number of bits to encode
    :return: encoded image
    """
    img = image.copy()
    width, height = img.size
    data_index = 0
    data_len = len(binary_data)

    for y in range(height):
        for x in range(width):
            if data_index >= data_len:
                break
            r, g, b = img.getpixel((x, y))[:3]  # Ensure we only get RGB values
            # Modify the least significant bit of the chosen color channel
            r = (r & ~bits) | int(binary_data[data_index: data_index + bits])
            data_index += bits
            img.putpixel((x, y), (r, g, b))
        if data_index >= data_len:
            break

    return img


def find_max_density(
        image: Image,
        binary_data: str,
        mse_threshold: int = 500,
        psnr_threshold: int = 30,
) -> int:
    """
    Find the maximum density of the binary data that can be encoded into the image.

    :param image: Image to encode the data into
    :param binary_data: Binary data to encode
    :param mse_threshold: Max value of mse
    :param psnr_threshold: Max value of psnr
    :return: max density of the binary data (int)
    """

    for dens in range(9, 1, -1):
        encoded_image = encode_pixels(image, binary_data, dens)
        encoded_image.save(f'encoded_image_{dens}.png')
        mse = calculate_mse('mario.png', f'encoded_image_{dens}.png')
        psnr = calculate_psnr(mse)
        # print(f'{dens=}, {mse=}, {psnr=}')
        if mse < mse_threshold and psnr > psnr_threshold:
            return dens


if __name__ == "__main__":
    image = Image.open('mario.png')
    binary_data = '0101010101010101'
    print(find_max_density(image, binary_data))


