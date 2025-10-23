import locale

# Nastavenie slovenského locale (pre Unix/Linux)
locale.setlocale(locale.LC_ALL, 'sk_SK.UTF-8')

# Formátovanie čísla s oddelovačom tisícov
cislo = 1234567.89
print(locale.format_string("%.2f", cislo, grouping=True))  # napr. '1 234 567,89'


import gettext
_ = gettext.gettext

print(_("Vitajte v aplikácii!"))