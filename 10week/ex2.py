
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf


w = pd.read_csv('ch5-1.csv')
w_n = w.iloc[:, 1:5]


model_lm_food = smf.ols(formula='weight ~ food', data=w_n)
result_lm_food = model_lm_food.fit()


print(result_lm_food.summary())


plt.figure(figsize=(10, 7))
plt.scatter(w.food, w.weight, alpha=0.5)
plt.plot(w.food, result_lm_food.params['Intercept'] + result_lm_food.params['food'] * w.food, color='red')
plt.text(66, 132, f'weight = {result_lm_food.params["Intercept"]:.4f} + {result_lm_food.params["food"]:.4f} * food', fontsize=12)
plt.title('Scatter Plot of Weight vs. Food')
plt.xlabel('Food')
plt.ylabel('Weight')
plt.show()
