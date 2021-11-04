
from tkinter import *
import os

print (os.path.dirname(os.path.realpath(__file__)) ) #프로젝트 소스코드 파일 경로 출력

root=Tk()
root.title("오늘의 추천 메뉴")
root.geometry("1024x840")
root.resizable(1, 1)

#imgPath = r"라면.gif"
image=PhotoImage(file="라면.jpg") #PhotoImage를 통한 이미지 지정
label=Label(root, image=image) #라벨 생성, 라벨에는 앞서 선언한 이미지가 들어감.
label.pack()

root.mainloop()

