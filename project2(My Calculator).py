#To calculate all the given numbers using a calculator
print('Welcome to My Calculator')
sum=0
i=0
while(True):
    value=input('Enter the price of the item or press q to quit:\n')
    if(value!='q'):
        sum=sum+int(value)
        print(f'The total till now is: {sum}')
        i=i+1
    else:
        print('Your Reciept')
        print(f'U have purchased total {i} elements and the total price is: {sum}')
        print('Thanks for using My Calculator')
        break