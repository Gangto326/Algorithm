import sys

read = sys.stdin.readline
N, C = map(int, read().split())

house_list = []

for i in range(N):
    house_list.append(int(read()))

house_list.sort()


"""
공유기를 설치할 집을 구하는 것은 N개를 전부 훑어도 됨 => 200,000 * log(1,000,000,000) = 약 6,000,000
"""
def binary_search(before_left, target, count):
    while count > 0:
        left = before_left+1
        right = N

        while left < right:
            mid = (left+right) // 2

            if (house_list[mid] - house_list[before_left]) < target:
                left = mid+1
            else:
                right = mid
        
        if left < N:
            before_left = left
            count -= 1
        else:
            return False
    
    return True


interval_left = 1
interval_right = house_list[-1] - house_list[0] + 1

while interval_left < interval_right:
    interval_mid = (interval_left + interval_right) // 2

    if binary_search(0, interval_mid, C-1):
        interval_left = interval_mid+1
    
    else:
        interval_right = interval_mid

print(interval_left-1)
