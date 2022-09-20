#   -------  FAULTY CALCULATOR  -------

# Enter first element
n1 = int(input("Enter 1st number:"))
# Enter operator
opera=input("Enter operator :")
# Enter Second operator
n2 = int(input("Enter 2nd number:"))

#   -------  CALCULATE EVERYTHING EXCEPT THE FOLLOWINGS  -------
# 45 * 3 Produce 555
# 56 + 9 Produce 77
# 56 / 6 Produce 4

if(n1 == 45 and opera =='*' and n2 == 3):
    result=555
elif(n1 == 56 and opera =='+' and n2 == 9):
    result=77
elif(n1 == 56 and opera =='/' and n2 == 6):
    result=4

elif (opera == '*'):
    result = n1 * n2
elif (opera == '/'):
    result = n1 / n2
elif (opera == '+'):
    result = n1 + n2
elif (opera == '-'):
    result = n1 - n2

print("Result is =",result)

