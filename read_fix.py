f = open("pe.txt", "r")
for i in f:
    print("{}".format(i.replace(",", ".")[0:-1]), end=",")
