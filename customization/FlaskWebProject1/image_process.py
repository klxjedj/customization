import functools
from datetime import datetime
from FlaskWebProject1.global_setting import *




from FlaskWebProject1.global_setting import *
import requests
from io import BytesIO
from PIL import Image

def parse_parameter(para):
    v,*color_pattern=para.split(',')
    print("parse:"+str(datetime.now()))
    return (v,color_pattern)

def generate_color_list(color_pattern):
    print("gene:"+str(datetime.now()))
    return [color_list[int(i)] for i in color_pattern]

def construct_urlpara(obj_list:list,color_list:list)->str:
    print("construct:"+str(datetime.now()))
    para=[para_pattern.format(obj=s,color=c)  for o,c in zip(obj_list,color_list) for s in o]
    return '&'.join(para)

def get_img(u):
    r=requests.get(u)
    print("get:"+str(datetime.now()))
    return r.content