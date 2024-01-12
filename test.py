import time
#主函数
if __name__ == "__main__":
    start = time.time()
    for i in range(100000000):
        a = 1
    end = time.time()
    print(end - start)