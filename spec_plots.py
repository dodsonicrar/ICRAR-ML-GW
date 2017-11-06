NFft=256
NOver=200
TypNoise=np.median(Ssn)

psd=scipy.signal.periodogram(ns,nfft=NFft,detrend=scipy.signal.detrend)
Ssn=np.zeros((1,(NFft/2+1)))
for n in range((NFft/2+1)):
    mns=np.mean(psd[1].transpose()[n][:])
    if (mns<1e-4):
        Ssn[0][n]=1
    else:
        Ssn[0][n]=mns
Ssn=Ssn.transpose()*np.ones((1,103))


for n in range(4949):
    pl.figure(0)
    b = pl.specgram(dH10[n][:], NFFT=NFft, Fs=4096, Fc=0, detrend=scipy.signal.detrend, noverlap=NOver)
    pl.clf()
    pl.subplot(1,2,1)
    pl.imshow(b[0]/Ssn,aspect='auto',extent=[4096/2,0,0,6001.0/4096])
    pl.title('Injected Signal: '+str(n))
    pl.subplot(1,2,2)
    hn=pl.histogram(b[0]/Ssn,30)
    cn=[]
    for m in range(len(h[0])):
     cn.append((hn[1][m]+hn[1][m+1])/2)
    pl.semilogy(cn,hn[0]+0.1)
    pl.pause(0.01)
    pl.figure(1)
    a = pl.specgram(ns[n][:], NFFT=NFft, Fs=4096, Fc=0, detrend=scipy.signal.detrend, noverlap=NOver)
    pl.clf()
    pl.subplot(1,2,1)
    pl.imshow(a[0]/Ssn,aspect='auto',extent=[4096/2,0,0,6001.0/4096])
    pl.title('Normalised Noise: '+str(n))
    pl.subplot(1,2,2)
    hn=pl.histogram(a[0]/Ssn,30)
    cn=[]
    for m in range(len(h[0])):
     cn.append((hn[1][m]+hn[1][m+1])/2)
    pl.semilogy(cn,hn[0]+0.1)
    pl.pause(00.01)
    pl.figure(2)
    pl.clf()
    pl.subplot(1,2,1)
    pl.imshow(b[0]/a[0],aspect='auto',extent=[4096/2,0,0,6001.0/4096])
    pl.title('Local noise supression: '+str(n))
    pl.subplot(1,2,2)
    h=pl.histogram(b[0]/(a[0]+TypNoise*3),30)
    c=[]
    for m in range(len(h[0])):
      c.append((h[1][m]+h[1][m+1])/2)
    pl.semilogy(c,h[0]+0.1)
    pl.pause(0.01)
    pl.figure(3)
    psd=scipy.signal.periodogram(ns[n],nfft=NFft,detrend=scipy.signal.detrend)
    if (n==0):
      Ssn100=(np.reshape(psd[1],(129,1))*np.ones((1,103)))
    else:
      Ssn100=Ssn100+(np.reshape(psd[1],(129,1))*np.ones((1,103)))
    nS=(n+1)
    if (n>99):
      psd=scipy.signal.periodogram(ns[n-100],nfft=NFft,detrend=scipy.signal.detrend)
      #a100 = pl.specgram(ns[n-100][:], NFFT=NFft, Fs=4096, Fc=0, detrend=scipy.signal.detrend, noverlap=NOver)
      Ssn100=Ssn100-(np.reshape(psd[1],(129,1))*np.ones((1,103)))
      nS=100
    pl.clf()
    pl.subplot(1,2,1)
    pl.imshow(b[0]/(Ssn100*nS),aspect='auto',extent=[4096/2,0,0,6001.0/4096])
    pl.title('Last few noise supression: '+str(nS))
    pl.subplot(1,2,2)
    h=pl.histogram(b[0]/(Ssn100/nS),30)
    c=[]
    for m in range(len(h[0])):
      c.append((h[1][m]+h[1][m+1])/2)
    pl.semilogy(c,h[0]+0.1)
    pl.semilogy((cn),hn[0]+0.1,'r')
    pl.pause(0.1)
    pl.figure(4)
    pl.clf()
    pl.subplot(2,1,1)
    pl.plot(d[n][:])
    pl.subplot(2,1,2)
    pl.plot(dH10[n][:])
    pl.pause(0.01)
    pl.figure(5)
    pl.clf()
    s=pl.specgram(d[n][:], NFFT=NFft, Fs=4096, Fc=0, detrend=scipy.signal.detrend, noverlap=NOver)
    pl.imshow(s[0],aspect='auto',extent=[4096/2,0,0,6001.0/4096])
    pl.title('Signal '+str(n))
    pl.pause(0.01)
