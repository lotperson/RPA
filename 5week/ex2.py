import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

def addtext(x,y):
    for i in range(len(x)):
        plt.text(i,y[i]+0.5,y[i], ha = 'center')
        
hat = pd.read_csv('singer_youtube.csv')
print(hat.head(), end="\n\n")

font_path = "malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
plt.rc('font',family=font_name)

name = ["여자친구", "소녀시대", "레드벨벳", "에이핑크", "마마무", "트와이스", "블랙핑크", "오마이걸", "있지", "우주소녀"]
youtube_count = [800, 1114600, 44500, 2900, 6900, 3334500, 443700, 3500, 21300, 350]


plt.figure(figsize=(10, 6))
plt.barh(name, youtube_count,color=('red','orange','yellow','green','blue','navy','purple'))
plt.xlabel('youtube count')
plt.gca().invert_yaxis()  
plt.xticks(rotation=45)
plt.show()

#plt.show()#
