# with open("new.txt", "w", encoding = 'utf-8') as f:
#     for i in range(1, 6):
#         data = "{}입니다.\t".format(i)
#         f.write(data)

# with open("new.txt", "w", encoding = 'utf-8') as f:
#     for i in range(1, 6):
#         data = f'{i}입니다.\t'
#         f.write(data)

# f = open("new.txt", "w", encoding = 'utf-8')
# for i in range(1,4):
#     data = f'{i}입니다.\t'
#     f.write(data)
# f.close()

f = open("new.txt", "w", encoding = 'utf-8')
for i in range(1, 6):
    data = '{}입니다.\t'.format(i)
    f.write(data)
f.close()