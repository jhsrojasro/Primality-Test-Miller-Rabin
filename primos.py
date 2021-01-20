# -*- coding: utf-8 -*-
"""LP Tarea1 .ipynb"""

#Autor: Jhon Sebastian Rojas Rodriguez
#Tarea 1 LP02 2020 II
import random
import math

def esTestigo(a, n):
  t = 0
  u = n - 1
  while u % 2 == 0:
    u = u//2
    t += 1
  x = pow(a, int(u), n)
  if(x == 1 or x == n-1):
    return True
  for i in range(1, t-1):
    x = pow(x, 2, n)
    if x == n-1:
      return True
    if x == 1:
      return False
  x = pow(x, 2, n)
  return x == n - 1

def test_miller_rabin(n, s):
  for j in range(s):
    a = random.randint(1, n - 1)
    if not esTestigo(a,n):
      return False
  return True

def esPrimo(n, s = 50):
  return (True, 1/(1+2 ** -s * math.log(n-1))) if test_miller_rabin(n, s) else (False, 1)

def generarPrimo_digitos(d):
  start = 10 ** (d-1)
  end = 10 ** d - 1
  p = False
  while not p:
    n = random.randint(start, end)
    while n % 2 == 0 or n % 3 == 0 or n == 1:
      n = random.randint(start, end)
    p, prob = esPrimo(n)
  return n, prob



