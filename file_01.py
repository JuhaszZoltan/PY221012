# nev = input('írd be a neved: ')
# print(f'Szia {nev}!')

# integer - egész szám
a:int = 10
# floating point number - lebegőpontos szám
b:float = 3.1415

print(10 + 3)
print(10 - 3)
print(10 * 3)

print(10 / 3)   # 3.3333....
print(10 // 3)  # 3          (DIV)
print(10 % 3)   # 1          (MOD)

print(2 ** 10)  # 1024
print(16 ** .5) # sqrt(16) -> 4

# string - karakterlánc
c:str = 'cica'

print('kutya' + "ház") # konkatenáció (összefűzés)
print(3 * 'cica ') # 'cica cica cica '

# Boolean - logikai
d:bool = True # False

print(True or False)  # 'VAGY'     T
print(True and False) # 'ÉS'       F
print(not True)       # 'TAGADÁS'  F

# compare (összehasonlító) operátorok

# numerikus alkalmazás:
print(10 > 3)         # T
print(10 >= 3)        # T
print(10 < 3)         # F
print(10 <= 3)

# általános alkalmazás:
print(10 == 3)              # F
print(True == False)        # F
print('macska' == 'kutya')  # F

print(10 != 3)
print(True != False)
print('macska' != 'kutya')

#              T
#         F               T
print(10 <= 3 or 'kutya' != 'macska') # T