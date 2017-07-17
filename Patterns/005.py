for i in range(6):
    for j in range(5):
        if i == 0:
            if j == 0 or j == 4:
                print " ",
            else:
                print "*",
        elif i == 3:
            print "*",
        else:
            if j == 0 or j == 4:
                print "*",
            else:
                print " ",

    print "\n"