# Exercise 2 - Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result

var1 = {"45*3":555, "55+9":77, "56/6":4}
var2 = ["+","-","*","/"]

print(var1,var2)
print("enter two numbers:")
inp1 = input()
inp2 = input()
inch = int(input("Make ur choice:1.+ 2.- 3.* 4./"))

#print(inp1+var2[3]+inp2)
print(var1.get("55/6"))
if inch == 1:
    if (inp1+var2[0]+inp2) in var1.keys():
        print(var1.get((inp1+var2[0]+inp2)))
    else:
        print(int(inp1) + int(inp2))
elif inch == 3:
    if (inp1+var2[2]+inp2) in var1.keys():
        print(var1.get((inp1+var2[2]+inp2)))
    else:
        print(int(inp1) * int(inp2))
elif inch == 4:
    if (inp1+var2[3]+inp2) in var1.keys():
        print(var1.get((inp1+var2[3]+inp2)))
    else:
        print(int(inp1) / int(inp2))

else:
    print(int(inp1) - int(inp2))
