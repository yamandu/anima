#!/usr/bin/env python
# -*- coding: utf-8 -*-
  
import re
   
__all__ = ['validar_cpf', 'validar_cnpj']
   
def validar_cpf(cpf):
    """
    Valida CPFs, retornando apenas a string de n�meros v�lida.
# CPFs errados
    >>> validar_cpf('abcdefghijk')
    False
    >>> validar_cpf('123')
    False
    >>> validar_cpf('')
    False
    >>> validar_cpf(None)
    False
    >>> validar_cpf('12345678900')
    False
  
# CPFs corretos
    >>> validar_cpf('95524361503')
    '95524361503'
    >>> validar_cpf('955.243.615-03')
    '95524361503'
    >>> validar_cpf('  955 243 615 03  ')
    '95524361503'
    """
    cpf = ''.join(re.findall('\d', str(cpf)))
  
    if (not cpf) or (len(cpf) < 11):
        return False
  
    # Pega apenas os 9 primeiros d�gitos do CPF e gera os 2 d�gitos que faltam
    inteiros = map(int, cpf)
    novo = inteiros[:9]
  
    while len(novo) < 11:
       r = sum([(len(novo)+1-i)*v for i,v in enumerate(novo)]) % 11
  
       if r > 1:
           f = 11 - r
       else:
           f = 0
       novo.append(f)
  
      # Se o n�mero gerado coincidir com o n�mero original, � v�lido
    if novo == inteiros:
       return cpf
    return False
  
def validar_cnpj(cnpj):
      """
      Valida CNPJs, retornando apenas a string de n�meros v�lida.
  
      # CNPJs errados
      >>> validar_cnpj('abcdefghijklmn')
      False
      >>> validar_cnpj('123')
      False
      >>> validar_cnpj('')
      False
      >>> validar_cnpj(None)
      False
      >>> validar_cnpj('12345678901234')
      False
      >>> validar_cnpj('11222333000100')
      False
  
      # CNPJs corretos
      >>> validar_cnpj('11222333000181')
      '11222333000181'
      >>> validar_cnpj('11.222.333/0001-81')
      '11222333000181'
      >>> validar_cnpj('  11 222 333 0001 81  ')
      '11222333000181'
      """
      cnpj = ''.join(re.findall('\d', str(cnpj)))
  
      if (not cnpj) or (len(cnpj) < 14):
          return False
  
      # Pega apenas os 12 primeiros d�gitos do CNPJ e gera os 2 d�gitos que faltam
      inteiros = map(int, cnpj)
      novo = inteiros[:12]
  
      prod = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
      while len(novo) < 14:
          r = sum([x*y for (x, y) in zip(novo, prod)]) % 11
          if r > 1:
              f = 11 - r
          else:
              f = 0
          novo.append(f)
          prod.insert(0, 6)
  
      # Se o n�mero gerado coincidir com o n�mero original, � v�lido
      if novo == inteiros:
         return cnpj
      return False
 
if __name__ == "__main__":
    import doctest, sys
    result = doctest.testmod() #verbose=True)
    if result[0] == 0:
        print "OK!"
    else:
        print result