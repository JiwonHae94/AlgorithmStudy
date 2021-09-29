
"""문제 설명
네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다.
 예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고, 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다.
 따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.

컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.

https://programmers.co.kr/learn/courses/30/lessons/43162


설명 : DFS를 이용해서 한 네트워크와 연결된 모든 네트워크를 추적해가며 연결된 네트워크의 개수를 셈
#space complexity : O(n)
#time complextity : O(n^2)
"""



def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]

    for i_com in range(n):
        if visited[i_com] == False:
            DFS(i_com, n, computers, visited)
            answer +=1
    return answer

def DFS(i_com, n, computers, visited):
    visited[i_com] = True

    for j_com in range(n):
        if j_com != i_com and computers[i_com][j_com] == 1:
            if visited[j_com] == False:
                DFS(j_com, n, computers, visited)




n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

print(solution(n, computers)) # answer is 2

