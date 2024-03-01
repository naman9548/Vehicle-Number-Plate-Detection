# Vehicle Number Plate Recognition System

## Overview
This project implements a vehicle number plate recognition system using OpenCV and EasyOCR in Python. The system detects license plates in live video streams, extracts text from the plates, and checks them against a specified vehicle number. If a match is found, the system alerts the user. This system can be used for various applications such as parking management, toll collection, and law enforcement.

## Components
### Dependencies
- `cv2`: OpenCV library for image and video processing.
- `easyocr`: Python library for optical character recognition (OCR).
- `re`: Regular expression module for text manipulation.
- `time`: Module for time-related functions.

## Functionality
### License Plate Detection
- The system captures video frames from a webcam using OpenCV.
- It detects license plates in each frame using a pre-trained Haar cascade classifier.
- Detected plates are then cropped and passed to the OCR module for text extraction.

### Optical Character Recognition (OCR)
- EasyOCR library is used to extract text from the detected license plate images.
- Detected text is processed to remove special characters and ensure uniform formatting.
- The system checks if the extracted text matches the specified vehicle number.

### Alerting
- If a match is found, the system alerts the user by printing a message to the console and marking the detected license plate in the video stream.

## Usage
1. Run the script (`python main.py`).
2. Enter the vehicle number you want to detect when prompted.
3. Detected license plates matching the specified vehicle number will be highlighted in the video stream.

## Project Structure
- `main.py`: Main script implementing the vehicle number plate recognition system.
- `model/`: Directory containing the pre-trained Haar cascade classifier for license plate detection.
- `plates/`: Directory to store images of detected license plates.
- `README.md`: Documentation providing an overview of the project, usage instructions, and setup details.

## Setup
### Installation
1. Clone the repository: `git clone <repository_url>`.
2. Install dependencies: `pip install -r requirements.txt`.

### Execution
- Run the script: `python main.py`.

## Note
- Ensure proper lighting conditions and camera positioning for optimal license plate detection.
- This system is designed for demonstration purposes and may require further optimization for real-world applications.

## Author
- **Naman Deol**: (https://www.linkedin.com/in/naman-deol-b1a581232/)

## Contributions
- Contributions are welcome! Please submit issues or pull requests for any enhancements or bug fixes.

## Contact
- For inquiries or feedback, feel free to contact the author via LinkedIn.
