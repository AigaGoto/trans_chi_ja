import pandas as pd
from googletrans import Translator
translator = Translator()
data=pd.read_csv('train_jp0.csv')
japan_list=[]

chinese_list = data['review']

# print(chinese_list[0])

# dec_lan = translator.detect(chinese_list[0])

# dst = translator.translate("english", src='ja', dest='en')

# print(dst.text)
# print(translator.translate("日本語", src='ja', dest='en').text)

# print(dec_lan)

for i in chinese_list:
    dst = translator.translate(i, src='zh-cn', dest='ja')
    japan_list.append(dst.text)
    print(dst.text)

data['Japanese']=japan_list
data.to_csv("result.csv",encoding='utf_8_sig' ,index=False)