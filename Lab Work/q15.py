u = int(input('Enter The Amount Of Units Consumed:'))
s = 'Amount to be paid: '
if u <= 50:
    amt = u*0.50

    print(s,amt)
elif u <= 150 and u > 50:
    amt = (50*0.5) + ((u-50)*0.75)
    print(s,amt)

elif u <= 250 and u > 150:
    amt = (50*0.5) + (100*0.75) + ((u-150)*1.2)
    print(s,amt)

else:
    amt = (50*0.5) + (100*0.75) + (100*1.2) + ((u-250)*1.5)
    print(s,amt)

print('Process Completed')