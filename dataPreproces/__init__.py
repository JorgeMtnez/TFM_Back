#!/usr/bin/env python
# coding: utf-8

# # TFM: MAPA DE PELIGROSIDAD

# Lo primero que debemos hacer es descargar los datos desde una pa

# In[48]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[49]:


dataset = pd.read_csv(r'C:\Users\izarag1\Downloads\Crime_Data_from_2020_to_Present.csv')


# In[50]:


# url = 'https://data.lacity.org/api/views/2nrs-mtv8/rows.csv?accessType=DOWNLOAD'

# dataset = pd.read_csv(url)


# Para poder tener un buen conocimiento de nuestros datos debemos saber cual es el significado de cada una de las variables:
#
# -	DR_NO : Division of Records Number: Official file number made up of a 2 digit year, area ID, and 5 digits
# -	Date Rptd : MM/DD/YYYY
# -	DATE OCC : MM/DD/YYYY
# -	TIME OCC : In 24 hour military time.
# -	AREA : The LAPD has 21 Community Police Stations referred to as Geographic Areas within the department. These Geographic Areas are sequentially numbered from 1-21.
# -	AREA NAME : The 21 Geographic Areas or Patrol Divisions are also given a name designation that references a landmark or the surrounding community that it is responsible for. For example 77th Street Division is located at the intersection of South Broadway and 77th Street, serving neighborhoods in South Los Angeles.
# -	Rpt Dist No : A four-digit code that represents a sub-area within a Geographic Area. All crime records reference the "RD" that it occurred in for statistical comparisons. Find LAPD Reporting Districts on the LA City GeoHub at http://geohub.lacity.org/datasets/c4f83909b81d4786aa8ba8a74a4b4db1_4
# -	Part 1-2
# -	Crm Cd : Indicates the crime committed. (Same as Crime Code 1)
# -	Crm Cd Desc : Defines the Crime Code provided.
# -	Mocodes : Modus Operandi: Activities associated with the suspect in commission of the crime.See attached PDF for list of MO Codes in numerical order. https://data.lacity.org/api/views/y8tr-7khq/files/3a967fbd-f210-4857-bc52-60230efe256c?download=true&filename=MO%20CODES%20(numerical%20order).pdf
# -	Vict Age : Two character numeric
# -	Vict Sex : F - Female M - Male X - Unknown
# -	Vict Descent : Descent Code: A - Other Asian B - Black C - Chinese D - Cambodian F - Filipino G - Guamanian H - Hispanic/Latin/Mexican I - American Indian/Alaskan Native J - Japanese K - Korean L - Laotian O - Other P - Pacific Islander S - Samoan U - Hawaiian V - Vietnamese W - White X - Unknown Z - Asian Indian
# -	Premis Cd : The type of structure, vehicle, or location where the crime took place.
# -	Premis Desc : Defines the Premise Code provided.
# -	Weapon Used Cd : The type of weapon used in the crime.
# -	Weapon Desc : Defines the Weapon Used Code provided.
# -	Status : Status of the case. (IC is the default)
# -	Status Desc : Defines the Status Code provided.
# -	Crm Cd 1 : Indicates the crime committed. Crime Code 1 is the primary and most serious one. Crime Code 2, 3, and 4 are respectively less serious offenses. Lower crime class numbers are more serious.
# -	Crm Cd 2 : May contain a code for an additional crime, less serious than Crime Code 1.
# -	Crm Cd 3 : May contain a code for an additional crime, less serious than Crime Code 1.
# -	Crm Cd 4 : May contain a code for an additional crime, less serious than Crime Code 1.
# -	LOCATION : Street address of crime incident rounded to the nearest hundred block to maintain anonymity.
# -	Cross Street : Cross Street of rounded Address
# -	LAT : Latitude
# -	LON : Longtitude
#

# In[51]:


dataset.head(10)


# In[52]:


dataset.info()


# In[53]:


dataset.nunique()


