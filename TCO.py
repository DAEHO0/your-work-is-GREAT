num = input('TCO는 몇 명입니까?(입력값 범위는 3 ~ 6 입니다):  ')

if '1' <= num <= '2':
    print(f'TCO는 {num}명 입니다, {num}명으론 무리입니다.')
    print('다시 입력해주세요.')
    
elif num == '3':
    print(f'TCO는 {num}명 입니다.')
    print('TCO 이름을 입력해주세요.')
    TCO1 = input('TCO1:  ')
    print(f'TCO1은 {TCO1} 입니다.')
    TCO2 = input('TCO2:  ')
    print(f'TCO2은 {TCO2} 입니다.')
    TCO3 = input('TCO3:  ')
    print(f'TCO3은 {TCO3} 입니다.')
    tco = [TCO1, TCO2, TCO3]
    
elif num == '4':
    print(f'TCO는 {num}명 입니다.')
    print('TCO 이름을 입력해주세요.')
    TCO1 = input('TCO1:  ')
    print(f'TCO1은 {TCO1} 입니다.')
    TCO2 = input('TCO2:  ')
    print(f'TCO2은 {TCO2} 입니다.')
    TCO3 = input('TCO3:  ')
    print(f'TCO3은 {TCO3} 입니다.')
    TCO4 = input('TCO4:  ')
    print(f'TCO4은 {TCO4} 입니다.')
    tco = [TCO1, TCO2, TCO3, TCO4]
    
elif num == '5':
    print(f'TCO는 {num}명 입니다.')
    print('TCO 이름을 입력해주세요.')
    TCO1 = input('TCO1:  ')
    print(f'TCO1은 {TCO1} 입니다.')
    TCO2 = input('TCO2:  ')
    print(f'TCO2은 {TCO2} 입니다.')
    TCO3 = input('TCO3:  ')
    print(f'TCO3은 {TCO3} 입니다.')
    TCO4 = input('TCO4:  ')
    print(f'TCO4은 {TCO3} 입니다.')
    TCO5 = input('TCO5:  ')
    print(f'TCO5은 {TCO5} 입니다.')
    tco = [TCO1, TCO2, TCO3, TCO4, TCO5]
    
elif num == '6':
    print(f'TCO는 {num}명 입니다.')
    print('TCO 이름을 입력해주세요.')
    TCO1 = input('TCO1:  ')
    print(f'TCO1은 {TCO1} 입니다.')
    TCO2 = input('TCO2:  ')
    print(f'TCO2은 {TCO2} 입니다.')
    TCO3 = input('TCO3:  ')
    print(f'TCO3은 {TCO3} 입니다.')
    TCO4 = input('TCO4:  ')
    print(f'TCO4은 {TCO3} 입니다.')
    TCO5 = input('TCO5:  ')
    print(f'TCO5은 {TCO5} 입니다.')
    TCO6 = input('TCO6:  ')
    print(f'TCO6은 {TCO6} 입니다.')
    tco = [TCO1, TCO2, TCO3, TCO4, TCO5, TCO6]
    
else:
    print('입력 값 범위를 초과했습니다.')