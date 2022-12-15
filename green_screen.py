import cv2 as cv
import numpy as np
import sys


def main():

    if(len(sys.argv) < 4):
        print('Too few argoments! (required image_path, background_path, output_path)')
    
    elif(len(sys.argv) > 4):
        print('Too much argoments! (required image_path, background_path, output_path)')
    
    # Get path for images
    IMAGE_PATH = sys.argv[1]
    BACKGROUND_PATH = sys.argv[2]
    OUTPUT_PATH = sys.argv[3]
    
    # Load images
    img = cv.imread(IMAGE_PATH, cv.IMREAD_COLOR)
    bg = cv.imread(BACKGROUND_PATH, cv.IMREAD_COLOR)

    # Convert images from BGR to HSV
    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    hsv_bg = cv.cvtColor(bg, cv.COLOR_BGR2HSV)

    # Resize background image to be equal to the image (img)
    bg_resized = cv.resize(hsv_bg, (img.shape[1], img.shape[0]))

    # Define Threshold for green screen color
    lower = np.array([52, 85, 55])
    upper = np.array([86, 255, 255])

    # Create a green mask
    mask = cv.inRange(hsv_img, lower, upper)

    # Create an image and background mask
    masked_image = np.copy(hsv_img)
    masked_image[mask != 0] = [0, 0, 0]
    bg_resized[mask == 0] = [0, 0, 0]

    # Connect two images (as matrix) into one
    final_image = bg_resized + masked_image

    ## Show on screen -> optional if you want to test, just remove '#'
    # plt.imshow(cv.cvtColor(final_image, cv.COLOR_HSV2RGB),cmap='gray')
    # plt.show()

    # Create output image on OUTPUT_PATH (as RGB)
    cv.imwrite(OUTPUT_PATH, cv.cvtColor(final_image, cv.COLOR_HSV2BGR))
    
if __name__ == "__main__":
    main()