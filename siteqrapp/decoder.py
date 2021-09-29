import base64
import json
import io
import cv2
import barcode
import pyzbar.pyzbar as pyzbar
from PIL import Image
from numpy.distutils.fcompiler import none

import requests
from requests_ntlm import HttpNtlmAuth

import re
from .getdataapi import getjs


def get_js(sc, shop):
    username = r'WebService'
    password = 'web2018'
    auth = HttpNtlmAuth(username, password)
    strParam = shop + '/' + sc
    list_url = r"https://ts.offprice.eu/service_retail/hs/wms_api/getpriceQR/" + strParam
    headers = {'Accept': 'application/json;odata=verbose'}
    responce = requests.get(list_url, verify=False, auth=auth, headers=headers)
    response_json = responce.json()
    return response_json


def draw_barcode(decoded, my_image):
    # # n_points = len(decoded.polygon)
    # # for i in range(n_points):
    # #     my_image = cv2.line(my_image, decoded.polygon[i], decoded.polygon[(i+1) % n_points], color=(0, 255, 0), thickness=5)
    # my_image = cv2.rectangle(my_image, (decoded.rect.left, decoded.rect.top),
    #                         (decoded.rect.left + decoded.rect.width, decoded.rect.top + decoded.rect.height),
    #                          color=(0, 255, 0),
    #                          thickness=5)
    return my_image


def decode_barcode(my_image):
    # decodes all barcodes from an my_image
    bar_class = barcode.ean.EAN13.name
    decoded_objects = pyzbar.decode(Image.open(my_image))
    # print(decoded_objects)
    for obj in decoded_objects:
        # draw the barcode
        # if obj.type == bar_class.replace("-", ""):
            # my_image = draw_barcode(obj, my_image)
            # print barcode type & data
            # print("Type:", obj.type)
        # print("Data:", obj.data.decode("utf-8"))
        return obj.data.decode("utf-8")
    return 0


def read_barcode(my_image):
    decoded_objects = decode_barcode(my_image)
    # print(decoded_objects.data)
    my_image = draw_barcode(decoded_objects, my_image)
    return my_image
    # my_image,
    # show the my_image in the window
    # cv2.imshow("my_image", my_image)
    # cv2.waitKey(0)
    # if cv2.waitKey(1) == ord("q"):
    #     break


def use_barcode(my_image):
    decoded_objects = decode_barcode(my_image)
    return decoded_objects


def use_barcode_ajax(my_image):
    decoded_objects = decode_barcode(my_image)
    return decoded_objects


def get_my_code_test():
    # base64.encode()
    shop = '008'
    myimg = ('static/img/05.jpg')
    image_barcode = cv2.imread(myimg)
    #newbar = read_barcode(image_barcode)
    # textbar = use_barcode(image_barcode)
    textbar = '2009886188657'
    textjson = get_js(textbar, shop)

    # get string with all double quotes
    single_quoted_dict_in_string = textjson
    desired_double_quoted_dict = str(single_quoted_dict_in_string)
    desired_double_quoted_dict = desired_double_quoted_dict.replace("'", "\"")
    return desired_double_quoted_dict
    #print(textjson)



# def get_my_code(image_base64, shop):

def get_my_code(image_base64, shop):
    # print(param)
    # image_base64 = param['photo']
    # shop = param['shop']

    # shop = '011'
    # Тест
    # img = ('static/img/222.jpg')
    # image_read = Image.open(img)
    # image_base64 = base64.b64encode(image_read)
    # print(image_base64)

    # Рабочий
    imgdata = base64.b64decode(str(image_base64))
    tempimg = io.BytesIO(imgdata)

    print(shop)
    datasacan = use_barcode(tempimg)
    if datasacan == 0:
        return 0
    textbar = datasacan
    # textbar = '2009886276002'

    textjson = getjs(textbar, shop)
    # print(textjson)
    # Надо чтобы возвращал штрихкод, если не удалось получить по нему данные
    if textjson == '[] []':
        return 1
    # get string with all double quotes
    single_quoted_dict_in_string = textjson
    desired_double_quoted_dict = str(single_quoted_dict_in_string)
    desired_double_quoted_dict = desired_double_quoted_dict.replace("'", "\"")
    return desired_double_quoted_dict
    #print(desired_double_quoted_dict)


