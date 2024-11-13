# # #improve the image quality

import cv2

image = cv2.imread("C:/Image quality increase/IMG-20241030-WA0004.jpg")
denoised_image = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)
cv2.imwrite("C:\Image quality increase\enhanced_image.jpg", denoised_image)





#jpg to png converter


# import cv2

# # Load the JPG image
# input_path = "C:/Users/Viswajith/Downloads/realistic-red-swirling-arrow-illustration-white_88188-921.jpg"  # Replace with your JPG image path
# image = cv2.imread(input_path)

# # Save the image in PNG format
# output_path = "C:/Image quality increase/image1.png"  # Replace with your desired output path
# cv2.imwrite(output_path, image)

# print("Conversion completed: JPG to PNG.")




#-----------------

#jpg to png for any background 



# from PIL import Image
# import numpy as np
# from rembg import remove  # More reliable background removal

# def convert_jpg_to_transparent_png(input_path, output_path):
#     """
#     Convert a JPG image to a PNG with transparency using rembg library.
    
#     Parameters:
#     input_path (str): Path to input JPG file
#     output_path (str): Path to save the output PNG file
    
#     Returns:
#     bool: True if conversion is successful, False otherwise
#     """
#     try:
#         # Open the image
#         input_image = Image.open(input_path)
        
#         # Remove background
#         output_image = remove(input_image)
        
#         # Save as PNG with transparency
#         output_image.save(output_path, 'PNG')
#         return True
            
#     except Exception as e:
#         print(f"Error converting image: {str(e)}")
#         return False

# # Alternative method without using rembg
# def convert_jpg_to_transparent_png_manual(input_path, output_path, threshold=240):
#     """
#     Convert a JPG image to a PNG with transparency using manual method.
#     Better for images with white backgrounds.
    
#     Parameters:
#     input_path (str): Path to input JPG file
#     output_path (str): Path to save the output PNG file
#     threshold (int): Brightness threshold for transparency (0-255)
#     """
#     try:
#         # Open the image
#         img = Image.open(input_path)
        
#         # Convert to RGBA if it isn't already
#         if img.mode != 'RGBA':
#             img = img.convert('RGBA')
        
#         # Get the image data as a numpy array
#         data = np.array(img)
        
#         # Calculate brightness
#         r, g, b, a = data.T
#         brightness = (r + g + b) / 3
        
#         # Create mask for bright pixels
#         white_areas = brightness > threshold
        
#         # Set alpha channel to 0 (transparent) for bright pixels
#         data[..., 3] = np.where(white_areas.T, 0, 255)
        
#         # Create new image with modified alpha channel
#         result = Image.fromarray(data)
        
#         # Save as PNG
#         result.save(output_path, 'PNG')
#         return True
        
#     except Exception as e:
#         print(f"Error converting image: {str(e)}")
#         return False

# # Example usage
# if __name__ == "__main__":
#     input_file = "C:/Users/Viswajith/Downloads/alexander-shatov-k1xf2D7jWUs-unsplash.jpg"
#     output_file = "C:/Users/Viswajith/Downloads/output1.png"
    
#     # Method 1: Using rembg (recommended)
#     print("Installing required package...")
#     import subprocess
#     subprocess.run(["pip", "install", "rembg"])
    
#     print("Converting image using rembg...")
#     success = convert_jpg_to_transparent_png(input_file, output_file)
    
#     if not success:
#         print("Trying alternative method...")
#         success = convert_jpg_to_transparent_png_manual(input_file, output_file)
    
#     if success:
#         print("Image converted successfully!")
#     else:
#         print("Conversion failed.")







