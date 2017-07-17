# num = int(input("Enter the value : "))
num = 4
for i in range(0, num):
    for k in range(0, i):
        print ("  "),

    for j in range(0, num - i):
        print (" * "),

    print "\n"
