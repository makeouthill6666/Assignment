# import time
#
# start = time.time()
#
# for i in range(1, 6):
#     print (i)
#
# end = time.time()
# print (end - start)
# print (ord("ㄱ"))
# print (ord("愛"))

# numbers = [1, 2, 3, 4, 5]
# for i in numbers:
#     for j in numbers:
#         for h in numbers:
#             x = i + j + h
#             print(x)
#

# 비재귀적 이진탐색의 Python 코드
def binary_search (arr, val):
    first, last = 0, len(arr) - 1
    while first <= last:
        mid = (first + last) // 2
        if arr[mid] == val:
            return mid
        if arr[mid] > val:
            last = mid - 1
        else:
            first = mid + 1
    return -1