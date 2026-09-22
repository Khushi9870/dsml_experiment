import numpy as np
import matplotlib. pylab as plt 
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, confusion_matrix
iris=load_iris()
X=iris.data
y=iris.target
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=42,stratify=y,)
model=Pipeline([("scaler",StandardScaler()),("svm",SVC(kernel="rbf",C=1.0,gamma="scale",)),])
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
print("Accuracy:",accuracy_score(y_test,y_pred))
print("Confusion matrix",confusion_matrix(y_test,y_pred))
print("New pridiction:",iris.target_names[model.predict([[6.3,3.3,6.0,2.5]])[0]])
#optional 2D visualization using petal features only
X_2D=iris.data[:,2:4]
visual_model=Pipeline([("Scaler",StandardScaler()),("svm",SVC(kernel="rbf",C=1.0,gamma="scale")),])
visual_model.fit(X_2D,y)
x_min,x_max=X_2D[:,0].min()-0.5,X_2D[:,0].max()+0.5
y_min,y_max=X_2D[:,1].min()-0.5,X_2D[:1,].max()+0.5
xx,yy=np.meshgrid(np.linspace(x_min,x_max,350),np.linspace(y_min,y_max,350),)
Z=visual_model.predict(np.c_[xx.ravel(),yy.ravel()])
Z=Z.reshape(xx.shape)
plt.contourf(xx,yy,Z,alpha=0.25)
plt.scatter(X_2D[:,1],X_2D[:,1],c=y,edgecolor="k")
plt.xlabel("Petal length")
plt.ylabel("Petal width")
plt.title("SVM Decision Regions")
plt.show()