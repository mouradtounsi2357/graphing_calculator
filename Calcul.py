#!/usr/bin/python3
#-------------------------------------------------------------------#
# MOURAD TOUNSI                                                     #
#-------------------------------------------------------------------#

import math


def puis(a,b):
    try:
        tmp=a**b
        return tmp
    except:
        return "nan"

def mult(a,b):
    try:
        tmp=a*b
        return tmp
    except:
        return "nan"

def dev(a,b):
    try:
        tmp=a/b
        return tmp
    except:
        return "nan"

def souc(a,b):
    try:
        tmp=a-b
        return tmp
    except:
        return "nan"

def add(a,b):
    try:
        tmp=a+b
        return tmp
    except:
        return "nan"

def flr(x):
    try:
        if x >=0:
            return float(int(x))
        else:
            return float(int(x))-1
    except :
        return "nan"

def convert_x_to_value(tab,v,variable):
    for i in range(0,len(tab),1):
        if tab[i] == v[0]:
            tab[i]=float(variable)
    return tab

def convert_constante_to_value(tab,c):
    for i in range(0,len(tab),1):
        for j in range(0,len(c),1):
            if tab[i] == c[j]:
                if j == 0:
                    tab[i]=math.pi
                if j == 1:
                    tab[i]=math.e
    return tab

def calcul_priorite_operation(tab,op):
    tab_calc=[]
    tab_new=[]
    choisie=(-1,-1,-1)
    res="nan"

    if tab[0] == '+':
        tab.remove(tab[0])
    if tab[0] == '-':
        if type(tab[1]) == float:
            tab.remove(tab[0])
            tab[0]=-tab[0]

    for i in range(len(tab)-1,0,-1):
        if (tab[i-1],tab[i]) == ('(','-'):
            if type(tab[i+1]) == float:
                tab.remove(tab[i])
                tab[i]=-tab[i]
            
    for i in range(0,len(tab)-2,1):
        var_bool=False
        for j in range(0,len(op),1):
            if tab[i+1] == op[j]:
                if (type(tab[i])==float) and (type(tab[i+2])==float):
                    var_bool=True
        if var_bool == True:
            tab_calc.append((i,i+1,i+2))
    
    for i in range(len(op)-1,-1,-1):
        for j in range(0,len(tab_calc),1):
            if tab[tab_calc[j][1]] == op[i]:
                if choisie == (-1,-1,-1):
                    choisie=tab_calc[j]
    
    if tab[choisie[1]] == op[0]:
        res=add(tab[choisie[0]],tab[choisie[2]])
    if tab[choisie[1]] == op[1]:
        res=souc(tab[choisie[0]],tab[choisie[2]])
    if tab[choisie[1]] == op[2]:
        res=dev(tab[choisie[0]],tab[choisie[2]])
    if tab[choisie[1]] == op[3]:
        res=mult(tab[choisie[0]],tab[choisie[2]])
    if tab[choisie[1]] == op[4]:
        res=puis(tab[choisie[0]],tab[choisie[2]])
    
    
    if type(res) == complex:
        res="nan"
        
    
    for i in range(0,len(tab),1):
        if i == choisie[0]:
            tab_new.append(res)
        elif (i == choisie[1]) or (i == choisie[2]):
            pass
        else:
            tab_new.append(tab[i])
    
    for i in range(0,len(tab_new),1):
        if tab_new[i] == "nan":
            return "nan"
    
    return tab_new

def eliminer_parenthese(l,tab,f,par):
    
    for p in range(0,l,1):
         
        tab_indice=[]
        tab_new=[]

        if len(tab) > 2:
            if (tab[0] == par[0]) and (tab[2] == par[1]):
                tab_indice.append(0)
                tab_indice.append(2)
        for i in range(0,len(tab)-3,1):
            if (tab[i+1] == '(') and (tab[i+3] == ')'):
                var_bool=False
                for j in range(0,len(f),1):
                    if tab[i] == f[j]:
                        var_bool=True
                if var_bool == False:
                    tab_indice.append(i+1)
                    tab_indice.append(i+3)
        
        for i in range(0,len(tab),1):
            var_bool=False
            for j in range(0,len(tab_indice),1):
                if i == tab_indice[j]:
                    var_bool=True
            if var_bool == False:
                tab_new.append(tab[i])
        tab=tab_new
    
    return tab

def calcul_fonction_usuelle(tab,f):
    #f=['tan','cos','sin','abs','fac','flr']+['ln']
    tab_v_indice=[]
    tab_new=[]
    for i in range(0,len(tab)-3,1):
        if (tab[i+1] == '(') and (tab[i+3] == ')'):
            for j in range(0,len(f),1):
                if tab[i] == f[j]:
                    if j == 0:
                        try:
                            tab_v_indice.append((math.tan(tab[i+2]),i))
                        except:
                            tab_v_indice.append(("nan",i))
                    if j == 1:
                        try:
                            tab_v_indice.append((math.cos(tab[i+2]),i))
                        except:
                            tab_v_indice.append(("nan",i))
                    if j == 2:
                        try:
                            tab_v_indice.append((math.sin(tab[i+2]),i))
                        except:
                            tab_v_indice.append(("nan",i))
                    if j == 3:
                        try:
                            tab_v_indice.append((math.fabs(tab[i+2]),i))
                        except:
                            tab_v_indice.append(("nan",i))
                    if j == 4:
                        try:
                            tab_v_indice.append((math.factorial(tab[i+2]),i))
                        except:
                            tab_v_indice.append(("nan",i))
                    if j == 5:
                        try:
                            tab_v_indice.append((flr(tab[i+2]),i))
                        except:
                            tab_v_indice.append(("nan",i))
                    if j == 6:
                        try:
                            tab_v_indice.append((math.log(tab[i+2]),i))
                        except:
                            tab_v_indice.append(("nan",i))
    
    for i in range(0,len(tab_v_indice),1):
        if tab_v_indice[i][0] == "nan":
            return "nan"

    for i in range(0,len(tab),1):
        var_bool=False
        for j in range(0,len(tab_v_indice),1):
            if i == tab_v_indice[j][1]:
                var_bool=True
                tab_new.append(tab_v_indice[j][0])
            if (i == tab_v_indice[j][1]+1) or (i == tab_v_indice[j][1]+2) or (i == tab_v_indice[j][1]+3):
                var_bool=True
        if var_bool == False:
            tab_new.append(tab[i])

    return tab_new



def calcul(tab,variable):
    pi=math.pi
    exp=math.e
    
    if variable == '':
        variable="nan"

    #fonction usuelle ------------------------------$
    f=['tan','cos','sin','abs','fac','flr']+['ln']
    # constante ------------------------------------$
    c=['pi']+['e']
    # variable -------------------------------------$
    v=['x']
    # parenthese -----------------------------------$
    par=['(',')']
    # operation ------------------------------------$
    op=['+','-','/','*','^']

    for i in range(0,len(c),1):
        if variable == c[i]:
            if i == 0:
                variable=pi
            elif i == 1:
                variable=exp
            

    tab=convert_x_to_value(tab,v,variable)
    tab=convert_constante_to_value(tab,c)
    
    while len(tab) > 1:
        tab=eliminer_parenthese(len(tab),tab,f,par)
        if tab == "nan":
            return "nan"
        tab=calcul_priorite_operation(tab,op)
        if tab == "nan":
            return "nan"
        tab=calcul_fonction_usuelle(tab,f)
        if tab == "nan":
            return "nan"
        

    if len(tab) == 0:
        return "nan"
    else:
        return tab[0]
