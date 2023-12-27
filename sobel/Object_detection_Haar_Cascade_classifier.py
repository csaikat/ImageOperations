import cv2

image_path = "C:\\Users\\Saikat Chatterjee\\OneDrive\\Desktop\\Image operations\\deer_small.jpg" # Put an absolute/relative path to your image
window_name = f"Detected Objects in {image_path}" # Set name of window that shows image
original_image = cv2.imread(image_path)  # Read image in memory


original_image = cv2.imread(image_path)
rectangle = cv2.rectangle(original_image,
                          (2500, 2000), # X-Y start
                          (1000, 200), # X-Y end
                          (0, 255, 0),
                          2)
cv2.namedWindow(window_name, cv2.WINDOW_KEEPRATIO)



cv2.namedWindow(window_name, cv2.WINDOW_KEEPRATIO) # Create window and set title
cv2.imshow(window_name, original_image)  # Load image in window
cv2.resizeWindow(window_name, (400, 400))  # Resize window

cv2.waitKey(0)  # Keep window open indefinitely until any keypress
cv2.destroyAllWindows()  # Destroy all open OpenCV windows
# Reading the image
...

# Naming the window
...