import pytesseract
import os
import cv2

def image_standardization(image):
    # Define the scale factor for upscaling
    scale_factor = 2 

    # Upscale the image
    upscaled_image = cv2.resize(image, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_LINEAR)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(upscaled_image, cv2.COLOR_BGR2GRAY)


    # Apply Gaussian blur for denoising
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # Apply Otsu's thresholding for binarization
    _, thresholded_image = cv2.threshold(blurred_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    return(thresholded_image)

def images_to_text(images_path):
    # initialize the the text results
    text = []

    # the sorting is very weird since python does random access, I will loop through the files here but a natsort is better
    for i in range(len(os.listdir(images_path))):
        # Load image
        image = image_standardization(cv2.imread(os.path.join(images_path, f"image_{i+1}.png")))
        # Extract text
        text.append(pytesseract.image_to_string(image, config=f'--psm {7}'))

    # return the text list
    return text

# We want a .txt file 
def convert_str_to_txt(text):
    # open a new output.txt file
    with open('../output.txt', 'w') as f:
        # write the lines in
        for line in text:
            f.write(f"{line}")