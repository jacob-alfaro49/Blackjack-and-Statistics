with open('balance.txt', 'r') as fp:
    data = fp.read()
    typos = "10000"
with open('balance.txt', 'w') as fp:
    fp.write(typos)