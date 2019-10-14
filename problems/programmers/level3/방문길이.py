def solution(dirs):
    x, y = 5, 5
    save = 0
    route = dict()
    for i in dirs:
        if i == "U":
            if y+1 <= 10:
                if ((x, y, x, y+1) not in route and (x, y+1, x, y) not in route):
                    route[(x, y, x, y+1)] = True 
                    route[(x, y+1, x, y)] = True
                    save += 1 
                y += 1
        elif i == "D":
            if 0 <= y-1:
                if ((x, y, x, y-1) not in route and (x, y-1, x, y) not in route):
                    route[(x, y, x, y-1)] = True 
                    route[(x, y-1, x, y)] = True
                    save += 1
                y += -1
        elif i == "L":
            if 0 <= x-1:
                if ((x, y, x-1, y) not in route and (x-1, y, x, y) not in route):
                    route[(x, y, x-1, y)] = True 
                    route[(x-1, y, x, y)] = True
                    save += 1
                x += -1
        elif i == "R":
            if x+1 <= 10:
                if ((x, y, x+1, y) not in route and (x+1, y, x, y) not in route):
                    route[(x, y, x+1, y)] = True 
                    route[(x+1, y, x, y)] = True
                    save += 1
                x += 1

    return save

if __name__ == "__main__":
    dirs = ["ULURRDLLU", "LULLLLLLU	"]
    for i in range(2):
        print(solution(dirs[i]))