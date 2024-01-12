import matplotlib.pyplot as plt
import pandas as pd
import random
import copy

def read():
    df = pd.read_excel(r'D:\Desktop\数据\DATA.xlsx')
    data = df.values.tolist()
    data = list(map(list, zip(*data)))
    return data

#主函数
if __name__ == "__main__":
    data = read()
    print(data)
    # 作图

    font = {'family': 'simhei',  # 这里必须要有第5行的操作前提
            'weight': 'normal',
            'size': 10,
            }
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.plot(data[0], data[1], color="red", linewidth=1.0, linestyle="-", label='SA')  # 将散点连在一起
    plt.plot(data[0], data[2], color="blue", linewidth=1.0, linestyle="-",  label = 'GA')
    plt.plot(data[0], data[3], color="green", linewidth=1.0, linestyle="-",  label = 'PSO')  # 将散点连在一起
    plt.plot(data[0], data[4], color="black", linewidth=1.0, linestyle="-",  label = 'Advanced SA')  # 将散点连在一起
    plt.legend(loc=0, prop=font, labelspacing=2, frameon=True)
    plt.xlabel('迭代次数')
    plt.ylabel('平均输出功率/w')
    plt.savefig("test.svg", dpi=300, format="svg")
    plt.show()