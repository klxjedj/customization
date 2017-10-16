image_path = r'FlaskWebProject1/static/images/'

parameter = '1,2,3,4,5,7,8,9,8,2,1,3,7,6'

img_url = r'https://render.nikeid.com/ir/render/nikeidrender/am90OGess1701_v{view}?obj=/s/shadow/shad&show&color=000000&{para}&obj=/s&req=object&fmt=png-alpha&wid=640'

para_pattern='obj={obj}&color={color}&show'

element=['鞋面',
         '覆面',
         '挡泥板',
         '标识',
         '鞋眼片',
         '鞋面鞋眼',
         '鞋跟主色',
         '鞋带',
         '内衬',
         '中底',
         '中底中板',
         '气垫',
         '外底',
         ]

img_list={
    '鞋面':'1.png',
         '覆面':'2.png',
         '挡泥板':'3.png',
         '标识':'4.png',
         '鞋眼片':'5.png',
         '鞋面鞋眼':'6.png',
         '鞋跟主色':'7.png',
         '鞋带':'8.png',
         '内衬':'9.png',
         '中底':'10.png',
         '中底中板':'11.png',
         '气垫':'12.png',
         '外底':'13.png',
    }

obj_list=[
    ['/s/g1','/s/g2'],
    ['/s/g6','/s/g7'],
    ['/s/g8'],
    ['/s/g9'],
    ['/s/g5','/s/g13','/s/g14'],
    ['/s/g12'],
    ['/s/g17'],
    ['/s/g10'],
    ['/s/g15'],
    ['/s/g18'],
    ['/s/g21'],
    ['/s/g22'],
    ['/s/g24']
    ]

color_list=[
    '0abcd0',
    'ab00c0', 
    '183905',
    '201924', 
    '312345', 
    '917019', 
    '673203', 
    '720194', 
    '013937', 
    '719293', 
    '102849', 
    '756921', 
    '019374']