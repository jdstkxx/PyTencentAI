# -*- coding: utf-8 -*-

'''
create by : joshua zou
create date : 2017.11.28
Purpose: check tecent ai api
'''


from TencentAPI import * 
from TencentAPIMsg import *

#通用api构造函数
def ExecTecentAPI(*arg,**kwds):
    if kwds.get('Apiname'): apiname= kwds.pop('Apiname')
    
    url = TencentAPI[apiname]['APIURL']
    name = TencentAPI[apiname]['APINAME']
    desc= TencentAPI[apiname]['APIDESC']
    para= TencentAPI[apiname]['APIPARA']
    
    tx= TencentAPIMsg(APPID,APPKEY)

    Req_Dict={}
    for key in para.split(','):
        value=None
        #print (kwds)
        if kwds.get(key):  value = kwds.pop(key)
        if key=='image': 
            #图像获取base64
            value= tx.get_img_base64str(value)
        if key=='text':
            #文本进行GBK编码
            value= value.encode('gbk')
       
        Req_Dict[key]=value        
        #print (key,value,Req_Dict[key])
        
    #生成请求包
    sign= tx.init_req_dict(req_dict=Req_Dict)
    resp = requests.post(url,data=Req_Dict)
    print (name+',API应答码:'+str(resp.json()['ret']))
    text = ''
    try :
        for each in resp.json()['data']['item_list']:
            text = text+'/'+ each['itemstring']
    except :
        text = ''
    return  text 
    
'''
基本文本分析
===========
分词 	对文本进行智能分词识别，支持基础词与混排词粒度 	https://api.ai.qq.com/fcgi-bin/nlp/nlp_wordseg text
词性标注 	对文本进行分词，同时为每个分词标注正确的词性 	https://api.ai.qq.com/fcgi-bin/nlp/nlp_wordpos text
专有名词识别 	对文本进行专有名词的分词识别，找出文本中的专有名词 	https://api.ai.qq.com/fcgi-bin/nlp/nlp_wordner text
同义词识别 	识别文本中存在同义词的分词，并返回相应的同义词 	https://api.ai.qq.com/fcgi-bin/nlp/nlp_wordsyn text


计算机视觉--OCR识别
====================
通用OCR识别 	识别上传图像上面的字段信息 	https://api.ai.qq.com/fcgi-bin/ocr/ocr_generalocr image
身份证OCR识别 	识别身份证图像上面的详细身份信息 	https://api.ai.qq.com/fcgi-bin/ocr/ocr_idcardocr image,card_type(身份证，0-正面，1-反面)
名片OCR识别 	识别名片图像上面的字段信息 	https://api.ai.qq.com/fcgi-bin/ocr/ocr_bcocr image
行驶证驾驶证OCR识别 	识别行驶证或驾驶证图像上面的字段信息 	https://api.ai.qq.com/fcgi-bin/ocr/ocr_driverlicenseocr image,type(识别类型，0-行驶证识别，1-驾驶证识别)
营业执照OCR识别 	识别营业执照上面的字段信息 	https://api.ai.qq.com/fcgi-bin/ocr/ocr_bizlicenseocr image
银行卡OCR识别 	识别银行卡上面的字段信息 	https://api.ai.qq.com/fcgi-bin/ocr/ocr_creditcardocr image
'''
#改成你自己腾讯APPID及APPKEY
APPID='100000000'
APPKEY='ZV1w000000'

if __name__ == "__main__":
    for file in glob.glob('D:\python\guoyaotang\*.jpg'):
        rest = ExecTecentAPI(Apiname='ocr_generalocr',image=file)
        print (file+rest)