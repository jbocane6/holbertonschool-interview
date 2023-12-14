#!/usr/bin/python3
""" Maria and Ben are playing a game.
Given a set of consecutive integers starting from 1 up to and including n,
they take turns choosing a prime number from the set and removing that number
and its multiples from the set.
The player that cannot make a move loses the game.
They play x rounds of the game, where n may be different for each round.
Assuming Maria always goes first and both players play optimally,
determine who the winner of each game is.

    Prototype: def isWinner(x, nums)
    where x is the number of rounds and nums is an array of n
    Return: name of the player that won the most rounds
    If the winner cannot be determined, return None
    You can assume n and x will not be larger than 10000
    You cannot import any packages in this task
"""


def isWinner(x,nums):
  """prueba"""
  Count_Maria = 0
  Count_Ben = 0

 
  for i in nums:
      if i == 1:
        Count_Ben = Count_Ben + 1
      if i == 2:
        Count_Maria = Count_Maria + 1   
      if i != 1 and i != 2 and type(i) == int: 
        if i is float:
            i = round(i)   
        vector = list(range(1,i+1))
        vector_de_primos = obtener_numeros_primos(i)
        while True:

            fin = analizar_si_quedan_movimientos(vector)
            if fin:

                while True:
                    
                    for elemento_vector in vector:
                        if elemento_vector in vector_de_primos:
                            Maria = elemento_vector
                            break
                    if Maria in vector_de_primos:
                        break
                vector = eliminar_elementos(vector,Maria)
                fin = analizar_si_quedan_movimientos(vector)
                if fin:
                    while True:
                        for elemento_vector in vector:
                            if elemento_vector in vector_de_primos:
                                Ben = elemento_vector
                                break

                        if Ben in vector_de_primos:
                            break
                    
                    vector = eliminar_elementos(vector,Ben)
            
                    fin = analizar_si_quedan_movimientos(vector)
                else:
                    Count_Maria = Count_Maria+1
                    break
            else:
                Count_Ben = Count_Ben + 1
                break

  if Count_Ben > Count_Maria:
    winner = 'Ben'
  if Count_Ben < Count_Maria:
    winner = 'Maria'
  if Count_Ben == Count_Maria:
    winner = 'None'


  return winner

def Verificar_primo_y_existencia(numero):
    """prueba"""
    if numero == 2:  
        indicador2 = True
    else:    
        if numero < 2:  
            indicador2 = False
        else:
            
            for test in list(range(2,numero)): 
                
                if numero % test == 0:
                    indicador2 = False
                    break
                else:
                    indicador2 = True

    
    if  indicador2:
        return True
    else:
        return False

def analizar_si_quedan_movimientos(vector):
    """prueba"""
    for i in vector:
        if Verificar_primo_y_existencia(i):
            movimientos = True
            break
        else:
            movimientos = False
            
    return movimientos

def eliminar_elementos(vector,numero):

    vector.remove(numero)
    for i in vector:
        if i % numero == 0:
            vector.remove(i)

    return vector

def obtener_numeros_primos(n):
  """prueba"""
  if n > 2:
    vector = list(range(2,n+1))
    numero=0
    while True:
        primo = vector[numero]
        vector = [ni for ni in vector if (ni % primo != 0)]  
        vector.insert(numero,primo)
        if primo*2 >= n:
            break
        numero = numero+1
    return vector
