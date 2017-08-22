# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 09:43:09 2017
-------------------------------------------------------------------------------
PLAGIARISM DETECTOR PROJECT
-------------------------------------------------------------------------------
@author: RaghavendraGali
"""
"""
-------------------------------------------------------------------------------
Practice code:
----------------------------------------------------------------------------"""
import math
import time
import os
class bagOfWords(object):
    def __init__ (self,mod_x=0,dic1={},dic2={},L=[]):
        self.mod_x=0
        self.b=0
        self.dic1=dic1
        self.dic2=dic2  
        self.L=L
    def wrdsfreq(self,lyrics):
        dic2={}
        spl=0
        for i in lyrics:
            spl=i.split() 
            for word in spl:
                if word in dic2:
                    dic2[word]+=1
                else:
                    dic2[word]=1
        return dic2
    def Mod(self,d1):
        self.mod_x=0
        for word in d1:
            self.mod_x+=d1[word]**2
        self.mod_x=math.sqrt(self.mod_x)
        return self.mod_x
    def comReps(self,dic1,dic2):
        L2=0
        a=0
        for i in dic2:
            if i in dic1:
                a=dic1[i]*dic2[i]
                L2+=a
        return float(L2)
    def EuFreqs(self):
        self.dic1={}
        self.dic2={}
        lists = os.listdir(os.getcwd())
        i=0
        for file in lists:
            j=0
            print("Loop 1 file: "+file)
            text_open=open(file,"r")
            self.dic1=a.wrdsfreq(text_open)
            L1.append(a.Mod(self.dic1))
            for file in lists:
                if file!=open:
                    if i<j:
                        print("File name is: "+file)
                        text_open=open(file,"r")
                        self.dic2=a.wrdsfreq(text_open)
                        L.append(a.comReps(self.dic1,self.dic2))
                        text_open.close()
                    j=j+1
            text_open.close()
            i+=1
        return L
    
    
a=bagOfWords()
t1=time.time()
L1=[]
L=[]
dis=[]
r=1
L=a.EuFreqs()
print(L)
print(L1)
j=0
for i in range(len(L1)):
    if j!=len(L):
         a=L1[i]/(L[j]*L[j+1])
         print(a)
         #ans=math.acos(a)
         dis.append(a)
         #print(ans)
         #ans=math.degrees(ans)
         #print(ans)
         j+=1
print(dis)
t2=time.time()-t1
print("Time taken: ",t2)

    
    
   