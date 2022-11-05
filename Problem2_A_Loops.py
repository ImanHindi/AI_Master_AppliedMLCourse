while True:
    try:
        input_list=list(input("input a list of integers").split(" "))
        print(input_list)
        break
    except:
        print("your input must be integer numbers")

int_list=[int(i) for i in input_list]
print(int_list)
#return the list of integers that accept the division by 5:
out_list=[i for i in int_list if i%5==0]

print("The integers that accept division by 5 =",out_list)