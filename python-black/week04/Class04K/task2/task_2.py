from PIL import Image

from mse import calculate_mse
from psnr import calculate_psnr


def encode_color(image, binary_data):
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
            r = (r & ~1) | int(binary_data[data_index])
            data_index += 1
            img.putpixel((x, y), (r, g, b))
        if data_index >= data_len:
            break

    return img


def encode_alpha(image, binary_data):
    if image.mode != 'RGBA':
        image = image.convert('RGBA')

    img = image.copy()
    width, height = img.size
    data_index = 0
    data_len = len(binary_data)

    for y in range(height):
        for x in range(width):
            if data_index >= data_len:
                break
            r, g, b, a = img.getpixel((x, y))  # Ensure we get RGBA values
            a = (a & ~1) | int(binary_data[data_index])
            data_index += 1
            img.putpixel((x, y), (r, g, b, a))
        if data_index >= data_len:
            break

    return img

if __name__ == "__main__":
    image = Image.open('mario.png')
    binary_data = '0101010101010101'  # Пример бинарных данных

    # Кодирование в цветовой канал
    encoded_image_color = encode_color(image, binary_data)
    encoded_image_color.save('encoded_image_color.png')
    mse_1 = calculate_mse('mario.png', 'encoded_image_color.png')
    pnsr_1 = calculate_psnr(mse_1)
    print('Color channel encoding:')
    print(f'MSE: {mse_1}')
    print(f'PSNR: {pnsr_1} dB')

    # Кодирование в альфа-канал
    encoded_image_alpha = encode_alpha(image, binary_data)
    encoded_image_alpha.save('encoded_image_alpha.png')
    mse_2 = calculate_mse('mario.png', 'encoded_image_alpha.png')
    pnsr_2 = calculate_psnr(mse_2)
    print('Alpha channel encoding:')
    print(f'MSE: {mse_2}')
    print(f'PSNR: {pnsr_2} dB')

    # Визуально ни то, ни другое изображения не изменились.
    # Сравним mse и psnr
    # MSE для кодирования альфа канала гораздо ниже и соотвествует нулю, так как данные добавленные в пиксели с максимальным альфо кналом не влияют на изображение. Поэтому значение PSNR стремиться к +бесконечности.
