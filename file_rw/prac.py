# with open("new.txt", "w", encoding = 'utf-8') as f:
#     for i in range(1, 6):
#         data = "{}입니다.\t".format(i)
#         f.write(data)

# with open("new.txt", "w", encoding = 'utf-8') as f:
#     for i in range(1, 11):
#         data = f'{i}입니다.\t'
#         f.write(data)

# f = open("new.txt", "w", encoding = 'utf-8')
# for i in range(1,4):
#     data = f'{i}입니다.\t'
#     f.write(data)
# f.close()

# f = open("new.txt", "w", encoding = 'utf-8')
# for i in range(1, 11):
#     data = '{}입니다.\n'.format(i)
#     f.write(data)
# f.close()

# with open("new.txt", "r", encoding = 'utf-8') as f:
#     line = f.readline()
#     print(line.strip())

with open("new.txt", "r", encoding = 'utf-8') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())
