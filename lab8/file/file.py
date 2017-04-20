import sys

try:
        a = open(sys.argv[1],"r")
except:
        print("error")
        exit()

try:
        a = open("file.txt","r")
        count = 1
        for list in a:
            v = list.split() #creates list with splits based off white space for that specific line
            print(v) #print additions
            try:
                total = v[0]+v[1]
                print(total) #print answer
                count += 1
            except:
                print("error" , count) #error at that line/count
