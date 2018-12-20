#파이썬 dictionary 활용기초
# dict = {
#     "대전": 23,
#     "서울": 30,
#     "구미": 20
# }

# list = [1, 231, "12314"]
# print(len(list))

#1. 평균을 구하세요.

# scores = {
#     "국어": 87,
#     "영어": 92,
#     "수학": 40
# }

# total_score = 0

# for score in scores.values():
#     total_score += score
# averge_score = total_score / len(scores)
# print(averge_score)

# total_score = sum(scores.values())
# averge_score = total_score/len(scores)
# print(averge_score)

#2. 반 평균을 구하기

# scores = {
#     "철수" : {
#         "수학": 80,
#         "국어": 90,
#         "음악": 100
#     },
#     "영희": {
#         "수학": 70,
#         "국어": 60,
#         "음악": 50
#     }
# }

# print(scores.values())

# total_score = 0
# total_score1 = 0

# for name in scores.values():
#     for score in name.values():
#         total_score1 += score / len(name)
#     total_score += total_score1
#     total_score1 = 0
#     print(total_score)

# averge_score = total_score / len(scores)
# print(averge_score)

#강사님 풀이법
# total_score = 0
# count = 0
# for person_score in scores.values():
#     for indivisual_score in person_score.values():
#         total_score += indivisual_score
#         count += 1

# averge_score = total_score / count
# print(averge_score)

# 3 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# scores = {
#     "국어": 87,
#     "영어": 92,
#     "수학": 40
# }

# for key, value in scores.items():
#     print(key)
#     print(value)

cities = {
    "서울": [-6, -10, -5],
    "대전": [-3, -5, 2],
    "광주": [0, -2, 10],
    "부산": [2, -2, 9]
}

hot = 0
cold = 0
hot_city = ""
cold_city = ""
count = 0

for name, temp in cities.items():
    #name = "서울"
    #temp = [-6, -10, -5]
    if count == 0:
        hot = max(temp)
        cold = min(temp)
        hot_city = name
        cold_city = name
    else:
        #최저온도가 cold 보다 더 추우면, cold에 넣고
        if min(temp) < cold:
            cold = min(temp)
            cold_city = name
        #최rh온도가 hot 보다 더 더우면, hot에 넣고
        if max(temp) > hot:
            hot = max(temp)
            hot_city = name
    count += 1

print(f'{hot_city}, {cold_city}')


    

    
    
       
  
     

    
    
