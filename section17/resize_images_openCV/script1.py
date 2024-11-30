"""
import cv2

img = cv2.imread('galaxy.jpg', 0)

print(type(img))
print(img)
print(img.shape)
print(img.ndim)

resized_image = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))

cv2.imshow('Galaxy', resized_image)
cv2.imwrite('Galaxy_resized.jpg', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

import cv2

my_images = ['galaxy.jpg','kangaroos-rain-australia_71370_990x742.jpg','Lighthouse.jpg','Moon sinking, sun rising.jpg']
#print(type(my_images))
for image in my_images:
  images = cv2.imread(image, 0)

  resized_images = cv2.resize(images, (100, 100))
  titles = 'resized_'+image
  cv2.imwrite(titles, resized_images)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  #print(type(images))

"""
import cv2
import glob

images=glob.glob("*.jpg")

for image in images:
    img=cv2.imread(image,0)
    re=cv2.resize(img,(100,100))
    cv2.imshow("Hey",re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+image,re)
"""