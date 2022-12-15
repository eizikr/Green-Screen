# Green-Screen
using 'OpenCV' package to display an image on a green screen.

# Description:
    - This program was created as part of course 'Image processing and computer vision' (Homework no.1) 
    - The program is using 'OpenCV' package to display an image on a green screen.
    - First it loads 2 images from 'input_images' folder and convert them from BGR to HSV.
    - Then it calculates a mask to cut both images where the pixels are between ''.
    - And finaly connect them together to one image and saves it in 'output_images' folder.

# Environment:
    This program was created to be use in windows 11 OS.
    To use this program you requied:
    -   Installed python 3.11.0 (requied)
    -   Create environment -> 'python -m venv opencv-env' (optional)
        * Activate environment -> '.\opencv-env\Scripts\activate'
        * Deactivate -> 'deactivate'
    -   Install openCV package -> pip install opencv-contrib-python matplotlib

# How to Run Your Program:
    - Activate opencv-env environment -> .\opencv-env\Scripts\activate
    - Install openCV packages.
    - run the program whith 3 input arguments(pathes): (image path) , (background path) , (output path)
        * example: "python green_screen.py ./input_images/studio.jpg ./input_images/background1.JPG  ./output_images/my_output.jpg"

ENJOY!
