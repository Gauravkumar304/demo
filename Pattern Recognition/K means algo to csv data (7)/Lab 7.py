import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier 
vdata=pd.read_csv("Salary_Data.csv")
x=vdata['Years of Experience'] 
y=vdata['Salary']
classes= [0,0,1,1,1,0,0,0,1,1,0,1,0,1,1,0,0,1,1]
data=list(zip(x,y))
knn=KNeighborsClassifier (n_neighbors=1)
knn.fit(data, classes)

import matplotlib.pyplot as plt
new_x=18
new_y=150000
new_point=[(new_x, new_y)]
prediction=knn.predict(new_point)
plt.scatter (x+[new_x], y+[new_y], c=classes+prediction[0]) 
plt.text(x=new_x-1.7,y=new_y-0.7,s=f"new point, class: {prediction[0]}")
plt.show()