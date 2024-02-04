ls = eval(input())
#完整传入单片机的scan信息
for i in ls:
    print(str(i[0]).encode())
    print(str(i[1]).encode())
    for l in range(2,len(i)):
        print(i[l],end=" ")