# img_type_trans
实现python的base64、PIL、array、bytes四种图片对象自由转换


    image = r'./test.png'
    img = ImageObj(image)
    img0 = img.to_base64().image
    img = img.to_bytes().to_array().to_pillowobj().to_array().to_pillowobj().to_bytes().to_pillowobj().to_base64().image
    if img0 == img:
        print('数据吻合')

    image = r'./test.png'
    image = cv2.imread(image)
    img = ImageObj(image)
    img0 = img.to_base64().image
    img = img.to_bytes().to_array().to_pillowobj().to_array().to_pillowobj().to_bytes().to_pillowobj().to_base64().image
    if img0 == img:
        print('数据吻合')

    img = ImageObj(r'./test.png')
    img0 = img.to_base64().image
    img = img.to_bytes().to_array().to_pillowobj().to_array().to_pillowobj().to_bytes().to_pillowobj().to_base64().image
    if img0 == img:
        print('数据吻合')

    image = r'./test.png'
    image = open(image, 'rb').read()
    img = ImageObj(image)
    img0 = img.to_base64().image
    img = img.to_bytes().to_array().to_pillowobj().to_array().to_pillowobj().to_bytes().to_pillowobj().to_base64().image
    if img0 == img:
        print('数据吻合')

    image = r'./test.png'
    image = base64.b64encode(open(image, 'rb').read())
    img = ImageObj(image)
    img0 = img.to_base64().image
    img = img.to_bytes().to_array().to_pillowobj().to_array().to_pillowobj().to_bytes().to_pillowobj().to_base64().image
    if img0 == img:
        print('数据吻合')
