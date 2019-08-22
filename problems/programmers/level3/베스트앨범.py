def solution(genres, plays):
    dict_list = dict()
    dict_score = dict()
    list_score = []
    result = []
    for i in range(len(genres)):
        if not dict_list.get(genres[i]):
            dict_list[genres[i]] = []
            dict_score[genres[i]] = 0
        dict_list[genres[i]].append([i, plays[i]])
        dict_score[genres[i]] += plays[i]
    
    for keys in dict_list.keys():
        dict_list[keys].sort(key=lambda x: x[1],  reverse=True)
    
    for key, item in dict_score.items():
        list_score.append([key, item])
    list_score.sort(key=lambda x: x[1], reverse=True)

    for i in list_score:
        if len(dict_list[i[0]]) == 1:
            result.append(dict_list[i[0]][0][0])
        else:
            for j in range(2):
                result.append(dict_list[i[0]][j][0])

    return result

if __name__ == "__main__":
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]
    print(solution(genres, plays))