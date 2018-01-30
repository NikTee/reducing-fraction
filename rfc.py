x = int (input ())
num = x
den = x
z = 2
count = 0
ar = []
avg1 = 0
i = 0
def wait():
 pause=input ()
def avg ():
 global i
 global avg1
 while i < len(ar) - 1:
  i = i + 1
  avg1 = avg1 + ar[i]
 else:
  avg1 = avg1 /( len(ar) + 1)
  print("Average of all outputs:\n", avg1)
  print("\nInput divided by average of all outputs:\n", x/avg1)
while True:
 if den == 0:
  wait ()
 if num == 0:
  if den == 1:
   avg ()
   print ("\nOutputs in order from", x, "to 1:\n", ar)
  ar.append (count)
  den = den - 1
  num = den
  count = 0
 while den % z == 0 and num % z == 0:
  z = 2
  num = num - 1
  count = count + 1
 else:
  if z > num or z > den:
   z = 2
   num = num - 1
  else:
   z = z + 1
