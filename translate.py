import pandas as pd
from googletrans import Translator
translator = Translator()
data=pd.read_csv('train_jp0.csv')
japan_list=[]

chinese = "状元楼饭店第一次去，因为地理位置优越：在宁波市和义大道高、大、上，里面装修中式，菜是地道的宁波菜，口味纯正，醉泥螺特棒，吃到了小时候的味道，因为去了晚了，在大堂等了一会儿，期间有茶水喝、服务员还与你聊天，到了就餐时生意太好，服务员都是小跑状，服务态度绝对不提速，样样都服务到位，点酒水还耐心的与我们解释，就这样绝对要夸一夸，特别是彭新星、洪继华也给我们宁波市形象增色，状元楼是宁波的一扇窗口，服务员的素质更体现我们宁波人的精神面貌。赞一个"


dst = translator.translate(chinese, src='zh-cn', dest='ja')
