from charset_normalizer import from_path
r = from_path('demofile.txt').best()
print(r.encoding)

# treba instalovat python -m pip install charset_normalizer