from utils import *
import cv2
from recognition import *
import time

# drone init
#myDrone = initTello()
print("드론 초기화")

# drone landing
#myDrone.takeoff()
print("드론 이륙")

# time measure
count = 0
now1 = time
mm1 = now1.localtime().tm_min
ss1 = now1.localtime().tm_sec
stop = False

# drone move remember
move = []

while True:
    if stop == True:
        break
    print("인식중")
    condition1 = handRecognition()
    # hand recognition
    if condition1 == 1:
        print("성공")
        while True:
            #myDrone.move_forward(5)
            print("드론 전진 (5센티)")
            move.append("f");
            print("인식중")
            condition2 = handRecognition()
            if condition2 == 0:
                print("인식 실패")
                #myDrone.rotate_clockwise(10)
                move.append("r");
                break
            elif condition2 == 2:
                print("정지")
                stop = True
                break
    elif condition1 == 0:
        #myDrone.rotate_clockwise(10)
        print("드론 회전 (10도)")
        move.append("r");
    elif condition1 == 2:
        print("정지2")
        break

# counting time measure
now2 = time
mm2 = now1.localtime().tm_min
ss2 = now1.localtime().tm_sec

count = (mm2 - mm1) * 60 + (ss2 - ss1)

# score check
print("드론이 쫒아간 시간은 %d초 입니다." %count)

# drone return
while move != []:
    pop = move.pop()
    if pop == "f":
        #myDrone.move_backward(5)
        print("드론 후진 (5센티)")
    elif pop == "r":
        #myDrone.rotate_counter_clockwise(10)
        print("드론 역회전 (10도)")

# game over
print("드론 원위치")