# img_type_trans
实现python的base64、PIL、array、bytes四种图片对象自由转换



image = r'test.png'
    
s = ImageTools()

img =  Image.open(image)
    
img = s.image_to_base64(img)

data0 = s.image_to_array(img)

data = s.image_to_bytes(data0)

data = s.image_to_pillowobj(data)

data1 = s.image_to_array(data)

if data0.any() == data1.any():

print('数据吻合')
