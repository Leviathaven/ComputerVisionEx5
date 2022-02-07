import cv2

haar_cascade = 'haarcascade_frontalface_default.xml'
image_name = '4.jpg'

def haar(image,
         scale_factor=1.1,
         min_neighbors=5,
         min_size=(10, 10)):
  cascade = cv2.CascadeClassifier(r'C:/Users/Raven/PycharmProjects/OpenCV/venv/Lib/site-packages/cv2/data/' + haar_cascade)

  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  detected = cascade.detectMultiScale(
      gray,
      scaleFactor=scale_factor,
      minNeighbors=min_neighbors,
      minSize=min_size)
  print('Обнаружено :', str(len(detected)))
  for (x, y, w, h) in detected:
      cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
  cv2.imwrite('photos5/haar_' +
              str(scale_factor) + '_' +
              str(min_neighbors) + '_' +
              str(min_size) + '_' + image_name, image)


image = cv2.imread('photos5/' + image_name)
haar(image, scale_factor=1.1, min_neighbors=1, min_size=(2, 2))