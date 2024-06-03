#!/usr/bin/env python
# coding: utf-8

# ## Ejercicio descargas

# Python es un lenguaje de propósito general, por lo que podemos desarrollar otros programas,
# aparte de ciencia de datos, que nos permitan montar dashboards, crear APIs o automatizar
# procesos. En este caso vas a automatizar un proceso, en el que tendrás que desarrollar un
# script que ordene todos los archivos de una carpeta, dependiendo de la extensión de los
# mismos.
# 
# 
# El objetivo es ordenar la típica carpeta de cajón desastre donde se nos acumulan archivos de
# todos los formatos como: imágenes, words, presentaciones, excels, ejecutables, zips, etc... Y
# que no vamos a ir viendo archivo a archivo, ordenándolos.... La solución suele ser eliminarlo
# todo. Vamos a intentar no tener que llegar a eso, ordenando los ficheros automáticamente en
# carpetas y revisar las que nos interesen. La típica carpeta donde aplicaríamos este programa es
# la de “Descargas”, donde se suelen acumular muchos archivos temporales.
# 
# 
# Por tanto, **el programa tiene que guardar los archivos de la carpeta “Descargas” (o cualquier
# otra donde acumules mucho archivo temporal) en los siguientes directorios dentro de la
# propia carpeta “Descargas”**:
# - Imagenes
# - Documentos
# - Software
# - Otros
# 
# Cada vez que ejecutes el script, automáticamente se ordenarán todos los archivos en sus
# correspondientes carpetas.
# 

# In[63]:


doc_types = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx')
img_types = ('.jpg', '.jpeg', '.png', '.svg', '.gif')
software_types = ('.exe', '.py','.ipynb')


# ### 1. Crea un programa con el flujo principal y encapsúlalo en funciones.

# In[64]:


import os
import shutil


# In[65]:


CARPETA_KEYNES = os.path.expanduser("c:\\Users\\rafam\\OneDrive\\Documentos\\GitHub\\mi_copia_dsftmayo24semana1.1\\semana 2 y 3\\1_Data_Analysis\\3-Sources\\Archivos\\Practica\\Keynes y el tipo de interés. Hechos acreditativos_files")
CARPETA_IMAGENES = os.path.join(CARPETA_KEYNES, 'Imagenes')
CARPETA_DOCUMENTOS = os.path.join(CARPETA_KEYNES, 'Documentos')
CARPETA_SOFTWARE = os.path.join(CARPETA_KEYNES, 'Software')
CARPETA_OTROS = os.path.join(CARPETA_KEYNES, 'Otros')


# In[66]:


os.makedirs(CARPETA_IMAGENES, exist_ok=True)
os.makedirs(CARPETA_DOCUMENTOS, exist_ok=True)
os.makedirs(CARPETA_SOFTWARE, exist_ok=True)
os.makedirs(CARPETA_OTROS, exist_ok=True)


# In[67]:


def mover_archivo(archivo, destino):
    shutil.move(os.path.join(CARPETA_KEYNES, archivo), os.path.join(destino, archivo))


# In[68]:


for archivo in os.listdir(CARPETA_KEYNES):
    if os.path.isdir(os.path.join(CARPETA_KEYNES, archivo)):
        continue


# In[69]:


extension = os.path.splitext(archivo)[1].lower()


# In[70]:


if extension in img_types:
    mover_archivo(archivo, CARPETA_IMAGENES)
elif extension in doc_types:
    mover_archivo(archivo, CARPETA_DOCUMENTOS)
elif extension in software_types:
    mover_archivo(archivo, CARPETA_SOFTWARE)
else:
    mover_archivo(archivo, CARPETA_OTROS)

print("Archivos ordenados correctamente.")


# In[71]:


cd "c:\\Users\\rafam\\OneDrive\\Documentos\\GitHub\\mi_copia_dsftmayo24semana1.1\\semana 2 y 3\\1_Data_Analysis\\3-Sources\\Archivos\\Practica"


# In[72]:


get_ipython().system(' jupyter nbconvert --to script ejercicio_descargas.ipynb')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ### 2. Crea una clase Fichero en clase.py y un main.py con el programa principal partiendo de esa clase.

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




