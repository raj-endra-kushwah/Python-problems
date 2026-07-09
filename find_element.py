size = int(input("Enter size of list : "))
ls=[]
for _ in range(size):
    print("Enter number : ")
    ls.append(int(input()))

target = int(input("Enter number to be found : "))
for i in range(size):
    if ls[i]==target:
        print("Num is present at index : ", i)
        exit()
print("Number not found ! ")
