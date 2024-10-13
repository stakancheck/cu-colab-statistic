from PIL import Image, ImageDraw


def find_colored_objects(image, target_color, tolerance=30, box_color=(255, 0, 0)):
    """
    Find objects of the target color in the image and draw rectangles around them.

    :param image: Image to process
    :param target_color: Target color as an RGB tuple
    :param tolerance: Tolerance for color matching
    :param box_color: Color of the rectangle to draw
    """
    img = image.copy()
    draw = ImageDraw.Draw(img)
    width, height = img.size
    pixels = img.load()

    def color_within_tolerance(color1, color2, tolerance):
        return all(abs(c1 - c2) <= tolerance for c1, c2 in zip(color1, color2))

    visited = set()
    boxes = []

    def flood_fill(x, y):
        stack = [(x, y)]
        min_x, min_y, max_x, max_y = x, y, x, y
        while stack:
            cx, cy = stack.pop()
            if (cx, cy) in visited:
                continue
            visited.add((cx, cy))
            if not color_within_tolerance(pixels[cx, cy], target_color, tolerance):
                continue
            min_x, min_y = min(min_x, cx), min(min_y, cy)
            max_x, max_y = max(max_x, cx), max(max_y, cy)
            for nx, ny in [(cx - 1, cy), (cx + 1, cy), (cx, cy - 1), (cx, cy + 1)]:
                if 0 <= nx < width and 0 <= ny < height and (nx, ny) not in visited:
                    stack.append((nx, ny))
        return min_x, min_y, max_x, max_y

    for y in range(height):
        for x in range(width):
            if (x, y) not in visited and color_within_tolerance(pixels[x, y], target_color, tolerance):
                box = flood_fill(x, y)
                if box:
                    boxes.append(box)

    for box in boxes:
        draw.rectangle(box, outline=box_color)

    return img


if __name__ == "__main__":
    image = Image.open('mario.png')
    target_color = (255, 0, 0)  # Example target color (red)
    result_image = find_colored_objects(image, target_color)
    result_image.save('output_image.png')
