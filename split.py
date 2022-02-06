import cv2
vidcap = cv2.VideoCapture('pokpo1.mov')
success,image = vidcap.read()
count = 0
frames = []
while success:
  frames.append(image)
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1
dst = frames[0]

for i in range(1, len(frames), 1):
    print('frame%d.jpg' % i)
    img = frames[i]
    dst = cv2.addWeighted(dst, 0.95, img, 0.05, 0)
cv2.imshow("result", dst)
cv2.waitKey(0)











