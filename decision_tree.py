import matplotlib.pyplot as plt 
from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier, plot_tree 
from sklearn.metrics import ( 
    accuracy_score, 
    confusion_matrix, 
    classification_report, 
) 
 
# 1. Load data 
iris = load_iris() 
X = iris.data 
y = iris.target 
 
# 2. Split data 
X_train, X_test, y_train, y_test = train_test_split( 
    X, y, 
    test_size=0.25, 
    random_state=42, 
    stratify=y, 
) 
 
# 3. Create and train model 
model = DecisionTreeClassifier( 
    criterion="gini", 
    max_depth=3, 
    random_state=42, 
) 
model.fit(X_train, y_train) 
 
# 4. Test the model 
y_pred = model.predict(X_test) 
 
print("Accuracy:", accuracy_score(y_test, y_pred)) 
print("Confusion Matrix: ", confusion_matrix(y_test, y_pred)) 
print(classification_report( 
    y_test, y_pred, 
    target_names=iris.target_names, 
)) 
 
# 5. Predict one new flower 
new_flower = [[5.1, 3.5, 1.4, 0.2]] 
prediction = model.predict(new_flower)[0] 
print("New flower:", iris.target_names[prediction]) 
 
# 6. Visualize the tree 
plt.figure(figsize=(12, 7)) 
plot_tree( 
    model, 
    feature_names=iris.feature_names, 
    class_names=iris.target_names, 
    filled=True, 
    rounded=True, 
) 
plt.title("Decision Tree - Iris Dataset") 
plt.tight_layout() 
plt.show()