import cv2

# Read image
img = cv2.imread("C:\\Users\\gnane\\Pictures\\KKK.jpg")

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection
edges = cv2.Canny(gray, 100, 200)

# Show the original image and the Canny edges side by side
cv2.imwrite('Canny_Edges_3rd.jpg', edges)