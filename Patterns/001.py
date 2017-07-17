# num = int(input("Enter the value : "))
num = 4
for i in range(1, num +1):
    for j in range(0, num - i):
        print (" "),

    for k in range(0, i):
        print ("*  "),
    print "\n"
