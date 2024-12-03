###------ 0. Preamble ---------
### ===========================

from scipy.io import loadmat
import pandas as pd
import numpy as np
import csv

### [NOTE: Use ALT+3 to comment // ALT+4 to uncomment]


###------ 1. Load .mat file and convert it to .csv file -------
### ===========================================================


## --- 1a. Load .mat file from desired directory
## ```````````````````````````````````````````````

# ^^^ octuple_tank_data_11_11_24.mat contains 4000 x 15 data; the first column being the index number (by MATLAB)

data = loadmat(r"D:\[] MKM_PhD_2023\MatlabCodes\Octuple_Tank\octuple_tank_data_11_11_24.mat")

#data = loadmat(r"C:\Users\MAHE\AppData\Local\Programs\Python\Python313\octuple_tank_data_11_11_24.mat")
## mkm_laptop --> "D:\[] MKM_PhD_2023\MatlabCodes\Octuple_Tank\octuple_tank_data_11_11_24.mat"



## --- 1b. Convert .mat file to .csv and save in the current directory
## ````````````````````````````````````````````````````````````````````
for i in data:
        if '__' not in i and 'readme' not in i:
              np.savetxt(("Res.csv"),data[i],delimiter=',')

df = pd.read_csv('Res.csv')

##reader = csv.reader(open("Res.csv", "rb"), delimiter=",")
##x = list(reader)
##result = numpy.array(x).astype("float")

with open('Res.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader) 


## --- 1c. Read .csv file as Numpy Array
## ``````````````````````````````````````
    
data_array = np.array(data, dtype=float)
N_data = len(data_array)    ## = 4000
M_data = len(data_array[0]) ## = 15 (... the first col. contains index no. !! It must be removed)


C = np.delete(data_array, 0, 1)## delete the first column of 'data_array'
## Caution: In python, indexing (row or column) starts from i,j = 0 !!


N1_data = len(C) ### no. of observations in raw-data file 'data_array' [ROWS = 4000]
M1_data = len(C[0]) ### no. of data-vectors in raw-data file 'data_array' [COLUMNS]

print('No. of observations in raw-data files =', N1_data)
print('\nNo. of data-vectors in raw-data files =', M1_data)

###dff = data.drop(data.iloc[:, 1:3], axis=1)
##dff1 = np.delete(data_array, 0, 0)
##


#### --- 1d. Write Numpy Array into .csv file (Optional)
#### ````````````````````````````````````````````````````
##DF = pd.DataFrame(C)
##DF.to_csv("data_OG.csv")  ### not necessary




###------ 2. Split data-file into Training & Testing data -------
### =============================================================

n1= N1_data/2
m1= M1_data/2

n2=n1
m2=m1

##Dtrain = 
##Dtest = 

plt.plot(x, y, color='green', label='Sine')
plt.legend()
plt.xlabel("Time (t)")
plt.ylabel("Ampliltude")
plt.grid()
plt.show()







