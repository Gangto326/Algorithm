def solution(cards1, cards2, goal):
    answer = "Yes"
    N = len(cards1)
    M = len(cards2)
    card1_index = 0
    card2_index = 0

    for g in goal:
        if card1_index < N and cards1[card1_index] == g:
            card1_index += 1
            
        elif card2_index < M and cards2[card2_index] == g:
            card2_index += 1
        
        else:
            answer = "No"
            break

    return answer