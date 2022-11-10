input_list=input("input a list").split(" ")
counter=dict()
kws=set(input_list)
for keyword in kws:
    kw=keyword
    counter[kw]=input_list.count(keyword)
print(counter)
if all(counter)==1:
    print("true")
else:
    print("false")