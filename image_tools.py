import PIL
import base64
import io
from PIL import Image
import cv2
import numpy



class ImageTools(object):
    '''
    图片工具类，用于处理图片转换成
    '''

    def __cv2_to_base64(self, image):
        return base64.b64encode(image.tobytes())

    def __base64_to_cv2(self, image):
        return numpy.frombuffer(base64.b64decode(image), dtype=numpy.uint8)

    def __pil_to_cv2(self, image):
        return numpy.asarray(image)

    def __cv2_to_pil(self, image):
        return Image.fromarray(image)

    def __bytes_to_pil(self, image):
        image_data = io.BytesIO(image)
        image= Image.open(image_data)
        return image

    def __pil_to_bytes(self, image):
        img_byte = io.BytesIO()
        image.save(img_byte, format='PNG')
        image = img_byte.getvalue()
        return image

    def __cv2_to_bytes(self, image):
        return image.tobytes()

    def __bytes_to_cv2(self, image):
        return numpy.frombuffer(image, dtype=numpy.uint8)

    def __base64_to_bytes(self, image):
        return base64.b64decode(image)

    def __bytes_to_base64(self, image):
        return base64.b64encode(image)

    def __pil_to_base64(self, image):
        img_byte = io.BytesIO()
        image.save(img_byte, format='PNG')
        image= img_byte.getvalue()
        return base64.b64encode(image)



    def isBase64(self, s):
        try:
            return base64.b64encode(base64.b64decode(s)) == s
        except Exception:
            return False

    def __base64_to_pil(self, image):
        return Image.fromarray(self.__bytes_to_cv2(self.__base64_to_bytes(image)))


    def image_to_base64(self, image):
        """
        将image对象转换为base64对象
        :param image: 可以是numpy数组、pil图片对象、图片的base64对象、图片的bytes形式
        :return:base64对象
        """
        if isinstance(image, (PIL.Image.Image)):
            return self.__pil_to_base64(image)
        elif isinstance(image, (numpy.ndarray,)):
            return self.__cv2_to_base64(image)
        elif self.isBase64(image):
            return image
        elif isinstance(image, (bytes,)):
            return self.__bytes_to_base64(image)
        else:
            raise TypeError('input obj err! please check!')

    def image_to_bytes(self, image):
        """
        将image对象转换为bytes对象
        :param image: 可以是numpy数组、pil图片对象、图片的base64对象、图片的bytes形式
        :return:PIl对象
        """
        if isinstance(image, (numpy.ndarray,)):
            return self.__cv2_to_bytes(image)
        elif isinstance(image, (PIL.Image.Image)):
            return self.__pil_to_bytes(image)
        elif self.isBase64(image):
            return self.__base64_to_bytes(image)
        elif isinstance(image, (bytes,)):
            return image
        else:
            raise TypeError('input obj err! please check!')

    def image_to_array(self, image):
        """
        将image对象转换为cv对象（numpy数组）
        :param image: 可以是numpy数组、pil图片对象、图片的base64对象、图片的bytes形式
        :return:numpy数组
        """
        if isinstance(image, (PIL.Image.Image)):
            return self.__pil_to_cv2(image)
        elif self.isBase64(image):
            return self.__base64_to_cv2(image)
        elif isinstance(image, (bytes,)):
            return self.__bytes_to_cv2(image)
        elif isinstance(image, (numpy.ndarray,)):
            return image
        else:
            raise TypeError('input obj err! please check!')

    def image_to_pillowobj(self,image):
        """
        将image对象转换为PIL对象
        :param image: 可以是numpy数组、pil图片对象、图片的base64对象、图片的bytes形式
        :return:PIL对象
        """
        if self.isBase64(image):
            return self.__base64_to_pil(image)
        elif isinstance(image, (bytes,)):
            return self.__bytes_to_cv2(image)
        elif isinstance(image, (numpy.ndarray,)):
            return self.__cv2_to_pil(image)
        elif isinstance(image, (PIL.Image.Image)):
            return image
        else:
            raise TypeError('input obj err! please check!')





if __name__ == '__main__':
    image = r'test.png'
    s = ImageTools()
    img =  Image.open(image)
    img = s.image_to_base64(img)
    # cv2.imshow(img)
    # print(img)
    print(type(img))
    data0 = s.image_to_array(img)


    data = s.image_to_bytes(data0)
    print(s.isBase64(data))
    print(type(data))
    data = s.image_to_base64(data)

    data1 = s.image_to_array(data)

    if data0.any() == data1.any():
        print('数据吻合')


    print(s.isBase64(data))
    print(type(data))



