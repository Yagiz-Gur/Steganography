from PIL import Image

# Function to hide a message in an image
def hide_message(carrier_image_path, message):
    # Open the carrier image
    carrier_image = Image.open(carrier_image_path)

    # Convert the message to binary
    binary_message = ''.join(format(ord(char), '08b') for char in message)

    # Check if the carrier image is large enough to hide the message
    if len(binary_message) > carrier_image.width * carrier_image.height:
        print("Carrier image is not large enough to hide the message.")
        return

    # Hide the message in the pixels of the image
    pixels = list(carrier_image.getdata())
    encoded_pixels = []
    for i, pixel in enumerate(pixels):
        if i < len(binary_message):
            # Modify the least significant bit of each color channel
            encoded_pixel = (
                pixel[0] & 0xFE | int(binary_message[i]),
                pixel[1] & 0xFE | int(binary_message[i]),
                pixel[2] & 0xFE | int(binary_message[i])
            )
            encoded_pixels.append(encoded_pixel)
        else:
            encoded_pixels.append(pixel)

    # Create a new image with the encoded pixels
    encoded_image = Image.new(carrier_image.mode, carrier_image.size)
    encoded_image.putdata(encoded_pixels)

    # Save the stego-image
    encoded_image.save("images/output/stego_image.png")
    print("Stego-image saved successfully.")

# Function to reveal a hidden message from an image
def reveal_message(stego_image_path):
    # Open the stego-image
    stego_image = Image.open(stego_image_path)

    # Retrieve the hidden message from the pixels of the image
    pixels = list(stego_image.getdata())
    binary_message = ''
    for pixel in pixels:
        # Retrieve the least significant bit of each color channel
        bit = pixel[0] & 0x01
        binary_message += str(bit)

    # Convert the binary message back to the original message
    message = ''
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i + 8]
        char = chr(int(byte, 2))
        message += char

    print("Hidden message:", message)

# Main program
def main():
    choice = input("Do you want to hide a message (hide) or reveal a hidden message (reveal)? ")

    if choice.lower() == "hide":
        message = input("Enter the message to hide: ")
        carrier_images = os.listdir("images/input")
        if len(carrier_images) == 0:
            print("No images found in 'images/input' directory.")
            return

        print("Available carrier images:")
        for i, image in enumerate(carrier_images):
            print(f"{i+1}. {image}")

        image_index = int(input("Enter the index of the carrier image: ")) - 1
        if image_index < 0 or image_index >= len(carrier_images):
            print("Invalid image index.")
            return

        carrier_image_path = f"images/input/{carrier_images[image_index]}"
        hide_message(carrier_image_path, message)
    elif choice.lower() == "reveal":
        stego_image_path = input("Enter the path to the stego-image: ")
        reveal_message(stego_image_path)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    import os
    main()