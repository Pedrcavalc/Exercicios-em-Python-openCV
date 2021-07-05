import cv2

image = cv2.imread('image.jpg')
grayscale = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

borda = cv2.Canny(grayscale, 80, 180)


params = cv2.SimpleBlobDetector_Params()
params.filterByArea = True
params.minArea = 20
params.maxArea = 40000

params.filterByCircularity = False
params.minCircularity = 0.1

params.filterByConvexity = False
params.minConvexity = 0.87

params.filterByInertia = False
params.minInertiaRatio = 0.8

params.minDistBetweenBlobs = 20

detector = cv2.SimpleBlobDetector_create(params)
blobs = detector.detect(borda)

print(len(blobs))
cv2.imshow('grayscale', grayscale)
cv2.waitKey(0)