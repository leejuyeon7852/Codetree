age_f, gender_f = input().split()
age_s, gender_s = input().split()

age_f = int(age_f)
age_s = int(age_s)

if (age_f >= 19 or age_s >= 19) and (gender_f == 'M' or gender_s == 'M'):
    print(1)
else:
    print(0)