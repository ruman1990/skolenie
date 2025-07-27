import pandas as pd

moje_cisla = [4, 7, 8]
moj_series = pd.Series(moje_cisla, index=[2, 3, 4])
print(moj_series[1])