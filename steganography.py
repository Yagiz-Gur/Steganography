from PIL import Image

def hide_message(image, message):
    # Convert message to binary
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    
    # Open the image
    img = Image.open(image)
    width, height = img.size
    
    # Check if message can fit in the image
    if len(binary_message) > width * height * 3:
        raise ValueError("Message is too large to fit in the image.")
    
    # Iterate over each pixel of the image
    pixel_index = 0
    for w in range(width):
        for h in range(height):
            if pixel_index < len(binary_message):
                # Get the RGB values of the pixel
                r, g, b = img.getpixel((w, h))
                
                # Modify the least significant bit of each color component
                r = (r & 0xFE) | int(binary_message[pixel_index])
                pixel_index += 1
                
                if pixel_index < len(binary_message):
                    g = (g & 0xFE) | int(binary_message[pixel_index])
                    pixel_index += 1
                    
                if pixel_index < len(binary_message):
                    b = (b & 0xFE) | int(binary_message[pixel_index])
                    pixel_index += 1
                
                # Update the pixel with modified RGB values
                img.putpixel((w, h), (r, g, b))
    
    # Save the stego-image
    output_image = 'images/output/stego_image.png'
    img.save(output_image)
    print("Stego-image saved successfully!")
    return output_image


def reveal_message(image):
    # Open the stego-image
    img = Image.open(image)
    width, height = img.size
    
    # Retrieve the hidden message from the least significant bits of each pixel
    binary_message = ""
    for w in range(width):
        for h in range(height):
            r, g, b = img.getpixel((w, h))
            binary_message += str(r & 0x01)
            binary_message += str(g & 0x01)
            binary_message += str(b & 0x01)
    
    # Convert binary message back to characters
    message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        char = chr(int(byte, 2))
        message += char
    
    return message


def main():
    option = input("Enter 'hide' to hide a message or 'reveal' to reveal a hidden message: ")
    
    if option == 'hide':
        message = input("Enter the message to hide: ")
        
        print("Available carrier images:")
        import glob
        carrier_images = glob.glob('images/input/*.png')
        for i, image in enumerate(carrier_images):
            print(f"{i+1}. {image}")
        
        selected_image = input("Enter the number of the image to use as a carrier: ")
        selected_image = int(selected_image)
        
        if selected_image < 1 or selected_image > len(carrier_images):
            print("Invalid image selection.")
            return
        
        image = carrier_images[selected_image - 1]
        
        try:
            stego_image = hide_message(image, message)
            print(f"Stego-image: {stego_image}")
        except Exception as e:
            print(f"Error: {str(e)}")
    
    elif option == 'reveal':
        print("Available images to reveal the hidden message:")
        import glob
        stego_images = glob.glob('images/output/*.png')
        for i, image in enumerate(stego_images):
            print(f"{i+1}. {image}")
        
        selected_image = input("Enter the number of the image to reveal the hidden message: ")
        selected_image = int(selected_image)
        
        if selected_image < 1 or selected_image > len(stego_images):
            print("Invalid image selection.")
            return
        
        image = stego_images[selected_image - 1]
        
        try:
            message = reveal_message(image)
            print(f"Hidden message: {message}")
        except Exception as e:
            print(f"Error: {str(e)}")
    
    else:
        print("Invalid option.")


if __name__ == '__main__':
    main()
