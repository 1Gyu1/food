import random
print("오늘 점심 머먹지")

#메뉴 리스트를 만들어 보자
menu = ["짜장면","짬뽕","라면","김밥","돈가스"]

print(menu)

for i in menu:
    print(i)

print("당신의 취향을 분석한 결과 이 중에서 당신이 제일 좋아하는 메뉴는")

a = random.randint(0,4)
print("{} 입니다".format(menu[a])) 
#