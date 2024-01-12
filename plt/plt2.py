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
    fig, ax = plt.subplots(figsize=(10, 6.18))
    markersize = 2
    linewidth = 1
    ax.plot(
        data[0], data[1], "-o",  # 同时创建曲线和散点
        markersize=markersize,  # 控制点的大小
        linewidth=linewidth,  # 控制线的大小
        markerfacecolor="red",  # 控制圆圈填充的颜色
        markeredgecolor="red",  # 控制圆圈边缘的颜色
        markeredgewidth=markersize,  # 控制圆圈边缘的大小
        label='SA'
    )
    ax.plot(
        data[0], data[2], "-o",  # 同时创建曲线和散点
        markersize=markersize,  # 控制点的大小
        linewidth=linewidth,  # 控制线的大小
        markerfacecolor="blue",  # 控制圆圈填充的颜色
        markeredgecolor="blue",  # 控制圆圈边缘的颜色
        markeredgewidth=markersize,  # 控制圆圈边缘的大小
        label = 'GA'
    )
    ax.plot(
        data[0], data[3], "-o",  # 同时创建曲线和散点
        markersize=markersize,  # 控制点的大小
        linewidth=linewidth,  # 控制线的大小
        markerfacecolor="green",  # 控制圆圈填充的颜色
        markeredgecolor="green",  # 控制圆圈边缘的颜色
        markeredgewidth=markersize,  # 控制圆圈边缘的大小
        label = 'PSO'
    )
    ax.plot(
        data[0], data[4], "-o",  # 同时创建曲线和散点
        markersize=markersize,  # 控制点的大小
        linewidth=linewidth,  # 控制线的大小
        markerfacecolor="yellow",  # 控制圆圈填充的颜色
        markeredgecolor="yellow",  # 控制圆圈边缘的颜色
        markeredgewidth=markersize,  # 控制圆圈边缘的大小
        label = 'Advanced SA'
    )
    plt.legend(loc=0, prop=font, labelspacing=2, frameon=True)
    plt.xlabel('迭代次数')
    plt.ylabel('平均输出功率/w')
    plt.savefig("test.svg", dpi=300, format="svg")
    plt.show()