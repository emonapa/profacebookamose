
help_array_carrying_ascii = list(range(0, 255))
count_array = [0]*255
helpbool = True
with open('dummytext.txt') as f:
  while helpbool:

    try:
        c = f.read(1)

    except:
        c = '-1'
        f.read(1)


    if not len(c):
      f.close()
      helpbool = False

    if helpbool:
        if (c != '-1') and (ord(c) <= 255):
                count_array[ord(c)] +=1

      

print(count_array)
"""
Tohle je jenom pythonacky bubble sort
"""
n = len(count_array)

for i in range(n):

    for j in range(n-1):

        if count_array[j] < count_array[j + 1]:

            temp0 = count_array[j]
            temp1 = help_array_carrying_ascii[j]
            
            count_array[j] = count_array[j+1]
            help_array_carrying_ascii[j] = help_array_carrying_ascii[j+1]

            count_array[j + 1] = temp0
            help_array_carrying_ascii[j+1] = temp1

for k in range(len(count_array)):
    print("Znak " + chr(help_array_carrying_ascii[k]) + " hodnota dekadicky " + str(help_array_carrying_ascii[k]) + " cetnost vyskytu " + str(count_array[k]))    
