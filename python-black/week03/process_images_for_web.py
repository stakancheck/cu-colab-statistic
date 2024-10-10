import os
from PIL import Image, ImageOps

def process_images_for_web(target_size=(800, 800)):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_dir = os.path.join(current_dir, 'photos_for_processing')
    output_dir = os.path.join(current_dir, 'processed_images')

    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
            img_path = os.path.join(input_dir, filename)
            with Image.open(img_path) as img:
                img = ImageOps.fit(img, target_size)
                output_path = os.path.join(output_dir, filename)
                img.save(output_path)
                print(f'Processed {filename} and saved to {output_path}')

process_images_for_web()
