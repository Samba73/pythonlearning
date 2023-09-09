#n = 5
#for i in range(0, n):
#    for j in range(0, i+1):
#        print('*', end=' ')
#    print()
#for i in range(n, 0, -1):
#    for j in range(0, i-1):
#        print('*', end=' ')
#    print()
index = 0
l = ['aba', 'd', '45', '233', 'dfg', 'neaten', 's']
count = 0
#leng = 0
#for index, il in enumerate(l):
#    sw = ''
#    #print(type(il))
#    if len(il) >= 2:
#        sw = il[0]
#        if il.startswith(sw) == il.endswith(sw):
#            count += 1
#for word in l:
#    if len(word) >= 2 and word[0] == word[-1]:
#        count += 1
#print(count)
#def concatenate(l1, l2):
#    concat_list = []
#    for i in range(len(l1)):
#        for j in range(len(l2)):
#            concat_list.append(f'{l1[i]} {l2[j]}')
#    return concat_list

eword = ''
dword = ''
alpha = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
l = alpha.split(',')
print(l)
shift = 100
word = 'hello worlds@*()'
while shift > 26:
    shift = shift - 26
ltemp = l[:shift]
##print(ltemp)
l1 = l[shift:]
for i in ltemp:
    l1.append(i)
print(l1)
for w in word:
 if w in l:
     pos = l.index(w)
     new_char = l1[pos]
     eword += new_char
 else:
     eword += w
print(eword)
word = eword
for w in word:
 if w in l1:
     pos = l1.index(w)
     new_char = l[pos]
     dword += new_char
 else:
     dword += w
print(dword)




