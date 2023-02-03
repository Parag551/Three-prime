try:
    num = int(input("Enter a number : "))
    if num>1:
        for i in range(2,num):
            if (i*i) ==num:
                print(num,"is Three prime")
                break
            elif (num % i) == 0:
                print(num,"is not a prime number")
                break
        else:
          print(num,"is a prime number")
    else :
      print("This is not a three prime number")
except ValueError as e:
    print("Please enter a Number")