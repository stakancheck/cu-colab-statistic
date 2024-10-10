import os
from PIL import Image, ImageFilter

def apply_filter(filter):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_dir = os.path.join(current_dir, 'photos_for_processing')
    output_dir = os.path.join(current_dir, 'filtered_images')

    os.makedirs(output_dir, exist_ok=True)

    filter_map = {
        'SHARPEN': ImageFilter.SHARPEN,
        'BLUR': ImageFilter.BLUR,
        'CONTOUR': ImageFilter.CONTOUR,
        'SMOOTH': ImageFilter.SMOOTH
    }

    if filter not in filter_map:
        print(f'Фильтра {filter} нет. Выход.')
        return

    for filename in os.listdir(input_dir):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
            img_path = os.path.join(input_dir, filename)
            with Image.open(img_path) as img:
                img = img.filter(filter_map[filter])
                output_path = os.path.join(output_dir, filename)
                img.save(output_path)
                print(f'Применён фильтр {filter} к {filename} и сохранён в {output_path}')

# Пример вызова функции
apply_filter('BLUR')
