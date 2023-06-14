# Table of contents
- [What is Steganography](#what-is-it)
- [How does it works on images?](#how-does-it-work)
- [steganography.py](#steganography.py)



# <a id="what-is-it">What is Steganography ? </a>

![1](https://miro.medium.com/v2/resize:fit:1400/1*dQyfOpFWmSxrmdOcQgW6OQ.jpeg)
  
Steganography is the practice of concealing secret information or messages within non-secret data or media, such as images, audio files, or text. Unlike encryption, which focuses on keeping the content of a message secret, steganography aims to hide the very existence of the message.

The main idea behind steganography is to embed the secret data into the carrier medium in such a way that it remains undetectable to an observer. This can be achieved by making subtle modifications to the carrier's data, which are typically imperceptible to the human senses. For example, altering the least significant bits of pixel values in an image or introducing small changes in the audio spectrum.

The hidden message can only be extracted or revealed by someone who possesses the appropriate knowledge or tools to decipher it. This can involve using a specific steganography algorithm or a secret key known only to the intended recipient.

Steganography has been used throughout history to exchange confidential information, and it continues to have applications in various fields, including digital forensics, data protection, and covert communication.

#  <a id="how-does-it-work" >How does it works on images?
</a >

![2](https://miro.medium.com/v2/resize:fit:1400/1*Gu_RomzVTPMEJ1hfKanRBA.png)
Steganography works on images by embedding secret data within the pixels of the image without significantly altering its visual appearance. Here's a simplified explanation of how steganography can be applied to images:

1.  **Selecting a carrier image:** A carrier image is chosen as the medium to hide the secret data. It could be any regular image, such as a JPEG or PNG file.
    
2.  **Encoding the secret data:** The secret data, which could be text, another image, or any other form of information, is converted into a binary format.
    
3.  **Determining the embedding method:** Different embedding techniques can be employed to hide the secret data within the image. One common approach is to modify the least significant bits (LSBs) of the pixel values.
    
4.  **Embedding the secret data:** The binary representation of the secret data is inserted into the LSBs of the pixel values in the carrier image. Since the changes are typically subtle, they are often imperceptible to the human eye.
    
5.  **Generating the stego-image:** The modified pixel values, containing the hidden data, are used to create a new image known as the stego-image. This image appears similar to the original carrier image and can be shared or transmitted without arousing suspicion.
    
6.  **Extracting the hidden data:** To extract the hidden data from the stego-image, a recipient must possess the knowledge of the steganography algorithm and, if applicable, the secret key. By reversing the embedding process, the LSBs are extracted and combined to reconstruct the original secret data.
    

It's important to note that more advanced steganography techniques exist, utilizing complex algorithms and employing various image properties to hide data. Additionally, steganalysis techniques are continually developed to detect and analyze potential steganographic content within images.


# <a id="steganography.py">steganography.py</a>

