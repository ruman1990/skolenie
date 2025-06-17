## 🧑‍💻 Úlohy na programovanie

#1. Napíš funkciu `multiply(x, y)`, ktorá vráti súčin dvoch čísel.
def multiply(x, y):
    return x * y

print(multiply(3, 4))  # Očakávaný výstup: 12

#2. Napíš funkciu, ktorá vypíše všetky prvky zoznamu odovzdaného ako argument.
def print_list_elements(elements):
    for element in elements:
        print(element)
print_list_elements(["apple", "banana", "cherry"])  # Očakávaný výstup: apple, banana, cherry

#3. Napíš funkciu, ktorá prijme ľubovoľný počet čísel a vráti ich súčet.
def sum_numbers(*args):
    return sum(args)
print(sum_numbers(1, 2, 3, 4))  # Očakávaný výstup: 10


#4. Napíš funkciu, ktorá má predvolený parameter `lang='Python'` a vypíše `'I code in <lang>'`.
def code_in_language(lang='Python'):
    print(f'I code in {lang}')
code_in_language()  # Očakávaný výstup: I code in Python

#5. Napíš rekurzívnu funkciu, ktorá spočíta súčet čísel od `n` po `0`.
def recursive_sum(n):
    if n <= 0:
        return 0
    else:
        return n + recursive_sum(n - 1)
print(recursive_sum(5))  # Očakávaný výstup: 15 (5 + 4 + 3 + 2 + 1 + 0)

#6. Napíš funkciu, ktorá prijíma meno a priezvisko a vráti ich vo formáte `'Priezvisko, Meno'`.
def format_name(first_name, last_name):
    return f'{last_name}, {first_name}'
print(format_name("John", "Doe"))  # Očakávaný výstup: Doe, John

#7. Napíš funkciu, ktorá prijíma zoznam a vráti nový zoznam, kde sú všetky prvky vynásobené dvoma.
def double_elements(elements):
    return [element * 2 for element in elements]
print(double_elements([1, 2, 3, 4]))  # Očakávaný výstup: [2, 4, 6, 8]

#8. Napíš funkciu, ktorá vypíše `'Hello'` bez použitia argumentov.
def say_hello():
    print('Hello')
say_hello()  # Očakávaný výstup: Hello  

#9. Napíš funkciu, ktorá prijíma ľubovoľné `**kwargs` a vráti hodnotu kľúča `'name'`, ak existuje.
def get_name(**kwargs):
    return kwargs.get('name', 'No name provided')
print(get_name(name='Alice'))  # Očakávaný výstup: Alice

#10. Napíš funkciu, ktorá vypíše čísla od 1 do 5 pomocou `for` cyklu.
def print_numbers():
    for i in range(1, 6):
        print(i)
print_numbers()  # Očakávaný výstup: 1, 2, 3, 4, 5
