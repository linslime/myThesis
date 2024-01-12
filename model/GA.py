#传统模拟退火算法
import math
import time

import matplotlib.pyplot as plt
import csv
import random

#步长
step = 0.01
start = 0
end = 250

J1 = 14137.79

#退火初始温度
T = 0.5

#体积
def V(u1):
    if u1 <= 2:
        return math.pi * u1
    else:
        return 2 * math.pi +(1-math.pow((2.8-u1)/0.8,3)) * (0.8 * math.pi/3)

def J2(x2,x1):
    return 2433 * (0.25 + 0.2019575 + x2 - x1) * (0.25 + 0.2019575 + x2 - x1) + 354.8125

def f1(x,u1,u2,w1,w2,p1,p2,q1,q2):
    return u2

def f2(x,u1,u2,w1,w2,p1,p2,q1,q2):
    return (1760 * math.cos(1.9806 * x) - 528.5018 * u2 -V(u1) * 1025 * 9.8 + 80000 * (w1 - u1) + c1 * (w2 - u2)-(1-math.cos(p1+q1)) * 9.8 * 2433)*(1/(4866+1091.099))

def f3(x,u1,u2,w1,w2,p1,p2,q1,q2):
    return w2

def f4(x,u1,u2,w1,w2,p1,p2,q1,q2):
    return  (1-math.cos(p1+q1)) * 9.8 - 1 * (1/2433) * (80000 * (w1 - u1) + c1 * (w2 - u2))

def f5(x,u1,u2,w1,w2,p1,p2,q1,q2):
    return p2

def f6(x,u1,u2,w1,w2,p1,p2,q1,q2):
    return (2140 * math.cos(1.9806 * x) - 1655.909 * p2 - 8890.7 * p1 + 250000 * (q1 - p1) + d1 * (q2 - p2) - 1.2 * 4866 * 9.8 * math.sin(p1)) / (J1 + 7142.493)

def f7(x,u1,u2,w1,w2,p1,p2,q1,q2):
    return q2

def f8(x,u1,u2,w1,w2,p1,p2,q1,q2):
    return  ((0.25 + 0.2019575 + w1 - u1) * math.sin(p1 + q1) * 9.8 * 2433- 250000 * (q1 - p1) - d1 * (q2 - p2))/J2(w1,u1)

