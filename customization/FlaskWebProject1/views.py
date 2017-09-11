"""
Routes and views for the flask application.
"""

from flask import render_template,Response,redirect,url_for
from FlaskWebProject1 import app
from FlaskWebProject1.image_process import *
from FlaskWebProject1.global_setting import *


@app.route('/')
def home():
    v,color_pattern=parse_parameter(parameter)
    color_list=generate_color_list(color_pattern)
    para=construct_urlpara(obj_list,color_list)
    u=img_url.format(view=v,para=para)
    return render_template('img.html',u=u)