def get_rgb_rsv(s): 
    #importing libraries
    import cv2
    import numpy as np
    from sklearn.cluster import KMeans
    from collections import Counter    
    from urllib.request import urlopen


    req = urlopen(s)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    img = cv2.imdecode(arr, -1)

    image = img
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(image, 10, 250)
    (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    idx = 0
    for c in cnts:
        x,y,w,h = cv2.boundingRect(c)
        if w>300 and h>700:
            idx+=1
            new_img=image[y:y+h,x:x+w]
            cv2.imwrite(str(idx) + '.png', new_img)
            img = new_img
    

    #img = cv2.resize(image, (330, 775), interpolation = cv2.INTER_AREA)
    def white_balance(img):
        result = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        avg_a = np.average(result[:, :, 1])
        avg_b = np.average(result[:, :, 2])
        result[:, :, 1] = result[:, :, 1] - ((avg_a - 128) * (result[:, :, 0] / 255.0) * 1.1)
        result[:, :, 2] = result[:, :, 2] - ((avg_b - 128) * (result[:, :, 0] / 255.0) * 1.1)
        result = cv2.cvtColor(result, cv2.COLOR_LAB2BGR)
        return result
    img = np.hstack((img, white_balance(img)))
        
    #fields' coordinates
    rects = [
        [65, 135, 115, 185],
        [220, 135, 270, 185],
        [65, 210, 115, 260],
        [220, 210, 270, 260],
        [65, 325, 115, 375],
        [220, 325, 270, 375],
        [65, 445, 115, 495],
        [220, 445, 270, 495],
        [65, 560, 115, 610],
        [220, 560, 270, 610],
        [65, 675, 115, 725],
        [220, 675, 270, 725]
    ]

    #creating block from coordinates
    c = 1
    for i in rects:
        imageSample = img[i[1]:i[3], i[0]:i[2]]
        name = "image" + str(c) + ".png"
        cv2.imwrite(name, imageSample)
        c += 1

    #getting dominant color
    def get_dominant_color(image, k=10):

        #reshape the image to be a list of pixels
        image = image.reshape((image.shape[0] * image.shape[1], 3))

        #cluster and assign labels to the pixels 
        clt = KMeans(n_clusters = k)
        labels = clt.fit_predict(image)

        #count labels to find most popular
        label_counts = Counter(labels)

        #subset out most popular centroid
        dominant_color = clt.cluster_centers_[label_counts.most_common(1)[0][0]]

        return list(dominant_color)

    #finding dom color for each block
    dominant_colors = []
    for i in range(1, 11):
        part_img = cv2.imread('image' + str(i) + '.png', cv2.IMREAD_COLOR)
        part_img = cv2.cvtColor(part_img, cv2.COLOR_BGR2RGB)
        dom_col = get_dominant_color(part_img, k=1)  
        dominant_colors.append([int(x) for x in dom_col])

    #string repr of rgb
    rgb = []
    for i in dominant_colors:
        rgb.append('rgb('+ ', '.join([str(x) for x in i]) + ')')

    #converting rgb to hsv function
    def rgb_to_hsv(r, g, b):
        r, g, b = r/255.0, g/255.0, b/255.0
        mx = max(r, g, b)
        mn = min(r, g, b)
        df = mx-mn
        if mx == mn:
            h = 0
        elif mx == r:
            h = (60 * ((g-b)/df) + 360) % 360
        elif mx == g:
            h = (60 * ((b-r)/df) + 120) % 360
        elif mx == b:
            h = (60 * ((r-g)/df) + 240) % 360
        if mx == 0:
            s = 0
        else:
            s = (df/mx)*100
        v = mx*100
        return h, s, v

    #function call
    hsv_colors = [rgb_to_hsv(i[0], i[1], i[2]) for i in dominant_colors]

    #int values of hsv
    hsv = []
    for i in hsv_colors:
        hsv.append([int(x) for x in i])
    return [rgb, hsv]