def RK4(u1,u2,w1,w2,p1,p2,q1,q2,x):
    for i in range(len(x) - 1):
        k11 = f1(x[i], u1[i], u2[i], w1[i], w2[i],p1[i],p2[i],q1[i],q2[i])
        k21 = f2(x[i], u1[i], u2[i], w1[i], w2[i],p1[i],p2[i],q1[i],q2[i])
        L11 = f3(x[i], u1[i], u2[i], w1[i], w2[i],p1[i],p2[i],q1[i],q2[i])
        L21 = f4(x[i], u1[i], u2[i], w1[i], w2[i],p1[i],p2[i],q1[i],q2[i])
        r11 = f5(x[i], u1[i], u2[i], w1[i], w2[i],p1[i],p2[i],q1[i],q2[i])
        r21 = f6(x[i], u1[i], u2[i], w1[i], w2[i],p1[i],p2[i],q1[i],q2[i])
        t11 = f7(x[i], u1[i], u2[i], w1[i], w2[i],p1[i],p2[i],q1[i],q2[i])
        t21 = f8(x[i], u1[i], u2[i], w1[i], w2[i],p1[i],p2[i],q1[i],q2[i])

        k12 = f1(x[i] + step / 2, u1[i] + step * k11 / 2, u2[i] + step * k21 / 2, w1[i] + step * L11 / 2, w2[i] + step * L21 / 2,p1[i] + step * r11/2,p2[i] + step * r21/2,q1[i] + step * t11/2,q2[i] + step * t21/2)
        k22 = f2(x[i] + step / 2, u1[i] + step * k11 / 2, u2[i] + step * k21 / 2, w1[i] + step * L11 / 2, w2[i] + step * L21 / 2,p1[i] + step * r11/2,p2[i] + step * r21/2,q1[i] + step * t11/2,q2[i] + step * t21/2)
        L12 = f3(x[i] + step / 2, u1[i] + step * k11 / 2, u2[i] + step * k21 / 2, w1[i] + step * L11 / 2, w2[i] + step * L21 / 2,p1[i] + step * r11/2,p2[i] + step * r21/2,q1[i] + step * t11/2,q2[i] + step * t21/2)
        L22 = f4(x[i] + step / 2, u1[i] + step * k11 / 2, u2[i] + step * k21 / 2, w1[i] + step * L11 / 2, w2[i] + step * L21 / 2,p1[i] + step * r11/2,p2[i] + step * r21/2,q1[i] + step * t11/2,q2[i] + step * t21/2)
        r12 = f5(x[i] + step / 2, u1[i] + step * k11 / 2, u2[i] + step * k21 / 2, w1[i] + step * L11 / 2, w2[i] + step * L21 / 2,p1[i] + step * r11/2,p2[i] + step * r21/2,q1[i] + step * t11/2,q2[i] + step * t21/2)
        r22 = f6(x[i] + step / 2, u1[i] + step * k11 / 2, u2[i] + step * k21 / 2, w1[i] + step * L11 / 2, w2[i] + step * L21 / 2,p1[i] + step * r11/2,p2[i] + step * r21/2,q1[i] + step * t11/2,q2[i] + step * t21/2)
        t12 = f7(x[i] + step / 2, u1[i] + step * k11 / 2, u2[i] + step * k21 / 2, w1[i] + step * L11 / 2, w2[i] + step * L21 / 2,p1[i] + step * r11/2,p2[i] + step * r21/2,q1[i] + step * t11/2,q2[i] + step * t21/2)
        t22 = f8(x[i] + step / 2, u1[i] + step * k11 / 2, u2[i] + step * k21 / 2, w1[i] + step * L11 / 2, w2[i] + step * L21 / 2,p1[i] + step * r11/2,p2[i] + step * r21/2,q1[i] + step * t11/2,q2[i] + step * t21/2)


        k13 = f1(x[i] + step / 2, u1[i] + step * k12 / 2, u2[i] + step * k22 / 2, w1[i] + step * L12 / 2, w2[i] + step * L22 / 2,p1[i] + step * r12/2,p2[i] + step * r22/2,q1[i] + step * t12/2,q2[i] + step * t22/2)
        k23 = f2(x[i] + step / 2, u1[i] + step * k12 / 2, u2[i] + step * k22 / 2, w1[i] + step * L12 / 2, w2[i] + step * L22 / 2,p1[i] + step * r12/2,p2[i] + step * r22/2,q1[i] + step * t12/2,q2[i] + step * t22/2)
        L13 = f3(x[i] + step / 2, u1[i] + step * k12 / 2, u2[i] + step * k22 / 2, w1[i] + step * L12 / 2, w2[i] + step * L22 / 2,p1[i] + step * r12/2,p2[i] + step * r22/2,q1[i] + step * t12/2,q2[i] + step * t22/2)
        L23 = f4(x[i] + step / 2, u1[i] + step * k12 / 2, u2[i] + step * k22 / 2, w1[i] + step * L12 / 2, w2[i] + step * L22 / 2,p1[i] + step * r12/2,p2[i] + step * r22/2,q1[i] + step * t12/2,q2[i] + step * t22/2)
        r13 = f5(x[i] + step / 2, u1[i] + step * k12 / 2, u2[i] + step * k22 / 2, w1[i] + step * L12 / 2, w2[i] + step * L22 / 2,p1[i] + step * r12/2,p2[i] + step * r22/2,q1[i] + step * t12/2,q2[i] + step * t22/2)
        r23 = f6(x[i] + step / 2, u1[i] + step * k12 / 2, u2[i] + step * k22 / 2, w1[i] + step * L12 / 2, w2[i] + step * L22 / 2,p1[i] + step * r12/2,p2[i] + step * r22/2,q1[i] + step * t12/2,q2[i] + step * t22/2)
        t13 = f7(x[i] + step / 2, u1[i] + step * k12 / 2, u2[i] + step * k22 / 2, w1[i] + step * L12 / 2, w2[i] + step * L22 / 2,p1[i] + step * r12/2,p2[i] + step * r22/2,q1[i] + step * t12/2,q2[i] + step * t22/2)
        t23 = f8(x[i] + step / 2, u1[i] + step * k12 / 2, u2[i] + step * k22 / 2, w1[i] + step * L12 / 2, w2[i] + step * L22 / 2,p1[i] + step * r12/2,p2[i] + step * r22/2,q1[i] + step * t12/2,q2[i] + step * t22/2)

        k14 = f1(x[i] + step, u1[i] + step * k13, u2[i] + step * k23, w1[i] + step * L13, w2[i] + step * L23,p1[i] + step * r13, p2[i] + step * r23,q1[i] + step * t13,q2[i] + step * t23)
        k24 = f2(x[i] + step, u1[i] + step * k13, u2[i] + step * k23, w1[i] + step * L13, w2[i] + step * L23,p1[i] + step * r13, p2[i] + step * r23,q1[i] + step * t13,q2[i] + step * t23)
        L14 = f3(x[i] + step, u1[i] + step * k13, u2[i] + step * k23, w1[i] + step * L13, w2[i] + step * L23,p1[i] + step * r13, p2[i] + step * r23,q1[i] + step * t13,q2[i] + step * t23)
        L24 = f4(x[i] + step, u1[i] + step * k13, u2[i] + step * k23, w1[i] + step * L13, w2[i] + step * L23,p1[i] + step * r13, p2[i] + step * r23,q1[i] + step * t13,q2[i] + step * t23)
        r14 = f5(x[i] + step, u1[i] + step * k13, u2[i] + step * k23, w1[i] + step * L13, w2[i] + step * L23,p1[i] + step * r13, p2[i] + step * r23,q1[i] + step * t13,q2[i] + step * t23)
        r24 = f6(x[i] + step, u1[i] + step * k13, u2[i] + step * k23, w1[i] + step * L13, w2[i] + step * L23,p1[i] + step * r13, p2[i] + step * r23,q1[i] + step * t13,q2[i] + step * t23)
        t14 = f7(x[i] + step, u1[i] + step * k13, u2[i] + step * k23, w1[i] + step * L13, w2[i] + step * L23,p1[i] + step * r13, p2[i] + step * r23,q1[i] + step * t13,q2[i] + step * t23)
        t24 = f8(x[i] + step, u1[i] + step * k13, u2[i] + step * k23, w1[i] + step * L13, w2[i] + step * L23,p1[i] + step * r13, p2[i] + step * r23,q1[i] + step * t13,q2[i] + step * t23)

        u1[i + 1] = u1[i] + step / 6 * (k11 + 2 * k12 + 2 * k13 + k14)
        u2[i + 1] = u2[i] + step / 6 * (k21 + 2 * k22 + 2 * k23 + k24)
        w1[i + 1] = w1[i] + step / 6 * (L11 + 2 * L12 + 2 * L13 + L14)
        w2[i + 1] = w2[i] + step / 6 * (L21 + 2 * L22 + 2 * L23 + L24)
        p1[i + 1] = p1[i] + step / 6 * (r11 + 2 * r12 + 2 * r13 + r14)
        p2[i + 1] = p2[i] + step / 6 * (r21 + 2 * r22 + 2 * r23 + r24)
        q1[i + 1] = q1[i] + step / 6 * (t11 + 2 * t12 + 2 * t13 + t14)
        q2[i + 1] = q2[i] + step / 6 * (t21 + 2 * t22 + 2 * t23 + t24)
        # print(p2[i])