# En una primera aproximación de los datos podemos observar que tenemos 3 variables a examinar:
# - La variable Crdm cd, la cual indica del 1 al 4 el nivel de peligrosidad de los datos, la cual podriamos fusionar, de alguna manera.
# - La variable vict sex tiene 5 valores distintos por lo que deberemos examinar cuales son y por que, ya que solo debería tener dos, hombre y mujer.

# In[54]:


# Lista de columnas en las que deseas aplicar el reemplazo
# columnas_a_modificar = ['Crm Cd 1', 'Crm Cd 2', 'Crm Cd 3', 'Crm Cd 4']

# Función que reemplaza los valores con 1 si tienen valor, y con 0 si no tienen valor
# dataset[columnas_a_modificar] = np.where(dataset[columnas_a_modificar].notnull(), 1, 0)

# Muestra el DataFrame modificado
# print(dataset)


# #### Para tener un mejor conocimiento del dataset podemos analizar los descriptivos

# In[55]:


dataset.describe()


# De esta aproximación podemos concluir las siguientes observaciones:
# - edad de 120 max

# ## Examinamos las posibles variables categóricas (con menos de 10 valores únicos)

# Estas variables son:
# - Vict Sex
# - Part 1-2
# - Status
# - Status Desc
# - Crdm cd 4

# Empezamos estudaindo la variable Vict Sex

# In[56]:


for valor in dataset['Vict Sex'].unique():
    print(valor)


# In[57]:


contador = dataset['Vict Sex'].value_counts()['H']
contador


# In[58]:


dataset.shape


# In[59]:


contador = dataset['Vict Sex'].value_counts()
contador


# In[60]:


contador = dataset['Vict Sex'].isnull().sum()
contador


# In[61]:


# Número de valores distintos por variable
dataset1 = dataset[dataset['Vict Sex'] != 'H']
dataset1.info()


# In[62]:


for valor in dataset1['Vict Sex'].unique():
    print(valor)


# In[63]:


dataset2 = dataset1[dataset1['Vict Sex'] != '-']
dataset2.info()


# In[64]:


for valor in dataset2['Vict Sex'].unique():
    print(valor)


# In[65]:


contador = dataset2['Vict Sex'].isnull().sum()
contador


# In[66]:


contador = dataset2['Vict Sex'].value_counts()
contador


# In[67]:


import plotly.express as px
# Histograma de calificación del productor
fig = px.histogram(dataset2, x="Vict Sex")
fig.show()


# Hemos eliminado los valores H y - ya que su represenatción era mínima, sin embargo, en el caso de X deberemos determinar si está variable será determinante. Pensamos que puede ser interesante dejar este valor porque actualmente el valor 'otros' es visulizado.

# In[68]:


sns.violinplot(x='Vict Sex', y='Vict Age', data=dataset2, palette='viridis')


# 2. Estudiamos la variable Status y Status Desc

# hacer rangos de edad

# In[69]:


for valor in dataset2['Status'].unique():
    print(valor)


# In[70]:


for valor in dataset2['Status Desc'].unique():
    print(valor)


# In[71]:


contador = dataset2['Status'].value_counts()
contador


# In[72]:


contador = dataset2['Status Desc'].value_counts()
contador


# Podemos observar que:
# - Las dos variables tienen exactamente los mismos valores y el mismo número, por lo tanto, se trata de la misma variable
# - Los valores Unknown representan un pocentaje insignificante y podrán ser eliminados

# In[73]:


dataset2 = dataset1[dataset1['Status Desc'] != 'UNK']
dataset2.info()


# In[74]:


dataset3 = dataset2.drop(['Status'],axis=1)


# In[75]:


import plotly.express as px
# Histograma de calificación del productor
fig = px.histogram(dataset3, x="Status Desc")
fig.show()


# 3. Part 1-2:

# In[76]:


for valor in dataset2['Part 1-2'].unique():
    print(valor)


# In[77]:


# Calcula la matriz de correlación
correlation_matrix = dataset3.corr()

# Crea un mapa de correlación utilizando Seaborn
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Mapa de Correlación')
plt.show()


# In[78]:


for valor in dataset2['Crm Cd'].unique():
    print(valor)


