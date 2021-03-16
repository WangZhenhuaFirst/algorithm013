'''
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
'''


def merge(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    arr = [0] * (m+n)
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1
    while p1 >= 0 and p2 >= 0:
        if arr1[p1] < arr2[p2]:
            arr[p] = arr2[p2]
            p2 -= 1
        else:
            arr[p] = arr1[p1]
            p1 -= 1
        p -= 1
    arr[:p2+1] = arr2[:p2+1]
    arr[:p1+1] = arr1[:p1+1]
    return arr


if __name__ == "__main__":
    arr1 = [1, 3, 5]
    arr2 = [2, 4, 6]
    res = merge(arr1, arr2)
    print(res)
