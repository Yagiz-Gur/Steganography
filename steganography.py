from PIL import Image
import os

def hide_message(image_path, message):
    img = Image.open(image_path)
    width, height = img.size

    message += "/end"  # Add '/end' to mark the end of the message

    binary_message = ''.join(format(ord(char), '08b') for char in message)  # Convert message to binary

    if len(binary_message) > width * height * 3:
        raise ValueError("Message is too large for the image")

    index = 0
    for y in range(height):
        for x in range(width):
            pixel = list(img.getpixel((x, y)))

            # Hide the message bits in the least significant bit of each color channel (RGB)
            for i in range(3):
                if index < len(binary_message):
                    pixel[i] = pixel[i] & 0b11111110 | int(binary_message[index])
                    index += 1

            img.putpixel((x, y), tuple(pixel))

    output_path = "images/output/stego_image.png"
    img.save(output_path)
    print("Stego-image saved successfully as", output_path)


def reveal_message(image_path):
    img = Image.open(image_path)
    width, height = img.size

    binary_message = ""

    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))

            # Extract the least significant bit of each color channel (RGB)
            for i in range(3):
                binary_message += str(pixel[i] & 1)

            if binary_message[-4:] == "/end":  # Check if the end of message marker is detected
                binary_message = binary_message[:-4]  # Remove the marker from the message
                message = ""
                for i in range(0, len(binary_message), 8):  # Convert binary to characters
                    char = binary_message[i:i+8]
                    message += chr(int(char, 2))
                print("Hidden message extracted successfully:", message)
                return

    print("End of message not found")


def main():
    option = input("Do you want to hide or reveal a hidden message? (hide/reveal): ")

    if option == "hide":
        message = input("Enter the message you want to hide: ")
        message = message + "/end"
        image_dir = "images/input/"
        image_files = os.listdir(image_dir)
        print("Available carrier images:")
        for i, file in enumerate(image_files):
            print(i+1, "-", file)
        image_index = int(input("Select the index of the carrier image: ")) - 1
        image_path = image_dir + image_files[image_index]

        hide_message(image_path, message)
    elif option == "reveal":
        image_dir = "images/input/"
        image_files = os.listdir(image_dir)
        print("Available images:")
        for i, file in enumerate(image_files):
            print(i+1, "-", file)
        image_index = int(input("Select the index of the image to extract hidden message: ")) - 1
        image_path = image_dir + image_files[image_index]

        reveal_message(image_path)
    else:
        print("Invalid option. Please select 'hide' or 'reveal'.")


if __name__ == "__main__":
    main()
