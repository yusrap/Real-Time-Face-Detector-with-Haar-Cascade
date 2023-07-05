import cv2
import random
import argparse
import os

# Constants
XML_FILE_PATH = 'haarcascade_frontalface_default.xml'
THICKNESS = 2

# Initialize face detector with pre-trained data
def initialize_face_detector(xml_file_path):
    face_detector = cv2.CascadeClassifier(xml_file_path)
    return face_detector

# Detect faces in an image or video frame
def detect_faces(image, face_detector):
    grayscale_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_coordinates = face_detector.detectMultiScale(grayscale_img)
    return face_coordinates

# Draw rectangles around detected faces
def draw_face_rectangles(image, face_coordinates):
    for (x, y, w, h) in face_coordinates:
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        cv2.rectangle(image, (x, y), (x + w, y + h), color, THICKNESS)

# Main function
def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Face Detector')
    parser.add_argument('--source', choices=['webcam', 'image', 'video'], help='input source type')
    parser.add_argument('--path', help='path to input file')
    args = parser.parse_args()

    # Initialize face detector
    face_detector = initialize_face_detector(XML_FILE_PATH)

    if args.source == 'webcam':
        # Open webcam
        webcam = cv2.VideoCapture(0)

        # Check if the webcam is opened successfully
        if not webcam.isOpened():
            print("Error opening webcam.")
            return

        print("Press 'q' or 'Q' to exit.")

        while True:
            # Read the current frame
            successful_frame_read, frame = webcam.read()

            # Detect faces in the frame
            face_coordinates = detect_faces(frame, face_detector)

            # Draw rectangles around detected faces
            draw_face_rectangles(frame, face_coordinates)

            # Display the frame with rectangles around detected faces
            cv2.namedWindow("Face Detector", cv2.WINDOW_NORMAL)
            cv2.imshow('Face Detector', frame)

            # Refresh rate of 1ms; press 'q' key to stop the loop and close the window
            key = cv2.waitKey(1)
            if key in (ord('q'), ord('Q')):
                break

        # Release the webcam and close the window
        webcam.release()
        cv2.destroyAllWindows()

    elif args.source == 'image':
        # Get the absolute path to the image file within the 'assets' subdirectory
        image_path = os.path.join('assets', args.path)

        # Load the image
        image = cv2.imread(image_path)

        if image is None:
            print("Error loading image. Please provide a valid image path.")
            return

        print("Press 'q' or 'Q' to exit.")

        # Detect faces in the image
        face_coordinates = detect_faces(image, face_detector)

        # Draw rectangles around detected faces
        draw_face_rectangles(image, face_coordinates)

        # Display the image with rectangles around detected faces
        cv2.namedWindow("Face Detector", cv2.WINDOW_NORMAL)
        cv2.imshow('Face Detector', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif args.source == 'video':
        # Get the absolute path to the video file within the 'assets' subdirectory
        video_path = os.path.join('assets', args.path)

        # Load the video 
        video = cv2.VideoCapture(video_path)

        # Check if the video is opened successfully
        if not video.isOpened():
            print("Error opening video file. Please provide a valid video path.")
            return

        print("Press 'q' or 'Q' to exit.")

        while True:
            # Read the current frame
            successful_frame_read, frame = video.read()

            if not successful_frame_read:
                break

            # Detect faces in the frame
            face_coordinates = detect_faces(frame, face_detector)

            # Draw rectangles around detected faces
            draw_face_rectangles(frame, face_coordinates)

            # Display the frame with rectangles around detected faces
            cv2.namedWindow("Face Detector", cv2.WINDOW_NORMAL)
            cv2.imshow('Face Detector', frame)

            # Refresh rate of 1ms; press 'q' key to stop the loop and close the window
            key = cv2.waitKeyEx(1)
            if key in (ord('q'), ord('Q')):
                break

        # Release the video and close the window
        video.release()
        cv2.destroyAllWindows()

    else:
        print("Invalid input. Please choose 'webcam', 'image', or 'video' as the input source.")

    print("Code completed.")

if __name__ == "__main__":
    main()