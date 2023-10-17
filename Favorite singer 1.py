import pandas as pd
n1 = input()
n2 = list(map(int, input().split()))
count = pd.Series(n2).value_counts()
print(max(count))
