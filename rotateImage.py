image = [[1, 2, 3, 10], [4, 5, 6, 11], [7, 8, 9, 12], [13, 14, 15, 16]]


def rotate(img):

    for i in range(len(img)):
        for j in range(i, len(img)):
            img[i][j], img[j][i] = img[j][i], img[i][j]
    for i in range(len(img)):
        for j in range(int(len(img)/2)):
            img[i][j], img[i][len(img)-1-j] = img[i][len(img)-1-j], img[i][j]

    return img


print(rotate(image))
