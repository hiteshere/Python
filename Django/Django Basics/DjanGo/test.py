def patternRun(n):

    for j in range(1, n+1):
        # for checking even row
        if j % 2 == 0:
            # for running over the row for printing required pattern
            for k in range(1, n+1):
                if k == 1 or k == n:
                    # using TRAILING COMMA for continuty of line
                    print "*",
                elif k == (n+1)/2:
                    if j == (n+1)/2:
                        print (n+1)/2,
                    else:
                        print " ",
                else:
                    print " ",
            print "\n"
        # for checking odd row
        if j % 2 != 0:
            # for running over the row for printing required pattern
            for o in range(1, n+1):
                if j == 1 or j == n:
                    if o % 2 != 0:
                        print "#",
                    elif o % 2 == 0:
                        print "*",
                else:
                    if o ==1 or o == n:
                        print "#",
                    else:
                        print " ",
            print "\n"

patternRun(7)