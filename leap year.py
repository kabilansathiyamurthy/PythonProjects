def is_leap(year):
    leap = False
    if year%4 == 0:
        print("True")
    else:
        print("False")
is_leap(year)
year = int(input())
print(is_leap(year))
