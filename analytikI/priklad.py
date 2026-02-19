import pandas as pd

moje_cisla = [4, 7, 8]
moj_series = pd.Series(moje_cisla, index=["a", "b", "c"])
print(moj_series[0])