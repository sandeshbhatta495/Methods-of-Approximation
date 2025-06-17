import numpy as np
import matplotlib.pyplot as plt
a=3
b=4
x=np.array([12,15,21,25])
y=np.array([50,70,100,120])
y_pred=a+b*x
plt.scatter(x,y,color='red',label='data points')
plt.plot(x,y_pred,color='blue',label='Best fit line')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Least Square Method:y=a+bx')

plt.show()
