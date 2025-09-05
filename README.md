# QR-code-scanner-
QR Code Scanner (Python + OpenCV)

A simple QR Code Scanner built with Python and OpenCV.
It captures video from your webcam, detects QR codes in real-time, and:

Draws bounding boxes around detected QR codes.

Displays the decoded text on screen.

If exactly one QR code contains a valid URL → opens it in your default web browser.

If multiple QR codes are detected → prints them to the terminal instead of auto-opening.

If the scanned code is not a URL → displays "Invalid URL".

Press q to quit.

📌 Features

✅ Real-time QR code scanning with your webcam.

✅ Clear green bounding box around each QR code.

✅ Text overlay above QR codes showing their decoded data.

✅ Automatic URL opening (only if exactly one QR code is found).

✅ Multiple QR codes → just prints results in terminal (no auto-opening).

✅ Invalid QR codes → marked on screen + printed in console.

✅ Simple exit by pressing q.

🛠️ Requirements

Make sure you have Python 3.7+ installed.

Install the required dependency:

pip install opencv-python


webbrowser and re are built-in Python modules (no installation needed).
numpy is automatically installed with OpenCV.

▶️ Usage

Run the script with:

python qr_scanner.py


A webcam window will open.

Point it at a QR code.

If one valid URL → it opens automatically in your browser.

If multiple codes → all are printed in the terminal, but none are opened automatically.

If not a URL → "Invalid URL" appears on screen + in the terminal.

Press q to quit.

📂 Modules Used

OpenCV (cv2)

For capturing webcam video, detecting QR codes, drawing bounding boxes, and displaying the video feed.

webbrowser
 (built-in)
To open valid QR code links in your system’s default browser.

re
 (built-in)
For validating whether the decoded QR code text is a proper URL using regular expressions.

numpy
 (indirectly via OpenCV)
Used internally by OpenCV to handle images as arrays and bounding box coordinates.

📸 Example Behavior

One QR code detected → Decoded text shown, URL opens automatically if valid.

Multiple QR codes detected → All results printed in terminal, none auto-opened.

Invalid QR code (non-URL) → Shows "Invalid URL" above the code and logs in terminal.

🚀 Future Improvements

Manual control to choose which QR code to open (e.g., press Enter on a selected one).

Sound feedback (beep) when a QR code is detected.

Save scan history (with timestamps) to a scans.txt file.

Support scanning directly from images (not just webcam).

📜 License

This project is open-source and free to use for learning or personal projects.
