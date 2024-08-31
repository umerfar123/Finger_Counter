# Finger Counting Application Using OpenCV

<img align="center" alt="Coding" width="100%" height='200px' src="fc.jfif">

## Introduction

This application uses OpenCV and MediaPipe to see your hand and count how many fingers are up. It draws lines to show where your fingers are and uses the position of your fingertips to figure out the count. For explained working of the system see [explanation](https://github.com/umerfar123/um_hand_digit_counter/blob/main/explanation.md) file.

## Usage

1. Open downloaded folder in vscode or any IDE.
2. Install the required libraries using following python command on IDE terminal:
   
   ```python
     pip install -r requirements.txt
   ```
3. If you are using external video capture device rather than default video capture device then you should change a parameter value in main.py file in ${\color{red}line 18}$.

   ```python
    cap=cv2.VideoCapture(param)
   ```
   +  If you are using default webcam set param=0.
   +  Set param = 1, 2, 3, ... These numbers represent additional video capture devices connected to your system. If you have multiple cameras, you can use these values to select a specific one.   

   
5. Run the main.py file.

   ```python
     python main.py
   ```
___
 > [!NOTE]
 > According to your system it will take time to load a window where you can see the feed from your video capture device.
