#Tipi PRIMITIVI ( di base che un linguaggio contiene)

num : int  = 2

num_f : float = 2.8

num_str : str = "2.8"

booleano : bool = False

# Stampo Int
print(type(num))

# Stampo float
print(type(num_f))

# Stampo stringa
print(type(num_str))

# Stampo booleano
print(type(booleano))

#come viene compilato un programma python
# 1. file.py --> compilatore
# 2. bytcode --> viene eseguito pvm (python virtual machine)
# 3. per richiamare il bytcode usare il comando dis (disassembla)

# come funziona la memoria
# 1. due spazi di memoria principali 
#  1.1 stack
#  1.2 heap

import sys 

a : int = 500
print(id(a))

b : int = a
print(id(b))

#print(sys.getrefcount(500))
#print(sys.version)
#print(dir(sys))
#print(sys.platform)
#print(help(sys))

from psutil import cpu_stats

# print(dir(psutil))

# print(psutil.cpu_percent(interval=1))

print(cpu_stats())


### Funzioni Built in
nome: str = "Pippo"

print(len(nome))

int_val: int = 3

print(type(int_val))

float_val: float = float (int_val)
print(type((float_val)))
print(type(float(int_val)))

str_val: str = "30"
print(type(int(str_val)))

codice: str = input("inserire codice di tre cifre dietro la carta:")
print(codice)
print(type(codice))
