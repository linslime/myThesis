import random
import numpy as np

def getVariance(value,deviation):
    list = []
    for i in range(100):
        list.append(random.uniform(value-deviation,value+deviation))
    list_mean = np.mean(list)
    list_var = np.var(list)
    list_std = np.std(list,ddof=1)
    return list_mean,list_var,list_std
#主函数
if __name__ == "__main__":
    print(getVariance(321.98,0.7))