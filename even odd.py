even_num=[]
odd_num=[]
for number in range(1,101):
    if number%2 == 0:
        even_num.append(number)
    else:
        odd_num.append(number)
        
print("even numbers:even_num")
print("odd numbers:odd_num")
