list=[]
while True:
    
    data=input('Enter the Input : ')
    if data == 'done':
        break
    else:
        list.append(data)
        

print(list)
print('The maximum number of list is ',max(list))
print('The minimum number of list is ',min(list))