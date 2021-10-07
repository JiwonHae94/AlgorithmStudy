"""
두 개의 단어 begin, target과 단어의 집합 words가 있습니다. 아래와 같은 규칙을 이용하여 begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾으려고 합니다.

1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
2. words에 있는 단어로만 변환할 수 있습니다.
예를 들어 begin이 "hit", target가 "cog", words가 ["hot","dot","dog","lot","log","cog"]라면 "hit" -> "hot" -> "dot" -> "dog" -> "cog"와 같이 4단계를 거쳐 변환할 수 있습니다.

두 개의 단어 begin, target과 단어의 집합 words가 매개변수로 주어질 때, 최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지 return 하도록 solution 함수를 작성해주세요.

설명: DFS를 통해 처음 알파벳기준으로 바꿔가면 최소 몇단계로 변할수있는지 센다

#space complexity : O(words)
#time complextity : O(words*begin )
"""


answer = 1e2
def solution(begin, target, words):
    if target not in words:
        return 0

    tmp_answer = 0

    visited = [False for i in range(len(words))]
    DFS(begin, target, words, visited, tmp_answer)

    return answer

def DFS(begin, target, words, visited, tmp_answer):
    global answer

    if begin == target:
        print(tmp_answer)
        if tmp_answer < answer:

            answer = tmp_answer
        return
    else:
        if len(visited) == sum(visited):
            return

        for i_word in range(len(words)):
            if visited[i_word] == False:

                for i_char in range(len(begin)):
                    if begin[:i_char] == words[i_word][:i_char] and begin[i_char+1:] == words[i_word][i_char+1:]:
                        DFS(words[i_word], target, words, visited[:i_word]+[True]+visited[i_word+1:], tmp_answer+1)

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]


print(solution(begin, target, words))