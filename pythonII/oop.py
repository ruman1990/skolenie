import re

text = "123"

# Skúsme rôzne prístupy
print("search:", re.search(r"^\s*\d{3}$", text))       # ✅ nájde 123
