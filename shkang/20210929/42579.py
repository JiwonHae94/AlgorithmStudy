"""
스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

속한 노래가 많이 재생된 장르를 먼저 수록합니다.
장르 내에서 많이 재생된 노래를 먼저 수록합니다.
장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

https://programmers.co.kr/learn/courses/30/lessons/42579


설명 : dictionary를 이용해서 [장르](key1)에 따라 [[고유번호](key2) -> [노래재생횟수](value2)](value1)를 매칭하여 문제를 품

#space complexity : O(2n)
#time complextity : O(n^2)
"""

def solution(genres, plays):

    cnt = {}
    genres_to_play = {}
    answer = []

    for i, (i_g, i_p) in enumerate(zip(genres, plays)):
        if i_g not in genres_to_play:
            genres_to_play[i_g] = {i: i_p}
        else:
            genres_to_play[i_g][i] = i_p

        cnt[i_g] = cnt.get(i_g, 0) + i_p

    for genres, count in sorted(cnt.items(), key=lambda x: x[1], reverse=True):
        for id, plays in sorted(genres_to_play[genres].items(), key=lambda x: x[1], reverse=True)[:2]:
            answer.append(id)

    return answer


genres = ["classic", "pop", "classic", "classic", "pop"]
playes = [500, 600, 150, 800, 2500]

print(solution(genres, playes))