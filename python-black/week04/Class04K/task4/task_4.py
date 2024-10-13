from PIL import Image

def encode_in_bit_plane(image, binary_data, bit_plane):
    """
    Encode the binary data into the specified bit plane of the image.
    :param image: Image to encode the data into
    :param binary_data: Binary data to encode
    :param bit_plane: Bit plane to encode the data into (0-7)
    :return: Encoded image
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
            # Modify the specified bit plane of the red channel
            r = (r & ~(1 << bit_plane)) | (int(binary_data[data_index]) << bit_plane)
            data_index += 1
            img.putpixel((x, y), (r, g, b))
        if data_index >= data_len:
            break

    return img

if __name__ == "__main__":
    image = Image.open('mario.png')
    binary_data = '0101010101010101'  # Example binary data
    bit_plane = 2  # Example bit plane

    encoded_image = encode_in_bit_plane(image, binary_data, bit_plane)
    encoded_image.save('encoded_image_bit_plane.png')
    print("Data successfully encoded in the specified bit plane and saved as 'encoded_image_bit_plane.png'")
