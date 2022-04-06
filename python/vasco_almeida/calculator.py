def calc():
  def single_expression():
   while True:
    print("\n Please, enter the operation you want to solve.\n (If you wish to leave, write 'quit' on the operator option) ")
    while True :
      first_number = float(input(" \n First Number: "))
      operator =  input(" \n Operator: ")
      if operator == "quit":
       print(" \n See you soon :)\n ")
       return 0
      second_number = float(input(" \n Second Number: "))
      if(operator == '+') :
        solution = first_number + second_number
        break
      if(operator == '-') :
        solution = first_number - second_number
        break
      if(operator == '*') :
        solution = first_number * second_number
        break
      if(operator == '/') :
        solution = first_number / second_number
        break
      else:
          print('''\nPlease only choose the operators: '+", '-', '*' or '/' \n''')
    print("\n Solution:", solution, "\n")
 
    
  def expression():

      print(''' 
  ----------Calculator---------- \n
  Please, enter the problem you want to solve. ''')
      expression = input(" \n Matemathical Expression: ")
      solution = "1"
      print("\n Solution:" + solution + '\n')

  print(''' 
  ----------Calculator---------- \n
     Please choose one of the following:\n
      1 - Simple Operation
      2 - Expression (Não Funciona)
      3 - Quit

     ''')
  opcao = input(" Option: ")
  if opcao == '1':
         single_expression()
  if opcao == '2':
         expression()
  if opcao == '3':
        print(" \n See you soon :) \n")
        quit()
    


     


