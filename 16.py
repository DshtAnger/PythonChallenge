#coding:utf-8
class Fib(object):

    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __str__(self):
        return "I am Fib!"

    def __repr__(slef):
        return "Yes!"

    def __len__(self):
        return 666

    # 实例本身就是迭代对象，故返回自己
    def __iter__(self):
        return self 

    def next(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration();
        return self.a # 返回下一个值

    #使对象能像列表那样按下标取元素,以及切片
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

'''for n in Fib():
    print n'''

print Fib()[:10]
