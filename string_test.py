# python 과거
#'일은 영어로 %s, 이는 영어로 %s' % ('one', 'two')

# pyformat
#'{} {}'.format('one', 'two')

name = '김준석'
e_name = 'Evan'
print('안녕하세요. 저는 {}입니다. My name is {}'.format(name, e_name))
print('안녕하세요. 저는 {1}입니다. My name is {0}'.format(name, e_name))
print('안녕하세요. 저는 {1}입니다. My name is {1}'.format(name, e_name))

# f-string python 3.6
print(f'안녕하세요. 저는 {name}입니다. My name is {e_name}')
print(f'안녕하세요. 저는 {e_name}입니다. My name is {name}')

print("안녕하세요. " + name + "입니다.")

import random
a = list(range(1,46))
b = random.sample(a, 6)
print(f'오늘의 행운의 번호는 {sorted(b)}입니다.') #sorted 사용
print(b)
b.sort() # sort 사용
print(f'오늘의 행운의 번호는 {b}입니다.')

print('오늘의 행운의 번호는 {}입니다.'. format(sorted(b))) #sorted 사용
print(b)
b.sort() # sort 사용
print('오늘의 행운의 번호는 {}입니다.'.format(b))