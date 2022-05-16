l=[]

while True :
  text = input('Enter a number:')
  if text == 'done' :
    break
  try:
    atext = int(text)
  except:
    print('Invalid input')
    continue
  l.append(atext)
        

l.sort()
a=len(l)
print ("Maximum is",l[a-1])
print ("Minimum is",l[0])
           
    
  