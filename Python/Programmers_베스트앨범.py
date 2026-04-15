def solution(genres, plays):
    N = len(plays)
    
    genre_dict = {}
    for i in range(N):
        if genres[i] in genre_dict:
            genre_dict[genres[i]][0] += plays[i]
            genre_dict[genres[i]][1].append((plays[i], i))
        
        else:
            genre_dict[genres[i]] = [plays[i], [(plays[i], i)]]
    
    answer = []
    for c, value in sorted(genre_dict.values(), key = lambda x: x[0], reverse = True):
        value.sort(key = lambda x: (x[0], -x[1]))
        
        for i in range(2):
            if value:
                answer.append(value.pop()[1])
    
    return answer