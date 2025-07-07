import numpy as np
import matplotlib.pyplot as plt
a=-37.49999
b=11.34999
x=np.array([3,4,5,6,7,8,9])
y=np.array([4.8,8.4,14.3,23.6,36.2,52.8,71.9])
y_pred=a+b*x
plt.scatter(x,y,color='red',label='data points')
plt.plot(x,y_pred,color='blue',label='Best fit line')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Least Square Method:y=a+bx')

plt.show()
