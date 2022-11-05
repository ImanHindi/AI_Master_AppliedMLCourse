no_of_lines = 2
lines =[]
try:
    #let the user to input multiple list of integers, convert the list to set find the unique values
    for i in range(no_of_lines):
        input_list=set(input(f"inter list {i+1}").split(" "))
        lines.append(input_list)

except:
    print("please try a gain!")

print(lines)
output=lines[0]
#apply intersection on the all sets entered by the user and find the duplicated keywords:
for n in range(no_of_lines-1):
    output &= lines[n+1]
print("common words",output)