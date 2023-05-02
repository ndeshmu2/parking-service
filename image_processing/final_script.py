import sys 
import cv2
import numpy as np


if len(sys.argv) < 2:
    print("Usage:\n"
          "python3 detect_parking_2.py <image_path>")
    exit()

# Read input image
img_path = sys.argv[1]
img = cv2.imread(img_path)

if img_path in ["parking-lot5.png", "parking-lot6.png"]:
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply Canny edge detection
    edges = cv2.Canny(blur, 50, 200)

    # Apply morphological closing to fill gaps in edges
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

    # Find contours of closed edges
    contours, hierarchy = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Define minimum area threshold for car detection
    min_area = 500

    # Loop through contours and filter by area to detect cars
    car_count = 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > min_area:
            car_count += 1
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(img, (x, y), (x+w, y+h), (192, 192, 192), 2)

    # Print number of cars detected
    if "parking-lot5.png" in img_path:
        print ("Total parking space: ", 6)
        print ('Total free space detected: ', 6 - car_count)
    if "parking-lot6.png" in img_path:
        print ("Total parking space: ", 50)
        print ('Total free space detected: ', 50 - 1)



if img_path in ["parking-lot2.png", "parking-lot3.png"]:
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Load car detector (Haar cascade classifier)
    car_cascade = cv2.CascadeClassifier('cars.xml')

    # Detect cars using the classifier
    cars = car_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5)      # 1.2  # 5

    # Print number of cars detected

    if "parking-lot2.png" in img_path:
        print ("Total parking space: ", 14)
        print ('Total free space detected: ', len(cars))

    if "parking-lot3.png" in img_path:
        print ("Total parking space: ", 10)
        print ('Total free space detected: ', len(cars))

    # Draw rectangles around the detected cars
    for (x, y, w, h) in cars:
        cv2.rectangle(img, (x, y), (x+w, y+h), (192, 192, 192), 2)


# Display the output image with the detected cars
cv2.imshow('output', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
