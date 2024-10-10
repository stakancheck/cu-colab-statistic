from PIL import Image

def calculate_mse(image1, image2):
    # Открываем изображения
    img1 = Image.open(image1)
    img2 = Image.open(image2)

    # Проверяем, что размеры изображений совпадают
    if img1.size != img2.size:
        raise ValueError('Изображения должны быть одинакового размера')

    # Получаем размеры изображений
    width, height = img1.size

    # Инициализируем переменную для суммы квадратов разностей
    total_error = 0

    # Проходим по каждому пикселю
    for x in range(width):
        for y in range(height):
            # Получаем значение пикселя для каждого изображения (в формате RGB)
            pixel1 = img1.getpixel((x, y))
            pixel2 = img2.getpixel((x, y))

            # Считаем разницу по каждому цветовому каналу (R, G, B)
            for i in range(3):  # R, G, B
                diff = pixel1[i] - pixel2[i]
                total_error += diff ** 2

    # Считаем общее количество пикселей
    num_pixels = width * height * 3  # умножаем на 3, так как у нас три канала (R, G, B)

    # Возвращаем среднеквадратичную ошибку
    mse = total_error / num_pixels
    return mse


if __name__ == '__main__':
    # Пример использования:
    mse_value = calculate_mse('original_image.png', 'encoded_image.png')
    print(f'MSE: {mse_value}')


