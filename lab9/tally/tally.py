import sys

try:
    a = open(sys.argv[1],"r")
except:
    print("you suck it no worky")

column = int(sys.argv[2]) #py tally.py test.txt 0
                            #0      #1      #2

def list_columns(column,a): #Grabs numbers in column into list [][]
    sum = []
    for line in a:

        split_line = line.rstrip().split()
        print(split_line)

        try:
            sum.append(split_line[column])
        except:
            print("ERROR: A line is out of range")
    return sum

def answer(sum): #list from list_columns and adds them up. The actual sum part
    final = 0
    for x in sum:
        try:
            final += float(x)
        except:
            print("ERROR: Not a number in a column")
    print(final)

sum = list_columns(column,a)
done = answer(sum)




