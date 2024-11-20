print("So you want prime numbers ...")
srange = int(input("From "))
erange = int(input("To "))

print("Prime numbers between", srange, "and", erange, "are:")

for num in range(srange, erange + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)