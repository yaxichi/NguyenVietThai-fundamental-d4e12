x=int(input('Mass(kg)'))
y=int(input('Heigt(cm)'))
k=y/100
BMI=x/k**2
print('your BMI is',BMI)
if BMI < 16:
    print('You are severely underweight')
if 16 < BMI < 18.5:
    print('You are underweight')    
if 18.5 < BMI < 25:
    print('You are normal')
if 25 < BMI < 30:
    print('You are over weight')
else:
    print('You are obese')            