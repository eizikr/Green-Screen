# Green Screen

![Green Screen](https://github.com/eizikr/Green-Screen/raw/main/green-screen.png)

Green Screen is a Python library and command-line tool for removing the green background from images or videos. It provides an easy-to-use interface for chroma keying, allowing users to replace the green screen with any desired background.

## Features

- Supports both images and videos for green screen removal.
- Provides a simple and intuitive API for developers.
- Command-line tool for quick and easy usage.
- Supports popular image and video formats such as PNG, JPEG, MP4, etc.
- Adjustable settings for fine-tuning the green screen removal process.
- Lightweight and efficient implementation.

## Installation

To install Green Screen, you need to have Python 3.x and pip installed on your system. Then, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/eizikr/Green-Screen.git

2. Navigate to the project directory:

   ```bash
   cd Green-Screen
   
3. Install the required dependencies::

   ```bash
   pip install -r requirements.txt
   
   
## Usage

### Using the Command-Line Tool

Green Screen provides a command-line interface for removing the green background from images or videos. Here's how you can use it:

   ```bash
   python green_screen.py --input INPUT_PATH --output OUTPUT_PATH --background BACKGROUND_PATH
   ```
   
   
* 'INPUT_PATH': Path to the input image or video file.
* 'OUTPUT_PATH': Path to save the processed output image or video.
* 'BACKGROUND_PATH': Path to the background image or video to replace the green screen. If not provided, the background will be transparent.

### Using the Python Library

You can also use Green Screen as a Python library in your own projects. Here's a simple example:

   ```bash
   from green_screen import remove_green_screen

   input_path = "input.png"
   output_path = "output.png"
   background_path = "background.png"

   remove_green_screen(input_path, output_path, background_path)
   ```

Make sure to replace the file paths with your own.

## Examples

### Example 1: Removing the Green Screen from an Image

   ```bash
   python green_screen.py --input input.png --output output.png --background background.jpg
   ```

This command removes the green screen from the input.png image and replaces it with the background.jpg image. The resulting image is saved as output.png.

### Example 2: Removing the Green Screen from a Video
   ```bash
   python green_screen.py --input input.mp4 --output output.mp4 --background background.jpg
   ```

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bug fix.

3. Commit your changes.

4. Push your changes to your forked repository.

5. Submit a pull request explaining your changes.

## Acknowledgments

Green Screen was inspired by the idea of chroma keying and built upon the following open-source libraries:

- [OpenCV](https://opencv.org/) - Computer vision library.
- [MoviePy](https://zulko.github.io/moviepy/) - Video editing library.

## Contact
- Name: Itzik Rahamim
- LinkedIn: [Itzik Rahamim](https://www.linkedin.com/in/itzik-rahamim-developer)
- Email: eizikr@icloud.com

---

Thank you for using Green Screen! We hope this tool simplifies your green screen removal process. If you have any questions or need assistance, feel free to reach out.
