input_value = int(input("Введите число: "))

roman_numb = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
                 'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
                 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}

res = ''

for letter, value in roman_numb.items():
    while input_value >= value:
        res += letter
        input_value-=value
        
print(res)
