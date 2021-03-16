'''
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
arr3 = []
'''

import heapq


def merge(*args):
    res = []
    h = []
    for arr in args:
        for num in arr:
            heapq.heappush(h, num)
    while h:
        res.append(heapq.heappop(h))
    return res


if __name__ == "__main__":
    arr1 = [1, 5, 7]
    arr2 = [2, 3, 9]
    arr3 = [4, 6, 8]
    res = merge(arr1, arr2, arr3)
    print(res)
