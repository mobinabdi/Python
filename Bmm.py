# def Maghsom(x,y):
#     M1= []
#     M2=[]
#     numbers =[]
#     for i in range(1,x+1):
#         if(x % i ==0):
#             M1.append(i)
#     for j in range(1,y+1):
#         if(y%j ==0):
#             M2.append(j)
#     for i in M1:
#         if i in M2:
#             numbers.append(i)
#     print(max(numbers))
#
# Maghsom(7,21)

def Maghsom(x, y):
    result = 1
    i = 2


    while i <= x and i <= y:

        if x % i == 0 and y % i == 0:
            result *= i

            x //= i
            y //= i

        else:
            i += 1 

    return result


print(Maghsom(12, 18))
print("test")
