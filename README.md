# License Plate Detection and Recognition System

- This project demonstrates how to detect and recognize license plates from an image using Python Image Processing.
- It is a practical implementation of computer vision and OCR techniques, suitable for applications such as vehicle monitoring systems or parking management.
- it only works for images

## IMAGES 

### Processed Image
<img src="https://res.cloudinary.com/diekemzs9/image/upload/v1729189076/b_w_lf6bcd.png" alt="Original Image" width="800"/>

### Number plate extraction
<img src="https://res.cloudinary.com/diekemzs9/image/upload/v1729189095/plate_gqyfkm.png" alt="Edge Detection" width="800"/>

### Final output
<img src="https://res.cloudinary.com/diekemzs9/image/upload/v1729189084/final_uoxcot.png" alt="Detected Plate" width="800"/>


### Image Processing Workflow

1. **Reading the Image**: The input image is read using OpenCV, and then it's displayed using `matplotlib` for visualization.
2. **Grayscale Conversion**: The image is converted to grayscale to simplify processing, focusing on intensity rather than color.
3. **Noise Reduction**: A bilateral filter is applied to reduce noise while preserving the edges, preparing the image for edge detection.
4. **Edge Detection**: The Canny edge detection algorithm is used to identify edges, highlighting the boundaries of objects like the license plate.
5. **Finding Contours**: The system identifies contours (closed shapes) in the image, filtering out the most relevant contours that are likely to be the license plate.
6. **Approximating License Plate**: A polygon approximation is used to detect a quadrilateral contour, assuming the license plate is rectangular.
7. **Masking and Cropping**: The license plate area is isolated from the image, and the region is cropped for OCR.
8. **Text Recognition**: EasyOCR is used to extract text from the cropped license plate image.



## Installation

Installing dependencies:

```bash
pip install easyocr
pip install imutils
pip install opencv-python
pip install matplotlib
```
