def binary_search(a, t):
    """
    二分查找: 在一个排好序的数组里找某个元素
    时间复杂度：O(logn)
    空间复杂度： O(1)
    """
    l, r = 0, len(a) - 1
    while l <= r:
        m = (l + r) // 2
        if a[m] < t:
            l = m + 1
        elif a[m] > t:
            r = m - 1
        else:
            return m
    return -1


if __name__ == '__main__':
    print(binary_search([1, 5, 10, 12, 13], 9))
