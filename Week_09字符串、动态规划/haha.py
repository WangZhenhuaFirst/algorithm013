def count_number(strs):
    count = 0
    res = []
    for i, s in enumerate(strs):
        if count == 0:
            res.append(s)
        if s != res[-1]:
            res.append(str(count))
            res.append(s)
            count = 0
        elif i == len(strs) - 1:
            res.append(str(count + 1))
        count += 1
    return ''.join(res)


if __name__ == "__main__":
    strs = 'aaabbcaa'
    res = solve(strs)
    print(res)

