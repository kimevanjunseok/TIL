# My solution

def solution(a, b):
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    weeks = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    day = sum(days[:a-1]) + b
    return weeks[day % 7]

