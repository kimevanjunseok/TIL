# f = open("new.txt", "w") #파일 만들고 열고 쓰고
# f.write("Hello !!!")
# f.close()

# with open("new.txt", "w") as f:
#     f.write("HI !!!")

# f = open("new.txt", "r")
# data = f.read()
# print(data)
# f.close()

# with open("new.txt", "r") as f:
#     data = f.read()
#     print(data)

# f = open("new.txt", "w" )

# for i in range(1, 10):
#     data = f'{i}번째 줄입니다.\n'
#     f.write(data)
    
# f.close()

# f = open("new.txt", "w", encoding = 'utf-8')

# for i in range(1, 100):
#     data = '{}번째 줄입니다.\n'.format(i)
#     f.write(data)
    
# f.close()

# with open("new.txt", "w") as f:
#     for i in range(1, 100):
#         data = f'{i}번째 줄입니다.\n'
#         f.write(data)

# menu = ["카레\n", "탕수육\n", "짬뽕\n"]
# f = open("menu.txt", "w", encoding = 'utf-8')
# f.writelines(menu)
# f.close()

menu = ["카레\n", "탕수육\n", "짬뽕\n"]
with open("menu.txt", "w", encoding = 'utf-8') as f:
    f.writelines(menu)