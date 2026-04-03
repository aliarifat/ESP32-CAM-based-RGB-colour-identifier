import cv2
import urllib.request
import numpy as np

def nothing(x):
    pass

url = 'http://192.168.1.108/cam-hi.jpg'
cv2.namedWindow("live transmission", cv2.WINDOW_AUTOSIZE)

# Red, Green, and Blue HSV ranges
red_lower1 = np.array([0, 120, 70])
red_upper1 = np.array([10, 255, 255])

red_lower2 = np.array([170, 120, 70])
red_upper2 = np.array([180, 255, 255])

green_lower = np.array([40, 70, 70])
green_upper = np.array([80, 255, 255])

blue_lower = np.array([90, 70, 70])
blue_upper = np.array([130, 255, 255])

while True:
    img_resp = urllib.request.urlopen(url)
    imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
    frame = cv2.imdecode(imgnp, -1)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create masks for Red, Green, and Blue
    mask_red1 = cv2.inRange(hsv, red_lower1, red_upper1)
    mask_red2 = cv2.inRange(hsv, red_lower2, red_upper2)
    mask_red = cv2.bitwise_or(mask_red1, mask_red2)

    mask_green = cv2.inRange(hsv, green_lower, green_upper)
    mask_blue = cv2.inRange(hsv, blue_lower, blue_upper)

    # Find contours for each color independently
    for color, mask, lower, upper in [("red", mask_red, red_lower1, red_upper1), 
                                      ("green", mask_green, green_lower, green_upper),
                                      ("blue", mask_blue, blue_lower, blue_upper)]:
        cnts, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for c in cnts:
            area = cv2.contourArea(c)
            if area > 2000:  # Only consider large contours
                # Get contour center
                M = cv2.moments(c)
                if M["m00"] != 0:  # Avoid division by zero
                    cx = int(M["m10"] / M["m00"])
                    cy = int(M["m01"] / M["m00"])

                # Draw contours and color label
                cv2.drawContours(frame, [c], -1, (255, 0, 0), 3)  # Draw contour in blue
                cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)  # Draw center circle
                cv2.putText(frame, color, (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    res = cv2.bitwise_and(frame, frame, mask=mask_red)  # Show result with red mask

    cv2.imshow("live transmission", frame)
    cv2.imshow("res", res)
    key = cv2.waitKey(5)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
