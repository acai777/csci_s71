import sys

if len(sys.argv) != 2:
    print("Please only insert one argument (your name)")
    quit()
else:
    print("Hello, " + sys.argv[1] + "!")