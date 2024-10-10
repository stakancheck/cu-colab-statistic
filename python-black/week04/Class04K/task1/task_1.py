from PIL import Image
from mse import calculate_mse
from psnr import calculate_psnr

def encode_in_channel(image, binary_data, channel):
    # Определяем индекс канала
    channel_index = {'r': 0, 'g': 1, 'b': 2}[channel]

    # Преобразуем изображение в массив пикселей
    pixels = list(image.getdata())

    # Преобразуем бинарные данные в список битов
    bits = [int(bit) for bit in binary_data]

    # Проверяем, что данных достаточно для кодирования
    if len(bits) > len(pixels) * 8:
        raise ValueError("Слишком много данных для кодирования в изображении")

    # Кодируем данные в выбранный канал
    bit_index = 0
    for i in range(len(pixels)):
        if bit_index < len(bits):
            pixel = list(pixels[i])
            pixel[channel_index] = (pixel[channel_index] & ~1) | bits[bit_index]
            pixels[i] = tuple(pixel)
            bit_index += 1

    # Создаем новое изображение с закодированными данными
    encoded_image = Image.new(image.mode, image.size)
    encoded_image.putdata(pixels)

    return encoded_image

def main():
    # Запрашиваем у пользователя путь к изображению и данные для кодирования
    data = input("Введите данные для кодирования: ")
    channel = input("Введите канал для кодирования (r, g, b): ").lower()

    # Преобразуем данные в бинарный формат
    binary_data = ''.join(format(ord(char), '08b') for char in data)

    # Открываем изображение
    image = Image.open('img01.jpg')

    # Кодируем данные в изображение
    encoded_image = encode_in_channel(image, binary_data, channel)

    # Сохраняем закодированное изображение
    encoded_image.save("encoded_image.png")
    # Сравним mse и psnr
    mse_value = calculate_mse('img01.jpg', 'encoded_image.png')
    print(f'MSE: {mse_value}')
    psnr_value = calculate_psnr(mse_value)
    print(f'PSNR: {psnr_value} dB')
    print("Данные успешно закодированы в изображение и сохранены как encoded_image.png")

if __name__ == "__main__":
    main()
