"""
Routes and views for the flask application.
"""

from flask import render_template,Response,redirect,url_for
from FlaskWebProject1 import app
from FlaskWebProject1.image_process import *
from FlaskWebProject1.global_setting import *

@app.route('/')
def main():
    #return redirect(url_for('img',parameter=parameter))
    return render_template('design.html',color_list=color_list,ele_list=element,img_list=img_list)

@app.route('/<parameter>')
def img(parameter):
    v,color_pattern=parse_parameter(parameter)
    color_list=generate_color_list(color_pattern)
    para=construct_urlpara(obj_list,color_list)
    u=img_url.format(view=v,para=para)
    img=get_img(u)
    return Response(img,mimetype='image/png')

@app.route('/favicon.ico')
def f():
    return ''