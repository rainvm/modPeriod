n = 5048
for i in range(1,n):
    x = (3**i)  % n
    if x == 1:
        print(i)
        break