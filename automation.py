import cv2

count = 0
picname = "pic"+str(count)+".png"
def takephoto():
    videocaptureobject = cv2.VideoCapture(0)
    cam = True
    while(cam == True):
        global picname
        key,frame = videocaptureobject.read()
        cv2.imwrite(picname,frame)
        print("photo clicked")
        cam = False
        global count
        count = count+1
        picname = "pic" + str(count) + ".png"
    videocaptureobject.release()
    cv2.destroyAllWindows()

while(True):
    takephoto()
    inpt = input("Type true if you want to take the picture, else type false")
    print(inpt)
    if(inpt == "False"):
        print("break")
        break