def linearSearch(list, search_ele):
    for ind in range(0, len(list)):
        if (list[ind]== search_ele):
            return ind

    else:
        return -1
ele = int(input('enter element to find:'))
list =[45,37,81,77,53,34,26,82]
res=linearSearch(list,ele)
if(res==-1):
    print(f'{ele} is present in index{res}')
else:
    print(f'{ele} is not present in the list')
    

