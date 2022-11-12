
# put your python code here

myNumber = int(input())

firstDigit = (myNumber // 100)

secondDigit = (myNumber - (firstDigit*100))//10

thirdDigit = (myNumber % 10)

print (firstDigit + secondDigit + thirdDigit)

