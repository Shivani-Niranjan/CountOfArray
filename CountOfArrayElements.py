array = list(map(int,input().strip().split()))
max = 0
count = 0
for i in array:
    if i > max:
        max = i
        count = 1
    elif i == max:
        count+=1
print(len(array)-count)