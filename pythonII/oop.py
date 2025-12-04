import re

txt = "The rain in Spain"
x = re.split("\s", txt)
# alebo
x = re.split("\s", txt, 1)  # iba prvý deliteľ