# ¿eliminamos crm cd y part 1-2?

# ## Pasar a factor

# In[79]:


# Lista de columnas con menos de 10 valores distintos. Potenciales factores!
dataset3['Vict Sex'] = dataset3['Vict Sex'].astype('category')
dataset3['Status Desc'] = dataset3['Status Desc'].astype('category')


# In[80]:


dataset3.info()
dataset3.describe()


# In[81]:


dataset3.describe(exclude=np.number)


# In[82]:


for valor in dataset2['Premis Desc'].unique():
    print(valor)


# ### Creamos los rangos de edad:

# In[83]:


## AGE (realizamos una variable con 3 rangos de edad y 3 variables con esos mismos rangos)
dataset3['Niño'] = dataset3['Vict Age'].apply(lambda x: 1 if x<=12 else 0)
dataset3['Joven'] = dataset3['Vict Age'].apply(lambda x: 1 if x>12 and x<=26 else 0)
dataset3['Adulto'] = dataset3['Vict Age'].apply(lambda x: 1 if x>26 and x<60 else 0)
dataset3['Mayor de 60'] = dataset3['Vict Age'].apply(lambda x: 1 if x>=60 else 0)
# dataset3['Mayor de 60'] = dataset3['Vict Age'].apply(lambda x: 0 if x<=35 else (1 if x>35 and x<60 else(2)))


# In[84]:


pd.set_option('display.max_columns', None)

dataset3.head()


# ### Valores atípicos

# In[85]:


dataset3.select_dtypes(include=np.number).apply(lambda x: x.skew())


# In[86]:


dataset3[['Crm Cd 4']].nunique()


# In[87]:


dataset['Crm Cd 1'].isnull().sum()


# In[ ]:





# In[88]:


print(dataset3['Crm Cd 1'].value_counts(),
dataset3['Crm Cd 2'].value_counts(),
dataset3['Crm Cd 3'].value_counts(),
dataset3['Crm Cd 4'].value_counts())


# In[89]:


dataset_prueba= dataset3[['Crm Cd','Crm Cd Desc']]
dataset_prueba


# In[90]:


dataset_ordenado = dataset_prueba.sort_values(by='Crm Cd', ascending=True)


# In[91]:


dataset_ordenado


# In[92]:


dataset_sin_duplicados = dataset_ordenado.drop_duplicates(subset=['Crm Cd'])


# In[93]:


dataset_sin_duplicados.shape


# In[94]:


pd.set_option('display.max_', None)
dataset_sin_duplicados


# In[95]:


dataset3['Crm Cd 1'].info()


# In[96]:


# Convertir las columnas en conjuntos y encontrar los valores distintos
valores_distintos_col1 = set(dataset['Crm Cd'])
valores_distintos_col2 = set(dataset['Crm Cd 1'])

# Encontrar los valores distintos entre las dos columnas
valores_distintos = valores_distintos_col1.symmetric_difference(valores_distintos_col2)

print("Valores distintos entre las columnas:", valores_distintos)


# In[97]:


dataset['Crm Cd 1'].value_counts()[521]


# In[98]:


dataset['Crm Cd 1'].value_counts()[430]


# In[ ]:


# Convertir las columnas en conjuntos y encontrar los valores distintos
valores_distintos_col3 = set(dataset['Crm Cd'])
valores_distintos_col4 = set(dataset['Crm Cd 2'])


# Encontrar los valores distintos entre las dos columnas
valores_distintos = valores_distintos_col3.symmetric_difference(valores_distintos_col4)

print("Valores distintos entre las columnas:", valores_distintos)


# In[ ]:


# Convertir las columnas en conjuntos y encontrar los valores distintos
valores_distintos_col1 = set(dataset['Crm Cd'])
valores_distintos_col2 = set(dataset['Crm Cd 3'])

# Encontrar los valores distintos entre las dos columnas
valores_distintos = valores_distintos_col1.symmetric_difference(valores_distintos_col2)

print("Valores distintos entre las columnas:", valores_distintos)


# In[ ]:




