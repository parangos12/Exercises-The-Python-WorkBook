# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 11:28:16 2020

@author: Pedro Arango Sánchez
"""

def reemplazo(string):
  
  s=len(string)
  z=string
  m=string.upper()

  for i in range(s):
    if z[i]==m[i]:
        
        c=z[i]
        z=z.replace(c,"$")
  return z


print(reemplazo("pEqrpOOcccCCC"))