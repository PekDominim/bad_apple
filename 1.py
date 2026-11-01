import cv2
import climage
import time
import os
import io

video_path = "Bad Apple!! - Full Version w⧸video [Lyrics in Romaji, Translation in English] [9lNZ_Rnr7Jc].mp4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error opening video file")
else:
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"Total number of frames: {total_frames}")

image_stream = io.BytesIO()
current_frame=0
print("\033[?25l", end="")
os.system('cls' if os.name == 'nt' else 'clear')

while current_frame!=7777:


        success, frame = cap.read()
        success, encoded_image = cv2.imencode('.jpg', frame)
        image_stream = io.BytesIO(encoded_image.tobytes())
        output = climage.convert(image_stream, is_unicode=True)
        print("\033[1;1H", end="")
        print(output, end="")
        time.sleep(0.016)
        current_frame+=1

print("\033[?25h", end="")
cap.release()
