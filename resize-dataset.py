import cv2
import glob

img_list = glob.glob("laser-scan/real-scans-v1/*.png")

for i,img_path in enumerate(img_list):
    img = cv2.imread(img_path)
    height, width, _ = img.shape
    img = img[:, width-height:width, :]
    print(img.shape)
    img = cv2.resize(img, (500,500))


    cv2.imwrite("laser-scan/real-scans-v1-resized/img"+('%03d' % i)+".png", img)




