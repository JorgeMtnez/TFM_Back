#!/usr/bin/env python
# coding: utf-8

# # TFM: MAPA DE PELIGROSIDAD

# Lo primero que debemos hacer es descargar los datos desde una pa

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


dataset = pd.read_csv(r"C:\Users\amari\OneDrive\Documentos\GitHub\TFM_Back\data\Crime_Data_from_2020_to_Present.csv")


# In[3]:


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

# In[4]:


dataset.head(10)


# In[5]:


dataset.info()


# In[6]:


dataset.nunique()


# En una primera aproximación de los datos podemos observar que tenemos 3 variables a examinar:
# - La variable Crdm cd, la cual indica del 1 al 4 el nivel de peligrosidad de los datos, la cual podriamos fusionar, de alguna manera.
# - La variable vict sex tiene 5 valores distintos por lo que deberemos examinar cuales son y por que, ya que solo debería tener dos, hombre y mujer.

# In[7]:


# Lista de columnas en las que deseas aplicar el reemplazo
# columnas_a_modificar = ['Crm Cd 1', 'Crm Cd 2', 'Crm Cd 3', 'Crm Cd 4']

# Función que reemplaza los valores con 1 si tienen valor, y con 0 si no tienen valor
# dataset[columnas_a_modificar] = np.where(dataset[columnas_a_modificar].notnull(), 1, 0)

# Muestra el DataFrame modificado
# print(dataset)


# #### Para tener un mejor conocimiento del dataset podemos analizar los descriptivos 

# In[8]:


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

# In[9]:


for valor in dataset['Vict Sex'].unique():
    print(valor)


# In[10]:


contador = dataset['Vict Sex'].value_counts()['H']
contador


# In[11]:


dataset.shape


# In[12]:


contador = dataset['Vict Sex'].value_counts()
contador


# In[13]:


contador = dataset['Vict Sex'].isnull().sum()
contador


# In[14]:


# Número de valores distintos por variable
dataset1 = dataset[dataset['Vict Sex'] != 'H']
dataset1.info()


# In[15]:


for valor in dataset1['Vict Sex'].unique():
    print(valor)


# In[16]:


dataset2 = dataset1[dataset1['Vict Sex'] != '-']
dataset2.info()


# In[17]:


for valor in dataset2['Vict Sex'].unique():
    print(valor)


# In[18]:


contador = dataset2['Vict Sex'].isnull().sum()
contador


# In[19]:


contador = dataset2['Vict Sex'].value_counts()
contador


# In[20]:


import plotly.express as px
# Histograma de calificación del productor
fig = px.histogram(dataset2, x="Vict Sex") 
fig.show()


# Hemos eliminado los valores H y - ya que su represenatción era mínima, sin embargo, en el caso de X deberemos determinar si está variable será determinante. Pensamos que puede ser interesante dejar este valor porque actualmente el valor 'otros' es visulizado.

# In[21]:


sns.violinplot(x='Vict Sex', y='Vict Age', data=dataset2, palette='viridis')


# 2. Estudiamos la variable Status y Status Desc

# hacer rangos de edad

# In[22]:


for valor in dataset2['Status'].unique():
    print(valor)


# In[23]:


for valor in dataset2['Status Desc'].unique():
    print(valor)


# In[24]:


contador = dataset2['Status'].value_counts()
contador


# In[25]:


contador = dataset2['Status Desc'].value_counts()
contador


# Podemos observar que:
# - Las dos variables tienen exactamente los mismos valores y el mismo número, por lo tanto, se trata de la misma variable
# - Los valores Unknown representan un pocentaje insignificante y podrán ser eliminados

# In[26]:


dataset2 = dataset1[dataset1['Status Desc'] != 'UNK']
dataset2.info()


# In[27]:


dataset3 = dataset2.drop(['Status'],axis=1)


# In[28]:


import plotly.express as px
# Histograma de calificación del productor
fig = px.histogram(dataset3, x="Status Desc") 
fig.show()


# 3. Part 1-2:

# In[29]:


for valor in dataset2['Part 1-2'].unique():
    print(valor)


# In[30]:


# Calcula la matriz de correlación
correlation_matrix = dataset3.corr()

# Crea un mapa de correlación utilizando Seaborn
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Mapa de Correlación')
plt.show()


# In[31]:


for valor in dataset2['Crm Cd'].unique():
    print(valor)


# ¿eliminamos crm cd y part 1-2?

# ## Pasar a factor

# In[32]:


# Lista de columnas con menos de 10 valores distintos. Potenciales factores!
dataset3['Vict Sex'] = dataset3['Vict Sex'].astype('category')
dataset3['Status Desc'] = dataset3['Status Desc'].astype('category')


# In[33]:


dataset3.info()
dataset3.describe()


# In[34]:


dataset3.describe(exclude=np.number)


# In[35]:


for valor in dataset2['Premis Desc'].unique():
    print(valor)


# ### Creamos los rangos de edad:

# In[36]:


## AGE (realizamos una variable con 3 rangos de edad y 3 variables con esos mismos rangos)
dataset3['Niño'] = dataset3['Vict Age'].apply(lambda x: 1 if x<=12 else 0)
dataset3['Joven'] = dataset3['Vict Age'].apply(lambda x: 1 if x>12 and x<=26 else 0)
dataset3['Adulto'] = dataset3['Vict Age'].apply(lambda x: 1 if x>26 and x<60 else 0)
dataset3['Mayor de 60'] = dataset3['Vict Age'].apply(lambda x: 1 if x>=60 else 0)
# dataset3['Mayor de 60'] = dataset3['Vict Age'].apply(lambda x: 0 if x<=35 else (1 if x>35 and x<60 else(2)))


# In[37]:


