# What is LSB (least significant bit) ?

![1](https://upload.wikimedia.org/wikipedia/commons/0/0c/LeastSignificantBitDemonstration.jpg)
  
The least significant bit (LSB) refers to the rightmost bit in a binary representation of a number. In the context of steganography, modifying the LSB of pixel values in an image is a common technique to hide information.

Let's take an example using a grayscale image to demonstrate LSB manipulation. Grayscale images have pixel values ranging from 0 (black) to 255 (white).

Suppose we have a pixel with an original value of 170, which, in binary, is represented as 10101010. Each bit represents a level of intensity in the image. By modifying the LSB, we can hide one bit of information without significantly changing the overall appearance of the image.

Let's say we want to hide the binary value 0110. To do this, we replace the LSB of the pixel value with each corresponding bit of the hidden data, as follows:

---

Original pixel value: 10101010 
Hidden data: 0110 
Modified pixel value: 1010101[0]

As you can see, the LSB of the pixel value has been changed to 0 to accommodate the hidden data. In this case, the change is subtle and unlikely to be visually noticeable.

To extract the hidden data, one would simply examine the LSB of each pixel in the stego-image and concatenate them to reconstruct the original hidden data.

It's worth noting that LSB manipulation is just one of many techniques used in steganography. More complex methods can involve modifying multiple bits, employing color channels in color images, or utilizing frequency domains for greater embedding capacity and resilience against detection.
