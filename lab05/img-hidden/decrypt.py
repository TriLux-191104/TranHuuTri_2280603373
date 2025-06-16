import sys
from PIL import Image

def decode_image(encoded_image_path):
    img = Image.open(encoded_image_path)
    width, height = img.size
    binary_message = ""

    # Duyệt từng pixel để lấy từng bit cuối
    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))  # (R, G, B)

            for color_channel in range(3):  # R, G, B
                binary_message += format(pixel[color_channel], '08b')[-1]

    # Chuyển các nhóm 8 bit về ký tự
    message = ""
    for i in range(0, len(binary_message), 8):
        char = chr(int(binary_message[i:i+8], 2))
        if char == '\0':
            break
        message += char

    return message

def main():
    if len(sys.argv) != 2:
        print("Usage: python decrypt.py <encoded_image_path>")
        return

    encoded_image_path = sys.argv[1]
    decoded_message = decode_image(encoded_image_path)
    print("📩 Decoded message:", decoded_message)

if __name__ == "__main__":
    main()
