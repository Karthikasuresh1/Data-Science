import matplotlib.pyplot as plt
data_students=[5,15,25,15,45,55]
plt.hist(data_students,bins=[0,10,20,30,40,50,60],weights=[10,2,0,20,3,2],edgecolor="red")
plt.show()