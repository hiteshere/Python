num = int(input("Enter the value : "))
for i in range(1, num +1):
    for j in range(0, num - i):
        print ("  "),

    for k in range(0, i):
        print ("*  "),
    print "\n"
for i in range(1, num):
    for k in range(0, i):
        print ("  "),

    for j in range(0, num - i):
        print ("*  "),

    print "\n"
