def solution(phone_book):
    phone_book.sort(key=lambda x: len(x))
    for i in range(len(phone_book)-1):
        for j in range(i+1, len(phone_book)):
            if phone_book[i] in phone_book[j][:len(phone_book[i])]:
                return False
    return True