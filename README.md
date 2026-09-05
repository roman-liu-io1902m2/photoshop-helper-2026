# photoshop-helper-2026

## A Python-Powered Workflow Enhancer for Adobe Photoshop

`photoshop-helper-2026` is a robust Python utility designed to streamline common tasks and automate repetitive processes for Adobe Photoshop users. By providing a suite of scripts and tools, this project aims to significantly enhance your productivity, reduce manual effort, and ensure consistency in your design and image processing workflows.

Whether you're a graphic designer, photographer, or digital artist, `photoshop-helper-2026` offers intelligent solutions to manage your assets, preprocess images, and prepare your projects with greater efficiency.

## Features

-   **Batch Image Processing:** Automate tasks like resizing, watermarking, format conversion, and applying basic filters to multiple images.
-   **Asset Organization:** Tools to intelligently sort, rename, and structure image files and project assets, making them ready for Photoshop.
-   **Metadata Management:** Read and write image metadata (EXIF, IPTC) to assist with cataloging and searchability.
-   **Layer Generation (Future):** Scripts to assist in generating boilerplate layers or assets based on data inputs (e.g., creating multiple text layers from a list).
-   **Smart Export Preparation:** Prepare images for specific export requirements (e.g., web optimization, print-ready formats) before opening them in Photoshop.
-   **Custom Scripting Hooks:** Easily extend the helper's functionality with your own Python scripts to tailor it to unique workflows.

## Installation

To get started with `photoshop-helper-2026`, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/photoshop-helper-2026.git
    cd photoshop-helper-2026
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage Example

Here's a simple example demonstrating how to use `photoshop-helper-2026` to batch resize all `.jpg` images in a `source_images` directory and save them to an `output_images` directory.

```python
import os
from photoshop_helper.image_processor import resize_images

# Define input and output directories
input_dir = "source_images"
output_dir = "output_images"

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Define target dimensions (e.g., 800 pixels wide, maintaining aspect ratio)
target_width = 800

print(f"Resizing images from '{input_dir}' to '{output_dir}' with width {target_width}px...")

# Use the resize_images function
# This function would iterate through the input_dir, resize JPEGs, and save them.
# The actual implementation of resize_images would be within the photoshop_helper package.
resize_images(input_folder=input_dir, output_folder=output_dir, target_width=target_width, format="JPEG", quality=85)

print("Image resizing complete!")
print(f"Check the resized images in the '{output_dir}' directory.")
```

To run this example, save it as a Python file (e.g., `resize_script.py`) in the root of your `photoshop-helper-2026` directory, ensure you have a `source_images` folder with some `.jpg` files, and then execute:

```bash
python resize_script.py
```

## Configuration

`photoshop-helper-2026` can be configured via a `config.ini` file located in the root directory of the project, or through environment variables for sensitive settings