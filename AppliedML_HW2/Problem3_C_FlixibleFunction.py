def find_min_max(*args,**kwargs): 
    #find the Max or Min value in the list
    #operation=kwargs
    res=[]
    for key in kwargs.keys():
        if kwargs[key][1]=="L":

            res.append(max(kwargs[key][0]))
        elif kwargs[key][1]=="S":
            res.append(min(kwargs[key][0]))

    return res


while True:
    try:
        no_of_lines = 4
        lines = ""
        for i in range(no_of_lines):
            lines += input() + "\n"

        #let the user to input the list of integers:
        input_list=lines.split("\n")[0:4]
        #list1=input_list[0].split(" ")
        op1=input_list[1]
        #list2=input_list[2].split(" ")
        op2 = input_list[3]
        #convert the list of strings to list of floats:
        int_list1 = [float(i) for i in input_list[0].split(" ")]
        int_list2 = [float(i) for i in input_list[2].split(" ")]

        #print(int_list1,int_list2)
        #let the user to choose the operant L,Large,large,l=Max and S,Small,small,s=Min:
        #input_op=input("tpye L to find the max or S to find the min:")[0].upper()

    except:
        print("your input must be numbers")
        continue

    
    #return result to the user:

    output=find_min_max(int_list1=[int_list1,op1],int_list2=[int_list2,op2])
    print(output)
    status = list(input("press Q to quite or C to  continue"))[0].upper()
    if status=="Q":
        break

