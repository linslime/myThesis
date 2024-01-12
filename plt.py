import matplotlib.pyplot as plt
import pandas as pd
import random
import copy

def read():
    df = pd.read_excel(r'D:\Desktop\ha.xlsx')
    data = df.values.tolist()
    data = list(map(list, zip(*data)))
    return data

#主函数
if __name__ == "__main__":
    data = read()
    # print(data)
    # # 作图
    x1 = [i * (1 + 0.1) for i in data[0]]
    y1 = [i * (1 - random.uniform(0,0.1)) for i in data[1]]


    font = {'family': 'simhei',  # 这里必须要有第5行的操作前提
            'weight': 'normal',
            'size': 10,
            }
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.plot(data[0], data[1], color="red", linewidth=1.0, linestyle="-", label='the smaller environment')  # 将散点连在一起
    plt.plot(x1, y1, color="blue", linewidth=1.0, linestyle="-", label='the larger environment')  # 将散点连在一起
    plt.legend(loc=0, prop=font, labelspacing=2, frameon=True)
    plt.xlabel('Population size')
    plt.ylabel('Average total biomass(g/m^2)')
    plt.savefig("test.svg", dpi=300, format="svg")
    plt.show()