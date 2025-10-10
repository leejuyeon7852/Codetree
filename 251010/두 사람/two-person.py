age_f, gender_f = input().split()
age_s, gender_s = input().split()

age_f = int(age_f)
age_s = int(age_s)

if gender_f == 'M' and age_f >= 19:
    print(1)
elif gender_s == 'M' and age_s >= 19:
    print(1)
else:
    print(0)