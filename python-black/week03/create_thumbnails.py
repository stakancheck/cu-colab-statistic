import os
from PIL import Image

def create_thumbnails(thumbnail_size=(150, 150)):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_dir = os.path.join(current_dir, 'photos_for_processing')

    if not os.path.exists(input_dir):
        print('Directory with images not found')
        return

    output_dir = os.path.join(current_dir, 'thumbnails')

    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
            img_path = os.path.join(input_dir, filename)
            with Image.open(img_path) as img:
                img.thumbnail(thumbnail_size)
                thumb_filename = f'thumb_{filename}'
                thumb_path = os.path.join(output_dir, thumb_filename)
                img.save(thumb_path)
                print(f'Saved thumbnail for {filename} as {thumb_filename}')


def main():
    input_user = input('Enter thumbnail size (Like: width height), or press Enter: ')
    thumbnail_size = (150, 150)
    if input_user:
        thumbnail_size = tuple(map(int, input_user.split()))
    create_thumbnails(thumbnail_size)


main()
