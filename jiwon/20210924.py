
# -------------------------------------
# category : HashMap
# Q : 카카오톡 오픈채팅방에서는 친구가 아닌 사람들과 대화를 할 수 있는데, 본래 닉네임이 아닌 가상의 닉네임을 사용하여 채팅방에 들어갈 수 있다.
#     신입사원인 김크루는 카카오톡 오픈 채팅방을 개설한 사람을 위해, 다양한 사람들이 들어오고, 나가는 것을 지켜볼 수 있는 관리자창을 만들기로 했다. 채팅방에 누군가 들어오면 다음 메시지가 출력된다.
#     "[닉네임]님이 들어왔습니다."
#     채팅방에서 누군가 나가면 다음 메시지가 출력된다.
#     "[닉네임]님이 나갔습니다."
#     채팅방에서 닉네임을 변경하는 방법은 다음과 같이 두 가지이다.
#     채팅방을 나간 후, 새로운 닉네임으로 다시 들어간다.
#     채팅방에서 닉네임을 변경한다.
#     닉네임을 변경할 때는 기존에 채팅방에 출력되어 있던 메시지의 닉네임도 전부 변경된다.
#     예를 들어, 채팅방에 "Muzi"와 "Prodo"라는 닉네임을 사용하는 사람이 순서대로 들어오면 채팅방에는 다음과 같이 메시지가 출력된다.
#     "Muzi님이 들어왔습니다."
#     "Prodo님이 들어왔습니다."
#     채팅방에 있던 사람이 나가면 채팅방에는 다음과 같이 메시지가 남는다.
#
#     url : https://programmers.co.kr/learn/courses/30/lessons/42888
#     설명 : hashmap을 이용한 풀이
# --------------------------------------
# space complexity : O(n) -> 추가 메모리 사용 없음
# time complexity : O(n) -> sum(list)할때 루프
from collections import defaultdict

engToKorean = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}

def solution(record):
    id_to_name = defaultdict(str)
    answer = []

    for i in record:
        temp = i.split(" ")
        action, uid = temp[0], temp[1]

        if action != "Change":
            answer.append([action, uid])

        if action != "Leave":
            name = temp[2]
            id_to_name[uid] = name

    return [id_to_name[i[1]] + engToKorean[i[0]] for i in answer]