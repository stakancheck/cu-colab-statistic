from base64 import decode

from PIL import Image

def extract_data_from_image(image_path):
    image = Image.open(image_path)
    binary_data = ""
    channel_index = 0  # Red channel (так как в прыдущих заданиях использовался красный канал)

    for pixel in image.getdata():
        binary_data += bin(pixel[channel_index])[-1]

    data = ""
    # print(binary_data)
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        if len(byte) == 8:
            char = chr(int(byte, 2))
            if char.isprintable():
                data += char
            # print(chr(int(byte, 2)))
    return data

def find_key_text(extracted_data):
    keyword = "prize"
    lines_with_keyword = [line for line in extracted_data.split('\n') if keyword in line]
    return lines_with_keyword

def analyze_images(image_paths):
    files_with_keyword = []
    for image_path in image_paths:
        extracted_data = extract_data_from_image(image_path)
        print('Extracted data:', extracted_data)
        lines_with_keyword = find_key_text(extracted_data)
        print(lines_with_keyword)
        if lines_with_keyword:
            files_with_keyword.append(image_path)
            print(f"Keyword found in {image_path}:")
            for line in lines_with_keyword:
                print(line)

    if files_with_keyword:
        print(f"Keyword found in files: {', '.join(files_with_keyword)}")
    else:
        print("Keyword not found in any of the files")

if __name__ == "__main__":
    image_paths = ['img.png']
    analyze_images(image_paths)
