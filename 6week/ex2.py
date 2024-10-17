import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import seaborn as sns 

hat = pd.read_csv('ch4-2.csv')

font_path = "malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)
print(hat.describe(),end="\n\n")

plt.figure(figsize=(8,10))
plt.boxplot(hat.weight)
plt.title('B hatchery chick weight box',fontsize =17)
plt.ylabel('weight (g)')


plt.show()