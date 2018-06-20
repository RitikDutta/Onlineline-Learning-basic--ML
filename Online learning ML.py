import numpy as np
from matplotlib import pyplot as plt
%matplotlib inline
class OnlineLearn():
    from sklearn.linear_model import LinearRegression
    regg = LinearRegression()
    def onlineLearn(self):
        num_array = list()
        num = input("Enter how many elements you want:")
        print ('Enter numbers in array: ')
        for i in range(int(num)):
            n = input("num :")
            num_array.append(int(n))
        y = np.array(num_array).reshape(-1,1)
        X = np.array(np.arange(1,len(y)+1)).reshape(-1, 1)
        self.regg.fit(X, y)
        nextOutput = self.regg.predict(len(y)+1)
        print("Your next value will be", round(nextOutput[0,0]))
        #plt.bar(plt.bar([1,2,3,4,5,6,7,8,9],num_array))
        plt.plot(X, y, color = 'red')
        plt.scatter(len(y)+1, round(nextOutput[0,0]))
onn = OnlineLearn()