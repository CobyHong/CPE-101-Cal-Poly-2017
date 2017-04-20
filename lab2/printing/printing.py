def print_examples():
    n = 2
    m = 4
    f = 42.7
   # place the print calls specified in the lab description below here
    print ("Entered print_examples function./n")
    print ("n:", n) #You have to put parentheses around print strings because this version of python sucks.
    n = 99
    print ("n:", n, "\tm:", m)
    print ("f:", f)

if __name__ == '__main__':
   print_examples()

   #Note to self: Remember the print lines have to be in same indent to get values because python is more whiny than javascript.
