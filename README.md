# Real-Time-Face-Detector-with-Haar-Cascade

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/yourusername/face-detector/blob/main/LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.7%20|%203.8%20|%203.9%20|%203.10-blue.svg)](https://www.python.org/downloads/release/python-310/)
[![OpenCV Version](https://img.shields.io/badge/opencv-4.5.3-blue.svg)](https://opencv.org/releases/)

A Python code for real-time face detection using the Haar cascade algorithm. This project utilizes the OpenCV library to detect faces in images, videos, or through a webcam feed.

![Face Detector Demo](documentation/face_detector_demo.gif)

## Features

- Detect faces in images, videos, or through a webcam in real-time.
- Utilize the Haar cascade algorithm implemented in OpenCV for accurate face detection.
- Draw rectangles around the detected faces with customizable colors.

## Installation

1. Ensure you have Python 3.7+ installed.
2. Clone this repository:

```bash
git clone https://github.com/yusrap/face-detector.git
```

3. Navigate to the project directory:

```bash
cd face-detector
```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To detect faces through a webcam feed, run the following command:

```bash
python face_detector.py --source webcam
```

To detect faces in a specific image, provide the path to the image file:

```bash
python face_detector.py --source image --path path/to/image.jpg
```

To detect faces in a video, provide the path to the video file:

```bash
python face_detector.py --source video --path path/to/video.mp4
```

You can adjust the sensitivity of the face detection algorithm by modifying the `scale-factor` and `min-neighbors` parameters in the code.

```python
face_coordinates = face_detector.detectMultiScale(grayscale_img, scaleFactor=1.1, minNeighbors=5)
```

## Examples

Here are some examples of how to use the face detector:

```bash
# Detect faces through webcam feed
python face_detector.py --source webcam

# Detect faces in an image
python face_detector.py --source image --path robert_downey.png

# Detect faces in a video
python face_detector.py --source video --path video.mp4
```

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests.

## Acknowledgments

This project utilizes the Haar cascade algorithm implemented in OpenCV. Thanks to the OpenCV community for their valuable contributions.

## Contact

For questions or suggestions, feel free to reach out to [patyusra@outlook.com](mailto:patyusra@outlook.com).