pd.set_option('display.max_columns', None)

dataset3.head()


# ### Valores atípicos

# In[38]:


dataset3.select_dtypes(include=np.number).apply(lambda x: x.skew())


# In[39]:


dataset3[['Crm Cd 4']].nunique()


# In[40]:


dataset['Crm Cd 1'].isnull().sum()


# In[41]:


print(dataset3['Crm Cd 1'].value_counts(),
dataset3['Crm Cd 2'].value_counts(),
dataset3['Crm Cd 3'].value_counts(),
dataset3['Crm Cd 4'].value_counts())


# In[42]:


dataset_prueba= dataset3[['Crm Cd','Crm Cd Desc']]
dataset_prueba


# In[43]:


dataset_ordenado = dataset_prueba.sort_values(by='Crm Cd', ascending=True)


# In[44]:


dataset_ordenado


# In[45]:


dataset_sin_duplicados = dataset_ordenado.drop_duplicates(subset=['Crm Cd'])


# In[46]:


dataset_sin_duplicados.shape


# In[47]:


pd.set_option('display.max_rows', None)
dataset_sin_duplicados


# In[48]:


dataset3['Crm Cd 1'].info()


# In[49]:


# Convertir las columnas en conjuntos y encontrar los valores distintos
valores_distintos_col1 = set(dataset['Crm Cd'])
valores_distintos_col2 = set(dataset['Crm Cd 1'])

# Encontrar los valores distintos entre las dos columnas
valores_distintos = valores_distintos_col1.symmetric_difference(valores_distintos_col2)

print("Valores distintos entre las columnas:", valores_distintos)


# In[50]:


dataset['Crm Cd 1'].value_counts()[521]


# In[51]:


dataset['Crm Cd 1'].value_counts()[430]


# In[61]:


prueba2 = dataset3.drop_duplicates(subset=['Crm Cd'])


# In[65]:


prueba2.shape


# In[66]:


prueba1.shape


# In[59]:


prueba1= dataset3.drop_duplicates(subset=['Crm Cd 2'])


# In[68]:


# Verificar los valores únicos en 'Crm Cd 2'
crm_cd_2_unique = dataset3['Crm Cd 2'].unique()

# Verificar los valores únicos en 'Crm Cd'
crm_cd_unique = dataset3['Crm Cd'].unique()

# Encontrar los valores en 'Crm Cd 2' que no están en 'Crm Cd'
valores_no_en_crm_cd = [valor for valor in crm_cd_2_unique if valor not in crm_cd_unique]

# Imprimir los valores que no están en 'Crm Cd'
print("Valores en 'Crm Cd 2' que no están en 'Crm Cd':")
print(valores_no_en_crm_cd)


# In[75]:


dataset3['Crm Cd 2'].value_counts()[521.0]


# In[ ]:


##comentar si eliminamos los crm cd 2, 3 y 4!


# In[78]:


dataset_sin_duplicados


# In[64]:


# Convertir las columnas en conjuntos y encontrar los valores distintos
valores_distintos_col3 = set(prueba1)
valores_distintos_col4 = set(prueba2)


# Encontrar los valores distintos entre las dos columnas
valores_distintos = valores_distintos_col3.symmetric_difference(valores_distintos_col4)

print("Valores distintos entre las columnas:", valores_distintos)


# In[ ]:


#907 has ta 20 años de prisión secuestro
#921 trafico de personas de 20 - 30 años
#922 robo de un menor de 16 meses a 3 años. leve
#924 0 a 6 meses infraccion delto leve
#928 amenzas telefo del leves
#930 del leves


# In[ ]:


#Cadena perpetua p hasta 20 años..
#del_muy_graves = dataset_sin_duplicados[Crm Cd[110, 121, 235, 900,  907, 921, 860, 822,  ]]


# In[ ]:


# de 5 a 19
#del_graves = dataset_sin_duplicados[Crm Cd[113, 122, 210, 220, 230, 231,236, 237, 250, 251, 354, 433, 434, 940, 942, 944,
 #                                          954, 956, 470, 473, 870, 845, 840, 820, 815, 814, 626, 627, 648, 805, 762, 761,
 #                                         760, 756, 755,   ]]


# In[ ]:


#de 1 a 5
#del_menos_graves = dataset_sin_duplicados[Crm Cd[310,330, 331, 341, 343, 345, 347, 349, 410, 420, 421, 901, 902, 435,
 #                                                903, 436, 904, 931, 943, 446, 350, 450, 946, 948, 949, 950, 951, 475, 622,
 #                                                865, 830, 821, 625, 624, 647, 810, 649, 763, 661, 662, 668, 740   ]]


# In[ ]:


#menos de un año
#del_leves = dataset_sin_duplicados[Crm Cd[320, 351, 352, 353, 432, 437, 438, 906, 924, 928, 930, 439, 932, 440, 441, 442,
  #                                        443, 444, 445, 451, 452, 471,474, 480, 485, 890, 888, 487, 510, 520, 522, 882, 623,
  #                                       , 880, 850, 651, 653, 652, 654, 660, 664, 666, 670, 753, 745,   ]]


# In[ ]:


#Meses
#infracciones = dataset_sin_duplicados[Crm Cd[933, 886, 884, 813, 812, 806,    ]]

# Convertir las columnas en conjuntos y encontrar los valores distintos
valores_distintos_col1 = set(dataset['Crm Cd'])
valores_distintos_col2 = set(dataset['Crm Cd 3'])

# Encontrar los valores distintos entre las dos columnas
valores_distintos = valores_distintos_col1.symmetric_difference(valores_distintos_col2)

print("Valores distintos entre las columnas:", valores_distintos)
# In[ ]:





# In[ ]:





# In[ ]:




