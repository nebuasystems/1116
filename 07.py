#키보드에서 5개의 정수를 받아 리스트 저장, 평균

numbers = []
sum = 0

for c in range(5):
    n = input('>')
    numbers.append(n)
    sum += int(n)

print(numbers)
print(sum/5)
