import pandas as pd
from sklearn import linear_model
import statsmodels.api as sm

data = pd.read_csv('starbucks.csv')
data_top = data.head()
print(data_top)

X = data[['fat', 'carb','fiber', 'protein']]
Y = data[['calories']]

reg = linear_model.LinearRegression()
reg.fit(X, Y)

print('Intercept: \n', reg.intercept_)
print('Coefficients: \n', reg.coef_)