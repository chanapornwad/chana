n = list(map(int, input().split()))
x = []
for i in n :
    if i%2 == 0 :
        x.append(i)

output=sum(x)
print(output)