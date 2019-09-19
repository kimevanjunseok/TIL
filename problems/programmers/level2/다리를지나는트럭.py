def solution(bridge_length, weight, truck_weights):
    sums = truck_weights[0]
    q = [[truck_weights.pop(0), 1, 1]]

    while q:
        n = len(q)
        for _ in range(n):
            x, y, z = q.pop(0)
            if y == bridge_length:
                sums -= x
            else:
                q.append([x, y+1, z+1])

        if truck_weights and sums + truck_weights[0] <= weight:
            sums += truck_weights[0]
            q.append([truck_weights.pop(0), 1, z+1])

    return z + 1

if __name__ == "__main__":
    bridge_length = [2, 100, 100]
    weight = [10, 100, 100]
    truck_weights = [[7,4,5,6], [10], [10,10,10,10,10,10,10,10,10,10]]
    for i in range(3):
        print(solution(bridge_length[i], weight[i], truck_weights[i]))