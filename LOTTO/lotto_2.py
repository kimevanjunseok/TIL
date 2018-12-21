import random
import requests
import json
from pprint import pprint

# 0. random으로 로또번호를 생성합니다.
# 1. api를 통해 우승번호를 가져옵니다.
# 2. 0번과 1번을 비교하여 나의 등수를 알려준다.
#------------------------------------------
# 1. url 요청 보내서 정보를 가져옵니다.
#     -json으로 받는다.(딕셔너리로 접근 가능)
# 2. api의 당첨번호와 보너스 번호를 저장하고.
# 3.뽑은게 몇등인지 하는거 뽑으세여, 몇번만에 되는지

url ="https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
res = requests.get(url)
lotto = res.json()
num = []
number = set(num)
lo_num = []
for i in range(1, 7):
    lo_num.append(lotto[f'drwtNo{i}'])

count = 0
set_lo_num = set(lo_num)

while True:
    num = random.sample(range(1, 46), 6)
    count += 1
    matched = len(set(lo_num) & set(num))
    if matched == 6:
        print(f"1등입니다. 횟수 : {count}")
        break
    elif matched == 5:
        set_lo_num1 = set_lo_num | {lotto['bnusNo']}
        if matched == 6:
            print(f"2등입니다. 횟수 : {count}")
        else:
            print(f"3등입니다. 횟수 : {count}")
    elif matched == 4:
        print(f"4등입니다. 횟수 : {count}")
    elif matched == 3:
        print(f"5등입니다. 횟수 : {count}")
    else:
        print(f"꽝입니다. 횟수 : {count}")

#강사님 로또 
# url ="https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
# res = requests.get(url)
# lotto = res.json()
# lo_num = []
# for i in range(1, 7):
#     lo_num.append(lotto[f'drwtNo{i}'])

# bonus = lotto['bnusNo']
# print("이번 주 당첨번호 : " + str(lo_num))
# print("보너스 번호 : " + str(bonus))

# count = 0
# while True:
#     count += 1
#     my_number = random.sample(range(1, 46), 6)
#     matched = len(set(lo_num) & set(my_number))
#     if matched == 6:
#         print("1등")
#         print(count, "번만에 당첨")
#         print(count*1000, "원 써서 먹었습니다.")
#         break
#     elif matched == 5:
#         if bonus in my_number:
#             print("2등")
#         else:
#             print("3등")
#     elif matched == 4:
#         print("4등")
#     elif matched == 3:
#         print("5등")
#     else:
#         print("응 안돼")