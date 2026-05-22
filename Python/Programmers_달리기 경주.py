def solution(players, callings):
    index_dict = {}
    
    for i in range(len(players)):
        index_dict[players[i]] = i
    
    for calling in callings:
        index_dict[calling] -= 1
        index_dict[players[index_dict[calling]]] += 1
        players[index_dict[calling] + 1], players[index_dict[calling]] = players[index_dict[calling]], players[index_dict[calling] + 1]
        
    return players