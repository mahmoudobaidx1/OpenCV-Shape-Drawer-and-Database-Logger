# OpenCV Shape Drawer and Database Logger

A simple Python-based application that allows users to draw various geometric shapes (lines, triangles, rectangles, pentagons, and hexagons) onto an image using **OpenCV**, resize or modify the output interactively, and store pixel color data into an **SQLite3** database.

## Features

* **Interactive Shape Drawing:** Dynamically draw lines, triangles, rectangles, pentagons, and hexagons by entering pixel coordinates via the command line.
* **Image Validation:** Automatically checks whether user-provided coordinates fall within the dimensions of the base image.
* **Real-time Image Modification:**
  * Press **`t`** to double the image size ($2\times$).
  * Press **`f`** to halve the image size ($1/2\times$).
  * Press **`q`** to quit and save the pixel values.
* **SQLite Integration:** Automatically extracts and logs the blue, green, and red (BGR) color components of the image pixels into a local SQLite database (`shapes.db`).

---

## Prerequisites

Make sure you have **Python** installed along with the required libraries. You will need:

* `opencv-python`
* `numpy`

### Installation

Install the required packages using pip:

```bash
pip install opencv-python numpy
```

---

## Project Structure

```text
├── shapes.py                  # Main script containing the Draw_shapes class
├── istockphoto-...jpg         # Base image template used for drawing
└── shapes.db                  # SQLite database generated upon saving (created automatically)
```

*(Note: Ensure that your template image filename matches the one specified in the script—e.g., `istockphoto-1370544962-612x612.jpg`—or update the `cv2.imread()` path accordingly.)*

---

## Usage

1. Run the script from your terminal:
   ```bash
   python shapes.py
   ```

2. When prompted, enter the number of points corresponding to the shape you want to draw:
   * **`2`** $\rightarrow$ Line
   * **`3`** $\rightarrow$ Triangle
   * **`4`** $\rightarrow$ Rectangle
   * **`5`** $\rightarrow$ Pentagon
   * **`6`** $\rightarrow$ Hexagon

3. Follow the console instructions to input the specific $(x, y)$ coordinate points for each vertex.

4. Once the image window pops up:
   * Press **`t`** to scale up.
   * Press **`f`** to scale down.
   * Press **`q`** to save the pixel data to the database and exit.

---

## Database Schema

The script automatically creates an SQLite database named `shapes.db` with a table structured to store the shape name and individual pixel color values:

* **Table Name:** `shapes`
* **Columns:**
  * `name` (TEXT): The name of the drawn shape.
  * `b` (INTEGER): Blue channel value.
  * `g` (INTEGER): Green channel value.
  * `r` (INTEGER): Red channel value.

---

## License

This project is open-source and available for educational and personal use.