def prime_checker(number) :
    is_Prime = True
    if (number == 1 or number == 0) :
        print("It's neither a prime number nor a composite number.")
    else :
        for i in range(2,number):
            if (number%i == 0):
                is_Prime = False
        if is_Prime == True :
            print("It's a prime number.")
        if is_Prime == False :
            print("It's a composite number.")

num=int(input("Enter The number you wish to check!\n"))
prime_checker(number=num)