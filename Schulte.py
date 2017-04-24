#-*- encoding:utf-8 -*-

from random import shuffle
from os import system
''' 该模块内的函数只适合在模块内是使用，不适合其它模块或函数调用。
'''
def get_non_negative_integer():
    """ 从终端读取一个整数
        该方法可以接受的用户输入为大于等于零的整数或者是空行
        返回一个大于等于-1的整数，（这里，将空行映射为整数 -1）
    """
    while True:
        r_num = raw_input("please input a positive integer(0<zero> to quit):").strip()
        #注意，当r_num是负数时（比如-1),r_num.isdigit()判定为False，这时候该字符串不是纯数字
        if r_num.isdigit() :return int(r_num)
        elif len(r_num)==0:return -1
        else:print "I'm sorry,but '{}' isn't valid.".format(r_num)


def get_schulte(n):
    """ 返回一个n行n列的舒尔特表。
        n是一个正整数。
    """
    if type(n) != type(1):return
    vs = range(1,n*n+1)
    shuffle(vs)
    schulte = []

    for i in range (0,n*n,n):
        schulte.append(vs[i:i+n])
    return schulte

def show_schulte(schulte):
    """ 打印输出舒尔特表
    """
    for row in schulte:
        for cell in row:
            print " {:<3}".format(cell),
        print "\n"

def main():
    ''' 程序入口函数
    '''
    old_n = 3
    for i in range(1,11):#最多重复十次
        print "{:2}".format(i),"*"*40

        n = get_non_negative_integer();

        if n >= 1:
            old_n = n #记住上一次的n值
        elif n==-1:   #n为-1时，使用上一次的n值
            n = old_n
        else:         #否则，结束循环
            break
        show_schulte(get_schulte(n))
    print "Bye!"
    system("pause")



if __name__=="__main__":
    main()