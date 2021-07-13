#!/usr/bin/env python
# coding: utf-8

# In[1]:


numero = int(input('Insira um número.'))
fatorial = numero
contador = 1
while (numero-contador)>1:
    fatorial = fatorial*(numero-contador)
    contador += 1
print('{0}! = {1}'.format(numero,fatorial))


# In[ ]:




