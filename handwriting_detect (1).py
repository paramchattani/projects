from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn import metrics
from sklearn.model_selection import train_test_split
digits=datasets.load_digits()
#dir(digits)
#print(digits.DESCR)
#print(digits.data)
#print(digits.images[-20])
#print(digits.target)
#print(digits.target_names)
clf=svm.SVC(gamma=0.001,C=100)
x=digits.data[:-40]
y=digits.target[:-40]
train=clf.fit(x,y)
result=train.predict([digits.data[-5]])
print(result)
plt.imshow(digits.images[-5],cmap=plt.cm.gray_r)
plt.show()
x_train,x_test,y_train,y_test=train_test_split(digits.data,digits.target,test_size=0.3,random_state=1)
clfs=svm.SVC(gamma=0.005,C=500)
a=clfs.fit(x_train,y_train)
y_pred=a.predict(x_test);
print(metrics.accuracy_score(y_test,y_pred))
print(metrics.confusion_matrix(y_test,y_pred))
print(metrics.classification_report(y_test,y_pred))
