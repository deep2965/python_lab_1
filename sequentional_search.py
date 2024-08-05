def sequencial_search(list,target):
    if target in list:
        return list.index(target)
    else:
        return -1
    
elements=[1,3,5,8,10,23,35]
search_value=10
result=sequencial_search(elements,search_value)

if result != -1:
    print(f"value {search_value} found at index {result}")
else:
    print("value is not found in elements list")
