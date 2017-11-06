import matplotlib.pyplot as pl
import numpy as np
import pandas as pd
import scipy

filename='/Users/rdodson/Data/GW/GW_list.txt'
url='http://ict.icrar.org/store/staff/rdodson/GW/GW_list.txt'
print 'About to read the large dile '+url
data_frame=pd.read_csv(url,delimiter=' ',header=None)
print 'Read file with '+str(data_frame.shape)+' values'
data = data_frame.values
labels = data[:,4].astype(int)
data = data[:, 0:4]

# Time in seconds
t=np.reshape(data.transpose()[0][0:29698949],(29698949/6001,6001))
# Signal plus noise
dH=np.reshape(data.transpose()[1][0:29698949],(29698949/6001,6001))*1e20
# Signal only
d=np.reshape(data.transpose()[2][0:29698949],(29698949/6001,6001))*1e20
# Noise 4 seconds previously
ns=np.reshape(data.transpose()[3][0:29698949],(29698949/6001,6001))*1e20
# True/False for significant signal
#tf=np.reshape(data.transpose()[4][0:29698949],(29698949/6001,6001))
tf=labels

#GW=np.loadtxt('GW_list.txt',delimiter=' ')
#t=np.reshape(GW.transpose()[0][0:29698949],(29698949/6001,6001))
#dH=np.reshape(GW.transpose()[1][0:29698949],(29698949/6001,6001))
#d=np.reshape(GW.transpose()[2][0:29698949],(29698949/6001,6001))
#ns=np.reshape(GW.transpose()[3][0:29698949],(29698949/6001,6001))
#tf=np.reshape(GW.transpose()[4][0:29698949],(29698949/6001,6001))

# Make 10 times stronger signal
dH10=[]
for n in range(4949):
    dH10.append(dH[n][:]+d[n][:]*10)

# Sum of noise
for n in range(4949):
    a = pl.specgram(ns[n][:], NFFT=256, Fs=4096, Fc=0, noverlap=200)
    if (n==0):
        Ssn=a[0]
    else:
        Ssn=Ssn+a[0]

Ssn=Ssn/4949