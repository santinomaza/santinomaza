from xml.sax import handler


#fname = input('Enter File: ')
#if len(fname) < 1 : fname = 'clown.txt'
#hand = open(fname)

#di = dict()
#for lin in hand:
 #   lin = lin.rstrip()
  #  # print(lin)
   # wds = lin.split()
    # print(wds)
    #for w in wds :
     #   print(w)
      #  if w in di :
       #     di[w] = di[w] + 1
        #    print('**Existing**')
        #else:
         #   di[w] = 1
          #  print('**NEW**')
        #print(w, di[w])

#print(di)

fname = input('Enter File: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    # print(lin)
    wds = lin.split()
    # print(wds)
    for w in wds :
        ##if the key is not there the count is zero
        ##oldcount = di.get(w, 0)
        ##print(w, 'old', oldcount)
        ##newcount = oldcount + 1
        ### idiom: retrieve/create/update counter
        di[w] = di.get(w, 0) + 1
        ###print(w, 'new', di[w])
#print(di)

#tpls x = sorted(di.items())
#tupls print(x[:5])

tmp = list()
for k, v in di.items() :
    # print(k, v)
    newtuple = (v, k)
    tmp.append(newtuple)

#tuples print('Flipped', tmp)

tmp =  sorted(tmp, reverse=True)
#tuples print('Sorted', tmp[:5])

for v, k in tmp[:5] :
    print(k, v)