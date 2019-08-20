from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn import svm
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