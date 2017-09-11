import functools
from FlaskWebProject1.global_setting import *




from FlaskWebProject1.global_setting import *

def parse_parameter(para):
    v,*color_pattern=para.split(',')
    return (v,color_pattern)

def generate_color_list(color_pattern):
    return [color_list[int(i)] for i in color_pattern]

def construct_urlpara(obj_list:list,color_list:list)->str:
    print(obj_list)
    para=[para_pattern.format(obj=s,color=c)  for o,c in zip(obj_list,color_list) for s in o]
    return '&'.join(para)

def get_img(u):
    r=requests.get(u)
    print(r.content)
    print(r.status_code)
    s=BytesIO()
    s.write(r.content)
    img=Image.open(s)
    img.show()
    return img