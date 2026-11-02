# A program that reads an amount from the keyboard. 
# Then, it calculates and prints both the amount and its VAT (23%).

amount = float(input('Enter amount: '))
vat = amount * 0.23

print(f'Amount  : {amount:.2f}')
print(f'VAT 23% : {vat:.2f}')