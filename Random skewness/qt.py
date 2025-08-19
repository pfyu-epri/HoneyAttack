from multiprocessing import Pool
import os, time, random

def factorial(x):                                               ## 阶乘计算函数
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result


    
def long_time_task(name):                                       ## 多线程计算Q- 和 Q+ 
    t = 1                                                       ## 声明变量，t和N的初始值无意义，下面的代码会改变这两个值
    k = 20                                                      ## k = 20, sweetwords数量
    N = 5000

    for N in range(5000+name*11875, 5000+(name+1)*11875):       ## name, 从0变化至7, 共8个线程; 5000至10,0000分成8份, 每份是(100000-5000)/8 = 11875
        e =(N-1)**(N-1)                                         ## 公式化简后, e等于(N-1)的(N-1)次幂
        
        ## Q-
        Qminus = 0
        for t in range(1, k):                                   ## t从1变化到k-1
            a = 1
            for i in range(N-1, N-t, -1):                       ## 这两行计算公式中的a, 从(N-1)连续乘到(N-t+1)
                a = a * i
            b = (k-1) ** (t-1)                                  ## 计算公式中的b, b等于(k-1)的(t-1)次幂
            c = (N-k) ** (N-t)                                  ## 计算公式中的c, c等于(N-k)的(N-t)次幂
            d = factorial(t-1)                                  ## 计算公式中的d, d等于(t-1)的阶层

            Qminus += (a*b*c)/(d*e)                             ## Q- 是 qt 中 t 从 1 变化到 k-1 的累加

        ## q_k                                                  ## qk 即 qt 中 t 取 k 时的值
        t = k
        a = 1
        for i in range(N-1, N-t, -1):                           ## 接下来5行代码与计算 qt 一致
            a = a * i
        b = (k-1) ** (t-1)
        c = (N-k) ** (N-t)
        d = factorial(t-1)
        qk = (a*b*c)/(d*e)                                      ## qt化简后的公式

        ## Q+
        Qplus = 1.0 - (qk + Qminus)                             ## 计算 Q+
        print(str(N), Qminus, Qplus, sep='\t')                  ## 输出格式为 N, Q-, Q+


if __name__=='__main__':
##print('Parent process %s.' % os.getpid())
    p = Pool(8)                                                 ## 含有8个线程的池子
    for i in range(8):                                          
        p.apply_async(long_time_task, args=(i,))                ## 传入参数i, 从0到7, 在任务函数中name接受 i 的值
##print('Waiting for all subprocesses done...')
    p.close()
    p.join()
##print('All subprocesses done.')
    

