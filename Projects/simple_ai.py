import os
p = "Programs supported by me"
print("\n",p.center(70))
l = ['Google chrome','Notepad','Music player','VLC Player','Camera','Calculator','Paint 3D']
j = 1
for i in l:
    print(j,". {}".format(i),sep="",end="     ")
    j += 1
print(end="\n\n")
while True:
    s = input("What can i do for you: ")
    if (("notepad" in s) or ("editor" in s)) and (("run" in s) or ("open" in s) or ("execute" in s)):
        os.system("notepad")
    elif (("run" in s) or ("execute" in s) or ("open" in s)) and (("chrome" in s) or ('browser' in s) or ('google' in s)):
        w = input("Enter URL: ")
        os.system("chrome {}".format(w))
    elif (("stop" in s) or ("close" in s)) or (("off" in s) or ("nothing" in s)):
        print("Ok take care,BYE 😊")
        break
    elif (("vlc" in s) or ("media" in s) or ("player" in s)) and (("run" in s) or ("execute" in s) or ("open" in s) or ("start" in s)):
        os.system("vlc")
    elif (("camera" in s) or ("cam" in s) or ("photo" in s)) and (("run" in s) or ("execute" in s) or ("open" in s) or ("start" in s)):
        os.system("start microsoft.windows.camera:")
    elif (("music" in s) or ("song" in s)) and (("run" in s) or ("play" in s) or ("open" in s) or ("start" in s)):
        os.system("start mswindowsmusic:")
    elif (("calculator" in s) or ("calculate" in s)) and (("run" in s) or ("execute" in s) or ("open" in s) or ("start" in s)):
        os.system("start calculator:")
    elif (("paint" in s) or ("draw" in s)) and (("run" in s) or ("execute" in s) or ("open" in s) or ("start" in s)):
        os.system("start ms-paint:")