"""
출발지점부터 distance만큼 떨어진 곳에 도착지점이 있습니다. 그리고 그사이에는 바위들이 놓여있습니다. 바위 중 몇 개를 제거하려고 합니다.
예를 들어, 도착지점이 25만큼 떨어져 있고, 바위가 [2, 14, 11, 21, 17] 지점에 놓여있을 때 바위 2개를 제거하면 출발지점, 도착지점, 바위 간의 거리가 아래와 같습니다.

제거한 바위의 위치	각 바위 사이의 거리	거리의 최솟값
[21, 17]	[2, 9, 3, 11]	2
[2, 21]	[11, 3, 3, 8]	3
[2, 11]	[14, 3, 4, 4]	3
[11, 21]	[2, 12, 3, 8]	2
[2, 14]	[11, 6, 4, 4]	4
위에서 구한 거리의 최솟값 중에 가장 큰 값은 4입니다.

출발지점부터 도착지점까지의 거리 distance, 바위들이 있는 위치를 담은 배열 rocks, 제거할 바위의 수 n이 매개변수로 주어질 때,
바위를 n개 제거한 뒤 각 지점 사이의 거리의 최솟값 중에 가장 큰 값을 return 하도록 solution 함수를 작성해주세요.

https://programmers.co.kr/learn/courses/30/lessons/43236

설명: 주어진 rocks를 정렬해줘야 바위 사이의 거리를 구하므로 정렬부터 한뒤 이분탐색에서  최소값은 1 최대값은  바위끼리의 간격이 모두 같을 때이다.
그리고 이분 탐색을 통해 removed rocks가 n보다 작은 경우에 mid를 출력

space complexity : O(6)
time complextity : O(nlogn)

"""


def solution(distance, rocks, n):
    rocks.append(distance)
    rocks.sort()
    asnwer = 0
    left, right = 1, distance // (len(rocks) -n)

    while left < right:
        mid = (left + right) // 2

        removed_rocks = 0
        prev_rock = 0
        for i_rock in rocks:
            if i_rock - prev_rock < mid:
                removed_rocks += 1
            else:
                prev_rock = i_rock

        if removed_rocks > n:
            right = mid
        else:
            asnwer = mid
            left = mid + 1
    return asnwer



distance = 25
rocks = [2, 14, 11, 21, 17]
n =2

print(solution(distance, rocks, n))