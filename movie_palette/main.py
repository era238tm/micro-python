import numpy as np
import cv2


def movie_palette(video_path, image_path, sample_rate):
    cap = cv2.VideoCapture(video_path)

    success = cap.grab()
    fno = 0

    colors = []

    while success:
        if fno % sample_rate == 0:
            _, img = cap.retrieve()
            colors.append(np.round(np.average(img, axis=(0, 1))))

        success = cap.grab()
        fno += 1

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    image = np.tile(colors, (len(colors) * height // width, 1, 1))

    cv2.imwrite(image_path, image)


if __name__ == "__main__":
    movie_palette('costa_rica.mp4', 'costa_rica.png', 4)
