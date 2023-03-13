
import random
n=random.randint(1,50)
print("-------------Guess the number Game----------------")
print("------------Made by Sandeep Maddhehsiya-----------")
print("----------------------Rules-----------------------")
print("----------------You've 9 guesses------------------")


for i in range(9,0,-1):

    b = int(input("Enter the number\n"))
    if b>0:
        if i!=0:
            while (True):
                if b==n:
                    print("congratulation! Your guess is correct")
                    break
                elif b<n:
                    print("Please enter a greater number")

                elif b>n:
                    print("Please enter a smaller number")
                i=i-1
                break

            print("guess Remaining")
            print(i)

            if i==0:
                print("You lose")
    else:
        print("Enter a valid input")
