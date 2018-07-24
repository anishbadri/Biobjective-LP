# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 16:13:58 2018

@author: gehen
"""

import numpy as np;
from copy import deepcopy;

def bolp(O1,O2,A,b):
    if all(i >= [0] for i in O2):
        C=O2
        C1=O1
    
    #Adding slack variables to constraints
    for i in range(0,len(b)):
        for j in range(0,len(b)):
            if (i==j):
                A[i]=A[i]+[1];
            else:
                A[i]=A[i]+[0]
    
    def createA(A,b):
        for i in range(0,len(b)):
            A[i]+=(b[i]);
        return A
    
    A= createA(A,b)
    
    #Adding slack variables to objectives
    x=len(A[1])-len(C[0]);
    for i in range(0,len(C)):
            C[i]=C[i]+[0]*x;
            C1[i]=C1[i]+[0]*x;
    
    #Creating initial tableau
    t=C+A
    print('tableau is:',t)
    
    #First tableau (I, Lambda, s)
    I=[]
    for i in range(0,len(t[0])):
        if t[0][i]<0:
            I.append(i+1)
    print('I=',I)
    
    #Initial basis
    B=[]
    for i in range(len(b),0,-1):
        B+=[len(t[0])-i];
    print('B=',B);
    
    
    while I!=[]:
        #Updating the tableau
        
        #Knowing entering and leaving variable
        s = []
        for i in I:
            s.append(t[0][i-1])
        smin=min(s)
        index1=s.index(smin);
        s=I[index1];
        print('s=',s);
        
        r=[];
        for i in range(len(C),len(t),1):
            if t[i][s-1]==0:
                r+=[t[i][len(t[0])-1]/0.001];
            else:
                r+=[t[i][len(t[0])-1]/t[i][s-1]];
        rmin=[]
        for i in r:
            if i>0:
                rmin+=[i];
        r=min(rmin)
        index2=rmin.index(r)
        rc=B[index2];
        print('r=',rc);
        
        print('-----------------------------------------------------------------------------------------------------------------------------------------')

    #New Basis
        B=B+[s];
        B.remove(rc);
        B.sort()
        print('B=',B)
    
    #Creating Basis Matrix
        AB=[]
        for i in range(0,len(B)):
            for j in range(0,len(B)):
                AB+=[t[len(C)+i][B[j]-1]];
    
        AB=np.array(AB).reshape(len(B),len(B))  
        
        AB=np.matrix(AB)
    
        CB=[]
        for i in range(0,len(C)):
            for j in range(0,len(B)):
                CB+=[t[i][B[j]-1]];
    
        CB=np.array(CB).reshape(len(C),len(B))  
        
        CB=np.matrix(CB)
    
    #Update C
        C=np.matrix(C)
        C=C-CB*AB.I*A
        C=C.tolist()
    
    #Update A
        A=np.matrix(A)
        A=AB.I*A
        A=A.tolist()
    
    #Update tableau
        t=C+A
        print('tableau is:',t)
    
    #Second tableau (I, Lambda, s)
        I=[]
        for i in range(0,len(t[0])):
            if t[0][i]<0:
                I.append(i+1)
        print('I=',I)
        
        print('B=',B)
    #Calculating Lambda
        if I!=[]:
    
            s = []
            for i in I:
                s.append(t[0][i-1])
            smin=min(s)
            index1=s.index(smin);
            s=I[index1];
            print('s=',s);
    
            r=[];
            for i in range(len(C),len(t),1):
                if t[i][s-1]==0:
                    r+=[t[i][len(t[0])-1]/0.001];
                else:
                    r+=[t[i][len(t[0])-1]/t[i][s-1]];
            rmin=[]
            for i in r:
                if i>0:
                    rmin+=[i];
            index2=rmin.index(min(rmin));
            rc=B[index2]
            print('r=',rc);
    
            print('-----------------------------------------------------------------------------------------------------------------------------------------')
    
    #Phase 3
    print('\n','------------PHASE 3------------','\n')
    #Creating initial tableau
    
    #Convertin 2d list to 1d list for C1        
    def flatten(input):
        new_list = []
        for i in input:
            for j in i:
                new_list.append(j)
        return new_list
    C1=flatten(C1)
    C.insert(1, C1)
    t.insert(1, C1)
    print('tableau is:',t)
    
    #First tableau (I, Lambda, s)
    I=[]
    for i in range(0,len(t[0])):
        if t[0][i]>=0 and t[1][i]<0:
            I.append(i+1)
    print('I=',I)
    
    print('B=',B);
    
    while I!=[]:
    #Updating the tableau
    
         #Calculating Lambda
        Lambda=[]
        for i in range(0,len(I)):
            Lambda+=[-C[1][I[i]-1]/(C[0][I[i]-1]-C[1][I[i]-1])]
        
        for i in range(0,len(Lambda)):
            index1=Lambda.index(max(Lambda));
        s=I[index1];
        print('s=',s);
        
        r=[];
        for i in range(len(C),len(t),1):
            if t[i][s-1]==0:
                r+=[t[i][len(t[0])-1]/0.001];
            else:
                r+=[t[i][len(t[0])-1]/t[i][s-1]];
        rmin=[]
        for i in r:
            if i>0:
                rmin+=[i];
        index2=rmin.index(min(rmin));
        rc=B[index2]
        print('r=',rc);
        
        
        Lambda=max(Lambda);
        print('Lambda=',Lambda)
        print('-----------------------------------------------------------------------------------------------------------------------------------------')
        
    
    #New Basis
        B=B+[s];
        B.remove(rc);
        B.sort()
    
    #Creating Basis Matrix
        AB=[]
        for i in range(0,len(B)):
            for j in range(0,len(B)):
                AB+=[t[len(C)+i][B[j]-1]];
    
        AB=np.array(AB).reshape(len(B),len(B))  
        
        AB=np.matrix(AB)
    
        CB=[]
        for i in range(0,len(C)):
            for j in range(0,len(B)):
                CB+=[t[i][B[j]-1]];
    
        CB=np.array(CB).reshape(len(C),len(B))  
        
        CB=np.matrix(CB)
    
    #Update C
        C=np.matrix(C)
        C=C-CB*AB.I*A
        C=C.tolist()
    
    #Update A
        A=np.matrix(A)
        A=AB.I*A
        A=A.tolist()
    
    #Update tableau
        t=C+A
        print('tableau is:',t)
    
    #Second tableau (I, Lambda, s)
        I=[]
        for i in range(0,len(t[0])):
            if t[0][i]>=0.0 and t[1][i]<0:
                I.append(i+1)
        print('I=',I)
        
        print('B=',B)
    #Calculating Lambda
        if I!=[]:
            Lambda=[]
            for i in range(0,len(I)):
                Lambda+=[-C[1][I[i]-1]/(C[0][I[i]-1]-C[1][I[i]-1])]
    
            for i in range(0,len(Lambda)):
                index1=Lambda.index(max(Lambda));
            s=I[index1];
            print('s=',s);
    
            r=[];
            for i in range(len(C),len(t),1):
                if t[i][s-1]==0:
                    r+=[t[i][len(t[0])-1]/0.001];
                else:
                    r+=[t[i][len(t[0])-1]/t[i][s-1]];
           # rmin=[]
           # for i in r:
           #     if i>0:
           #         rmin+=[i];
            rmin = min(i for i in r if i > 0)
            index2=r.index(rmin);
            rc=B[index2]
            print('r=',rc);
    
    
            Lambda=max(Lambda);
            print('Lambda=',Lambda)
            print('-----------------------------------------------------------------------------------------------------------------------------------------')

#First objective(C) and constraints
bolp([[1,2,1]],[[0,2,1]],[[0,1,4],[1,1,0]],[[8],[8]]) 

   