import numpy as np
import cv2


def convert_to_YUV(photo):

    data = cv2.imread(photo)

    # RGB TP YUV transformatiom matrix:
    #YUV_transform = np.array(([0.299, 0.587, 0.144], [-0.299, -0.587, 0.886], [0.701, -0.587, -0.114])).T
    YUV_transform = np.array(([0.299, 0.587, 0.144], [-0.14713, -0.2886, 0.436], [0.615, -0.51499, -0.10001])).T

    # matrix multiplication - Conversion from RGB to YUV
    photo_YUV = data @ YUV_transform

    # Add 128 to U & V channels
    photo_YUV[:, :, 1:] += 128.0

    # clip the pixel values to be in 0-255 range
    photo_YUV = np.clip(photo_YUV, 0, 255)

    # Change to uint8
    photo_2d = photo_YUV.astype('uint8')

    return photo_2d


if __name__ == "__main__":

    ######  Show original photo  ##########
    img = cv2.imread('test1.jpg')
    cv2.imshow('YUV_CV2', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    ######  Show CV2 conversion BGR to YUV  ##########
    img_YUV = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
    cv2.imshow('YUV_CV2', img_YUV)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    ######  Show CV2 conversion BGR to Y  ##########
    y, u, v = cv2.split(img_YUV)
    cv2.imshow('Y_CV2', y)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    ##### Convert using my function  ##############
    photo_YUV = convert_to_YUV('test1.jpg')

    #####  Display YUV of my function ###############
    cv2.imshow('MY_photo_YUV', photo_YUV)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #####  Display Y of my function ###############
    y, u, v = cv2.split(photo_YUV)
    cv2.imshow('MY_Func_Y', np.array(y))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
###################################3








