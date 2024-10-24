import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('2024_seoul_data.csv', encoding='utf-8')


df.rename(columns={
    '최저기온': 'min_temp',
    '평균기온': 'avg_temp',
    '최고기온': 'max_temp'
}, inplace=True)

df.fillna(method='ffill', inplace=True)

df['min_temp'] = pd.to_numeric(df['min_temp'], errors='coerce')
df['avg_temp'] = pd.to_numeric(df['avg_temp'], errors='coerce')
df['max_temp'] = pd.to_numeric(df['max_temp'], errors='coerce')

plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

plt.title('서울시 2024년도 여름 기온 변화')
plt.plot(range(1, len(df) + 1), df['max_temp'], label='최고기온', color='red')
plt.plot(range(1, len(df) + 1), df['avg_temp'], label='평균기온', color='yellow')
plt.plot(range(1, len(df) + 1), df['min_temp'], label='최저기온', color='blue')
plt.xlabel('일')
plt.ylabel('기온')
plt.legend()
plt.show()
