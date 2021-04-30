import os
import PIL
import base64
import io
from PIL import Image
import cv2
import numpy



class ImageObj(object):
    '''
    图片工具类，用于处理图片转换成
    '''
    def __init__(self, image):
        if isinstance(image, str):
            if os.path.isfile(image):
                self.image = open(image, 'rb').read()
            else:
                raise TypeError('No such path!')
        elif isinstance(image, (PIL.Image.Image)):
            self.image = image
        elif isinstance(image, (numpy.ndarray,)):
            self.image = image
        elif self.isBase64(image):
            self.image = image
        elif isinstance(image, (bytes,)):
            self.image = image
        else:
            raise TypeError('input obj err! please check!')

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
        return self.__pil_to_cv2(image).tobytes()

    def __cv2_to_bytes(self, image):
        return image.tobytes()

    def __bytes_to_cv2(self, image):
        return numpy.frombuffer(image, dtype=numpy.uint8)

    def __base64_to_bytes(self, image):
        return base64.b64decode(image)

    def __bytes_to_base64(self, image):
        return base64.b64encode(image)

    def __pil_to_base64(self, image):
        return base64.b64encode(self.__pil_to_cv2(image).tobytes())



    def isBase64(self, s):
        try:
            return (base64.b64encode(base64.b64decode(s,validate=True)) == s)
            # if base64.b64encode(base64.b64decode(s)) == s:
            #     return True
            # return False
        except Exception:
            return False

    def __base64_to_pil(self, image):
        return Image.fromarray(self.__bytes_to_cv2(self.__base64_to_bytes(image)))


    def to_base64(self):
        """
        将image对象转换为base64对象
        :param image: 可以是numpy数组、pil图片对象、图片的base64对象、图片的bytes形式
        :return:base64对象
        """
        if isinstance(self.image, (PIL.Image.Image)):
            self.image = self.__pil_to_base64(self.image)
        elif isinstance(self.image, (numpy.ndarray,)):
            self.image = self.__cv2_to_base64(self.image)
        elif self.isBase64(self.image):
            ...
        elif isinstance(self.image, (bytes,)):
            self.image = self.__bytes_to_base64(self.image)
        return self

    def to_bytes(self):
        """
        将image对象转换为bytes对象
        :param image: 可以是numpy数组、pil图片对象、图片的base64对象、图片的bytes形式
        :return:PIl对象
        """
        if isinstance(self.image, (numpy.ndarray,)):
            self.image = self.__cv2_to_bytes(self.image)
        elif isinstance(self.image, (PIL.Image.Image)):
            self.image = self.__pil_to_bytes(self.image)
        elif self.isBase64(self.image):
            self.image = self.__base64_to_bytes(self.image)
        elif isinstance(self.image, (bytes,)):
            pass
        return self

    def to_array(self):
        """
        将image对象转换为cv对象（numpy数组）
        :param image: 可以是numpy数组、pil图片对象、图片的base64对象、图片的bytes形式
        :return:numpy数组
        """
        if isinstance(self.image, (PIL.Image.Image)):
            self.image = self.__pil_to_cv2(self.image)
        elif self.isBase64(self.image):
            self.image = self.__base64_to_cv2(self.image)
        elif isinstance(self.image, (bytes,)):
            self.image = self.__bytes_to_cv2(self.image)
        elif isinstance(self.image, (numpy.ndarray,)):
            pass
        return self

    def to_pillowobj(self):
        """
        将image对象转换为PIL对象
        :param image: 可以是numpy数组、pil图片对象、图片的base64对象、图片的bytes形式
        :return:PIL对象
        """
        if self.isBase64(self.image):
            self.image =  self.__base64_to_pil(self.image)
        elif isinstance(self.image, (bytes,)):
            self.image = self.__bytes_to_cv2(self.image)
        elif isinstance(self.image, (numpy.ndarray,)):
            self.image = self.__cv2_to_pil(self.image)
        elif isinstance(self.image, (PIL.Image.Image)):
            pass
        return self


if __name__ == '__main__':
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








