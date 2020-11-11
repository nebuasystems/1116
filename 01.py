#1. 키보드 입력치가 3의 배수?

number = input('수를 입력하세요:')
i_number = int(number)

if i_number%3 == 0:
    print('3의 배수 ok')

else:
    print('3의 배수 아님')
