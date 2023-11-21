from getchar import Getchar #getchar.py->Getchar클래스 import
import serial
                               #timeout : 1초~~
sp = serial.Serial('COM4',9600,timeout = 1) #시리얼 포트 생성자

kb = Getchar()   #kb : 클래스 객체
key = ''

while key!='Q':
    key = kb.getch()    #kb = Getchar클래스 (키보드 값을 리턴)
    if key == '.':
        sp.write('.'.encode())    #시리얼 포트로 송신
    elif key == ',':
        sp.write(','.encode())    #시리얼 포트로 송신
    elif key == '1':
        sp.write('1'.encode()) 
    elif key == '2':
        sp.write('2'.encode()) 
    elif key == '3':
        sp.write('3'.encode()) 
    else:
        pass
        