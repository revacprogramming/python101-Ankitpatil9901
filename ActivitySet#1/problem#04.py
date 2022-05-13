h=float(input("Enter hours = "))
r=float(input("Enter rate = "))

if(h>40):
  overtime=(h-40)*(r*1.5)
  pay=(40*r)+overtime
else:
  pay=(h*r)
print("pay =" pay)