def construction(n):
    list = []
    for i in range(n):
        # list.append([random.randint(0,200000),random.randint(0,200000)])
        list.append([random.randint(100, 200), random.randint(50000, 60000)])
    value = []
    for i in range(n):
        value.append(getValue(list[i][0],list[i][1]))
    return list,value

def getValue(z0,x0):
    global c1
    global d1
    c1 = z0
    d1 = x0
    x = []
    temp = start
    while temp <= end:
        x.append(temp)
        temp += step

    u1 = [0 for i in range(len(x))]
    u2 = [0 for i in range(len(x))]
    w1 = [0 for i in range(len(x))]
    w2 = [0 for i in range(len(x))]
    p1 = [0 for i in range(len(x))]
    p2 = [0 for i in range(len(x))]
    q1 = [0 for i in range(len(x))]
    q2 = [0 for i in range(len(x))]
    RK4(u1, u2, w1, w2, p1, p2, q1, q2, x)
    p = [c1 * (u2[i] - w2[i]) * (u2[i] - w2[i]) + d1 * (p2[i] - q2[i]) * (p2[i] - q2[i]) for i in range(15000, 25000)]
    value = sum(p) / len(p)
    return value

def selection(value):
    first = random.randint(0,len(value) - 1)
    second = random.randint(0,len(value) - 1)
    while first == second:
        second = random.randint(0,len(value) - 1)
    return first,second

def encode(n):
    str = bin(n)
    list = [int(str[i]) for i in range(2,len(str))]
    return list

def decode(list):
    value = 0
    n = len(list) - 1
    for i in list:
        value += i * math.pow(2,n)
        n = n - 1
    return int(value)

def crossOver(list1,list2):
    if len(list1) > len(list2):
        list2 = [0 for i in range(len(list1) - len(list2))] + list2
    else:
        list1 = [0 for i in range(len(list2) - len(list1))] + list1
    if len(list1) < 18:
        list1 = [0 for i in range(3)] + list1
        list2 = [0 for i in range(3)] + list2
    ans = []
    for i in range(len(list1)):
        if list1[i] == list2[i] or random.random()<0.5:
            ans.append(list1[i])
        else:
            ans.append(list2[i])
    return ans

def mutation(list):
    a = random.randint(0,len(list)-1)
    list[a] = 1 - list[a]
    return list

def g_crossOver(f,s):
    n = len(f)
    ans = []

    for i in range(n):
        fs = encode(f[i])
        ss = encode(s[i])
        list = crossOver(fs,ss)
        if random.random()<0.5:
            list = mutation(list)
        a = decode(list)
        if a > 100000:
            a = 100000
        ans.append(a)
    value = getValue(ans[0],ans[1])
    return ans,value

#主函数
if __name__ == "__main__":

    community,value = construction(10)
    sss = time.time()
    for i in range(1000):
        first, second = selection(value)
        f = community[first]
        s = community[second]
        ans, tempValue = g_crossOver(f, s)
        index = value.index(min(value))
        community[index] = ans
        value[index] = tempValue
        index = value.index(max(value))
        print(community[index][0],community[index][1],value[index],time.time() - sss)
    # with open("D:\Desktop\\SA.csv", "w", newline="") as csvfile:
    #     writer = csv.writer(csvfile)
    #     writer.writerows(list(map(list, zip(*aver))))
