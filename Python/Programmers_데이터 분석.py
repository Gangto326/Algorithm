def solution(data, ext, val_ext, sort_by):
    data_type = ["code", "date", "maximum", "remain"]
    ext_index = data_type.index(ext)
    sort_index = data_type.index(sort_by)
    
    answer = []
    for i in range(len(data)):
        if data[i][ext_index] <= val_ext:
            answer.append(data[i])
    
    answer.sort(key = lambda x: x[sort_index])
    return answer