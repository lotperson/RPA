import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv('2024_seoul_data.csv',encoding='utf-8')
df2 = df.fillna(method ='ffill')
df2.info()

df.rename(columns={'최저기온':'min_temp'},inplace=True)
df.rename(columns={'평균기온':'avg_temp'},inplace=True)
df.rename(columns={'최고기온':'max_temp'},inplace=True)
df2.head(3)

plt.rc('font',family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

plt.title('서울시 2024년도 여름 기온 변화')
plt.plot(range(1, len(df) + 1), df['max_temp'], label='최고기온', color='red')
plt.plot(range(1, len(df) + 1), df['avg_temp'], label='평균기온', color='yellow')
plt.plot(range(1, len(df) + 1), df['min_temp'], label='최저기온', color='blue')
plt.xlabel('일')
plt.xlabel('일')
plt.ylabel('기온')
plt.legend()
plt.show()