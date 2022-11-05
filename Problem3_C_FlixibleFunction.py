while True:
    try:
        #let the user to input the list of integers:
        input_list=list(input("input a list of integers").split(" "))
        #convert the list of strings to list of floats:
        int_list = [float(i) for i in input_list]
        print(int_list)
        #let the user to choose the operant L,Large,large,l=Max and S,Small,small,s=Min:
        input_op=input("tpye L to find the max or S to find the min:")[0].upper()

    except:
        print("your input must be numbers")
        continue
    #find the Max or Min value in the list
    if input_op=="L":
        output=max(int_list)
    elif input_op=="S":
        output = min(int_list)
    else:
        output="please check the operator entered and try again."
    #return result to the user:
    print(output)
    status = list(input("press Q to quite or C to  continue"))[0].upper()
    if status=="Q":
        break

