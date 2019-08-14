# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 18:22:34 2019

@author: adars
"""

def safe(i,j,l):
    if i>=0 and i<x and j>=0 and j<w and l[i][j]==1:
        return True
    else:
        return False
def maze(i,j):
    global l
    global p
   # print('i AM IN')
    #print(i,j,'i,j')
    #print(p,'p ko check')

    if i==0 and j==0:
        print('The value is',p)
        return p
    if safe(i,j,l):
        if safe(i-1,j,l):
            p.append('u')
           # print('upppp')
            l[i][j]=0
            p=maze(i-1,j)

        if safe(i+1,j,l):
            p.append('d')
            #print('down')
            l[i][j]=0
            p=maze(i+1,j)

        if safe(i,j-1,l):
            p.append('l')
            l[i][j]=0
            p=maze(i,j-1)
        if safe(i,j+1,l):
            p.append('r')
            l[i][j]=0
            p=maze(i,j+1)
        #print(p,'p')
        if not (safe(i-1,j,l) and safe(i+1,j,l) and safe(i,j-1,l) and safe(i,j+1,l)):
        # print('pop operation')
         try:
          p.pop()
         except:
          pass
         l[i][j]=0
         return p

w=int(input())
x=int(input())
l=list()
for a in range(x):
    l.append([])
    for b in range(w):
        l[a].append(int(input()))
p=list()
print(l)
#maze(0,w-1)
#p=list()
maze(x-1,0)
#p=list()
#maze(x-1,w-1)