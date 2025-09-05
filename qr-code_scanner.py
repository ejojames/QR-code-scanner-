"""
QR Code Scanner with OpenCV
---------------------------
- Opens your webcam and looks for QR codes in real-time
- Draws a green bounding box around detected QR codes
- Shows the decoded text on screen
- If exactly one QR code contains a valid URL, it opens in your browser
- If multiple QR codes are detected, only prints them in the terminal
- If not a URL, it says "Invalid URL"
- Press 'q' to quit
"""

import cv2
import webbrowser
import re

def is_url(text: str) -> bool:
    """Check if the text looks like a valid URL using regex."""
    url_pattern = re.compile(
        r'^(https?://)?'       # optional http or https
        r'([a-zA-Z0-9.-]+)'    # domain name
        r'(\.[a-zA-Z]{2,})'    # top-level domain (.com, .org, etc.)
        r'(/.*)?$'             # optional path
    )
    return bool(url_pattern.match(text))

def qr_code_scanner():
    cap = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()
    last_data = None

    print("QR Code Scanner started. Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Could not access webcam.")
            break

        # Detect multiple QR codes
        retval, decoded_info, points, _ = detector.detectAndDecodeMulti(frame)

        if points is not None:
            for qr_data, qr_points in zip(decoded_info, points):
                if qr_data:
                    # Convert coordinates to int
                    qr_points = qr_points.astype(int)
                    num_points = len(qr_points)

                    # Draw bounding box
                    for i in range(num_points):
                        pt1 = tuple(qr_points[i])
                        pt2 = tuple(qr_points[(i + 1) % num_points])
                        cv2.line(frame, pt1, pt2, (0, 255, 0), 3)

                    # Show decoded text above QR
                    cv2.putText(frame, qr_data, (qr_points[0][0], qr_points[0][1] - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

            # Handle decoded results
            decoded_info = [d for d in decoded_info if d]  # filter empty results
            if decoded_info:
                if len(decoded_info) == 1:
                    data = decoded_info[0]
                    if data != last_data:
                        last_data = data
                        print(f"QR Code detected: {data}")
                        if is_url(data):
                            if not data.startswith("http"):
                                data = "http://" + data
                            print(f"Opening URL: {data}")
                            webbrowser.open(data)
                        else:
                            print(f"Invalid URL: {data}")
                else:
                    print("Multiple QR codes detected:")
                    for d in decoded_info:
                        print(" -", d)

        cv2.imshow("QR Code Scanner", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            print("Exiting QR Code Scanner.")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    qr_code_scanner()
