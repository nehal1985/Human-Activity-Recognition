import numpy as np
import pandas as pd
from scipy import stats

a = "0.788354,\
0.764051,\
0.686076,\
0.720506,\
0.735696,\
0.763038,\
0.711899,\
0.750886,\
0.700253,\
0.698734,\
0.782785,\
0.763038,\
0.739747,\
0.793924,\
0.738734,\
0.755949,\
0.728608,\
0.723038,\
0.79443,\
0.740253,\
0.753418,\
0.770633,\
0.813671,\
0.796456,\
0.745316,\
0.79038,\
0.767595,\
0.77519,\
0.77924,\
0.755949,\
0.740759,\
0.752405,\
0.740253"

a = a.split(',')
#print len(a)
for i in range(0,len(a),3):
	s = float(a[i]) + float(a[i+1]) + float(a[i+2])
	#print s/3

num = 5

a = [[2.06385050e-02 ,  2.06867717e-02  , 1.27847642e-02 ,  6.09926088e-03,
    1.02101662e-03 ,  2.07963842e-03  , 8.85474265e-01,   2.06631999e-02,
    2.24115048e-03  , 1.91908213e-03 ,  2.12861481e-03 ,  2.20739073e-03,
    1.37711316e-02  , 3.77238682e-03,   7.35209440e-04  , 2.20035389e-03,
    1.57725462e-03],
 [  2.24688067e-03 ,  5.50873112e-03   ,1.27269269e-03,   2.31472496e-03,
    2.37901183e-03 ,  3.79171601e-04  , 9.51529384e-01 ,  2.07437071e-04,
    3.25155607e-03  , 6.87200669e-03 ,  9.61866870e-04 ,  3.48046981e-03,
    1.12063782e-02  , 3.67921125e-03,   2.49694963e-03 ,  1.28896267e-03,
    9.24537715e-04],
 [  9.66122083e-04  , 6.94387686e-03  , 3.45678825e-04,   2.53057363e-03,
    3.79262189e-03  , 2.65058334e-04  , 9.37180281e-01 ,  5.60644455e-03,
    2.21580006e-02  , 4.44904855e-03  , 1.42685371e-03  , 3.64371663e-04,
    7.25217210e-03  , 4.09244932e-03  , 2.42732523e-04   ,1.04028953e-03,
    1.34334830e-03]]
a = a[1]
a = np.array(a)
#for i in a:
#	print float(i)

#print a
#print np.sum(a > 0.95)

#print np.ceil(num*1.0/2)

#acc = [0.8,0.95,0.9]

pre = np.array([[0.44,1.0,0.52,2.0,0.45,1.0, 1.0],[0.4,1.0,0.5,2.0,0.45,1.0,1.0]])

df = pd.DataFrame(pre)

l = df.iloc[0].values
print l

pre = l[0::2]
pre = pre[0:-1]
print pre

act = l[1::2]

real = l[-1]
print act
print real


print stats.mode(act)



print "_______________"
data = np.array([[1,2],[3,4],[5,6]])
label = np.array([[1],[2],[1]])
print data
print label

pos =  label[..., 0] == 1
print pos
print data[pos]


one = np.arange(10)
two = np.arange(10)

print (one + two) / 2


a = [-0.02425879, 0,          0.08955222,  0.15384617, -0.15000001 , 0.01176471,
 -0.00116956 ,-0.04347825, -0.08749998, -0.08163264,  0,          0.,
 -0.30000001 , 0.21428573 , 0.   ,       0.  ,       -0.1       ]
for i in a:
    print str(i).replace(".",",")