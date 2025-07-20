## Argumenty príkazového riadku v Pythone

Python programy môžu prijímať argumenty z príkazového riadku. Premenná <code>sys.argv</code>
obsahuje zoznam argumentov príkazového riadku, ktoré boli odovzdané Python skriptu. <code>argv\[0]</code> je názov skriptu; zvyšné prvky sú argumenty odovzdané skriptu.

```python
# command_line_arguments.py

import sys

print("Názov skriptu:", sys.argv[0])
print("Argumenty:", end=" ")

for arg in sys.argv[1:]:
    print(arg, end=" ")

print()
```

Tento príklad vypíše argumenty príkazového riadku, ktoré boli odovzdané skriptu.

```python
import sys
```

Importujeme modul <code>sys</code>, ktorý obsahuje premennú <code>argv</code>.

```python
print("Názov skriptu:", sys.argv[0])
```

Vypíše sa názov programu.

```python
for arg in sys.argv[1:]:
    print(arg, end=" ")
```

Prechádzame zoznam argumentov uložených v <code>sys.argv</code> a
vypisujeme ich do konzoly. Pomocou možnosti <code>end</code> pridáme na koniec medzeru
namiesto nového riadku.

```python
print()
```

Na konci sa do konzoly vytlačí nový riadok.

```
$ ./command_line_arguments.py 1 2 3
Názov skriptu: ./command_line_arguments.py
Argumenty: 1 2 3 
```
