import cv2
import threading
from queue import Queue
from user import User
from lift_GUI import *
from time import sleep
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

def display(in_q,out_q):
    # Create a VideoCapture object and read from input file
    cap = cv2.VideoCapture('white background.mp4')
    # Check if camera opened successfully
    if (cap.isOpened() == False):
        print("Error opening video  file")
    frame_counter = 0
    # Read until video is completed
    out_q.put(True)
    while (cap.isOpened()):

        # Capture frame-by-frame
        ret, frame = cap.read()
        frame_counter += 1
        if ret == True:
            # If the last frame is reached, reset the capture and the frame_counter
            if frame_counter == cap.get(cv2.CAP_PROP_FRAME_COUNT):
                frame_counter = 0  # Or whatever as long as it is the same as next line
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

            #frame = frame[:600,:1024,:]
            # Display the resulting frame
            cv2.namedWindow('Welcome', cv2.WND_PROP_FULLSCREEN)
            #cv2.setWindowProperty('Welcome', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.imshow('Welcome', frame)

            # Press Q on keyboard to  exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

            if not in_q.empty():
                cap.release()
                out_q.put(False)
                # Closes all the frames
                cv2.destroyAllWindows()
                user = User(in_q.get())
                if user.type=="admin":
                    print(user)
                    a=input("hello type something")
                cap = cv2.VideoCapture('white background.mp4')
                if user.type=="user":
                    user_GUI(user.name)
                out_q.put(True)
        # Break the loop
        else:
            break

    # When everything done, release
    # the video capture object
    cap.release()

    # Closes all the frames
    cv2.destroyAllWindows()


def take_input(out_q,in_q):
    reader = SimpleMFRC522()
    while(True):
        if not in_q.empty() and in_q.get()==True:
            try:
                print("accepting")
                u,i=reader.read()
                sleep(.5)
                print(u,i)
            
            finally:
                GPIO.cleanup()
            out_q.put(i)
        else:
            print("not accepting")
        sleep(.3)

q = Queue()
q1 = Queue()
th_hw = threading.Thread(target = take_input,args=(q,q1))
th_sw = threading.Thread(target= display,args=(q,q1))
th_hw.start()
th_sw.start()