# USAGE
# python color_kmeans.py --image images/jp.png --clusters 3
#https://www.pyimagesearch.com/2014/05/26/opencv-python-k-means-color-clustering/

# import the necessary packages
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
#import argparse
import utils
import cv2
import scipy.misc

def isNotWhatYouWant(ref_image, i):
    isNotBackground = (ref_image[i][0] == 0) and (ref_image[i][1] == 0) and (ref_image[i][2] == 0)
    isNotHat = (ref_image[i][0] == 0) and (ref_image[i][1] == 255) and (ref_image[i][2] == 255)
    isNotHair = (ref_image[i][0] == 255) and (ref_image[i][1] == 0) and (ref_image[i][2] == 255)
    isNotLArm = (ref_image[i][0] == 129) and (ref_image[i][1] == 255) and (ref_image[i][2] == 129)
    isNotRArm = (ref_image[i][0] == 0) and (ref_image[i][1] == 246) and (ref_image[i][2] == 82)
    isNotLLeg = (ref_image[i][0] == 255) and (ref_image[i][1] == 0) and (ref_image[i][2] == 85)
    isNotRLeg = (ref_image[i][0] == 255) and (ref_image[i][1] == 85) and (ref_image[i][2] == 85)
    isNotFace = (ref_image[i][0] == 255) and (ref_image[i][1] == 85) and (ref_image[i][2] == 170)
    isNotUnkown = (ref_image[i][0] == 0) and (ref_image[i][1] == 255) and (ref_image[i][2] == 85)

    # /f(isNotBackground or isNotHat or isNotHair or isNotLArm or isNotRArm or isNotLLeg or isNotRLeg or isNotFace):
    if(isNotBackground or isNotHat or isNotHair or isNotLArm or isNotRArm or isNotLLeg or isNotRLeg or isNotFace or isNotUnkown):
        return True
    else:
        return False

# construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required = True, help = "Path to the image")
# ap.add_argument("-c", "--clusters", required = True, type = int,
# 	help = "# of clusters")
# args = vars(ap.parse_args())

# load the image and convert it from BGR to RGB so that
# we can dispaly it with matplotlib
#image = cv2.imread(args["image"])

for a in range(8289, 8404):

    image = cv2.imread("./final2/" + str(a) + ".png")
    ref_image = cv2.imread("./images/" + str(a)+ "_fake_B.png")
    # image = cv2.imread("./RGB_TEST_2.png")
    ref_image = cv2.cvtColor(ref_image, cv2.COLOR_BGR2RGB)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # show our image
    # plt.figure()
    # plt.axis("off")
    # plt.imshow(image)

    image_temp = image
    reference_img_temp = ref_image

    # reshape the image to be a list of pixels
    ref_image_size = ref_image.shape[0] * ref_image.shape[1]
    ref_image = ref_image.reshape((ref_image.shape[0] * ref_image.shape[1], ref_image.shape[2]))

    image_size = image.shape[0] * image.shape[1]
    image = image.reshape((image.shape[0] * image.shape[1], image.shape[2]))

    # print(image)
    refined_image = []
    refined_image_for_colorchip= []

    for i in range(image_size):
        # image_pixel = [image[i][0], image[i][1], image[i][2]]
        if isNotWhatYouWant(ref_image, i):
            continue
        refined_image_for_colorchip += [[image[i][0], image[i][1], image[i][2]]]

     ###debug
        # isBack = (image[i][0] == 0) and (image[i][1] == 0) and (image[i][2] == 0)
        #
        # if(isBack):
        #     print(i//256, i % 256, reference_img_temp[i//256][i % 256][0],reference_img_temp[i//256][i % 256][1],reference_img_temp[i//256][i % 256][2])
        #     image_temp[i//256][i % 256][0] = 0
        #     image_temp[i//256][i % 256][1] = 255
        #     image_temp[i//256][i % 256][2] = 0
        # else:
        #     refined_image += [[image[i][0], image[i][1], image[i][2]]]

    # cluster the pixel intensities
    #clt = KMeans(n_clusters = args["clusters"])
    clt = KMeans(n_clusters = 4)
    #clt.fit(image)
    # print(image)
    clt.fit(refined_image_for_colorchip)

    # build a histogram of clusters and then create a figure
    # representing the number of pixels labeled to each color
    hist = utils.centroid_histogram(clt)
    bar = utils.plot_colors(hist, clt.cluster_centers_)
    #print(type(bar))
    scipy.misc.imsave('./color_chip/' + str(a) + '.png', bar)
    #print(a)


    # show our image
    # plt.figure()
    # plt.axis("off")
    # plt.imshow(image_temp)



    # show our color bart
    # plt.figure()
    # plt.axis("off")
    # plt.imshow(bar)
    # plt.show()

