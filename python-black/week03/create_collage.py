import os
from PIL import Image, ImageOps

def create_collage(thumbnail_size=(150, 150), border_size=10):
    collage_size = (600 + border_size * 8, 600 + border_size * 8)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    thumbnails_dir = os.path.join(current_dir, 'thumbnails')
    collage_path = os.path.join(current_dir, 'collage.jpg')

    collage = Image.new('RGB', collage_size)

    thumbnails = [f for f in os.listdir(thumbnails_dir) if f.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif'))]

    if len(thumbnails) < 16:
        raise ValueError("Недостаточно миниатюр для создания коллажа 4x4")

    for i, filename in enumerate(thumbnails[:16]):
        img_path = os.path.join(thumbnails_dir, filename)
        with Image.open(img_path) as img:
            img = ImageOps.fit(img, thumbnail_size)
            img = ImageOps.expand(img, border=border_size, fill='black')
            x = (i % 4) * (thumbnail_size[0] + 2 * border_size)
            y = (i // 4) * (thumbnail_size[1] + 2 * border_size)
            collage.paste(img, (x, y))

    collage.save(collage_path)
    print(f'Collage saved as {collage_path}')

create_collage()
