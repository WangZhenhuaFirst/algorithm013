'''
[布隆过滤器的原理和实现](https://www.cnblogs.com/cpselvis/p/6265825.html)
[使用布隆过滤器解决缓存击穿、垃圾邮件识别、集合判重](https://blog.csdn.net/tianyaleixiaowu/article/details/74721877)
[布隆过滤器 Python 实现示例](https://www.geeksforgeeks.org/bloom-filters-introduction-and-python-implementation/)
[高性能布隆过滤器 Python 实现示例](https://github.com/jhgg/pybloof)

[布隆过滤器 Python 代码示例](https://shimo.im/docs/UITYMj1eK88JCJTH/read)
'''


from bitarray import bitarray
import mmh3


class BloomFilter:
    def __init__(self, size, hash_num):
        self.size = size
        self.hash_num = hash_num  # 一个元素用几个二进制位来表示它
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def add(self, s):
        for seed in range(self.hash_num):
            result = mmh3.hash(s, seed) % self.size  # 取模是为了防止下标超过范围
            self.bit_array[result] = 1

    def lookup(self, s):
        for seed in range(self.hash_num):
            result = mmh3.hash(s, seed) % self.size
            if self.bit_array[result] == 0:
                return 'Nope'
        return "Porbably"


bf = BloomFilter(500000, 7)
bf.add("dantezhao")
print(bf.lookup("dantezhao"))
print(bf.lookup("yyj"))
