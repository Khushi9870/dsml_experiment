import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
mean_absolute_error,
mean_squared_error,
r2_score,
)
# Study hours (X) and examination score (y)
X = np.array([
1, 2, 2.5, 3, 4, 5,
5.5, 6, 7, 8, 9, 10,
], dtype=float).reshape(-1, 1)
y = np.array([
18, 25, 30, 34, 42, 52,
55, 61, 68, 76, 86, 92,
], dtype=float)
X_train, X_test, y_train, y_test = train_test_split(
X, y,
test_size=0.25,
random_state=42,
)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Coefficient:", model.coef_[0])
print("Intercept:", model.intercept_)
print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mse)
print("RMSE:", np.sqrt(mse))
print("R-squared:", r2_score(y_test, y_pred))
print("Score for 7.5 hours:", model.predict([[7.5]])[0])
# Plot full dataset and regression line
x_line = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
plt.scatter(X.ravel(), y, label="Observed data")
plt.plot(x_line.ravel(), model.predict(x_line), label="Best-fit line")
plt.xlabel("Study hours")
plt.ylabel("Score")
plt.title("Linear Regression")
plt.legend()
plt.grid(alpha=0.3)
plt.show()