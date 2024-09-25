

def q1():

 print("true")

def q2():

  math = input("Input an integer: ")
  think = int(math)
  compare = think > 5
  print(compare)
  
  

def q3():
  
  letters = input("Input the letter a")
  show = letters == 'a'
  print(show)

def q4():
  vocabulary = input("Input a word ealier in the dictionary than google: ")
  search = vocabulary < 'google'
  print(search)

def q5():
  num1 = int(input("Input an integer: "))
  num2 = int(input("Input another integer: "))
  mathanswer = num1 * num2 > 40
  print("Your numbers multiplied together are greater than 40:", mathanswer)


#Do edit the code below
#Comment the lines below when running your tests

q1()
q2()
q3()
q4()
q5()
