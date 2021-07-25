#!/usr/bin/python3
#-------------------------------------------------------------------#
# MOURAD TOUNSI                                                     #
#-------------------------------------------------------------------#

def cocher(s,tab_s):
    s_=''
    for i in range(0,len(s),1):
        var_bool=False
        for j in range(0,len(tab_s),1):
            if (i<=tab_s[j][1]) and (i>=tab_s[j][0]):
                s_+='@'
                var_bool=True
        if var_bool == False:
            s_+=s[i]
    return s_

def det_fonction_1(s,f1):
    tab_f1=[]
    for i in range(0,len(s)-2,1):
        for j in range(0,len(f1),1):
            if (s[i],s[i+1],s[i+2]) == (f1[j][0],f1[j][1],f1[j][2]):
                tab_f1.append((i,i+2,f1[j]))
    return tab_f1

def det_fonction_2(s,f2):
    tab_f2=[]
    for i in range(0,len(s)-1,1):
        for j in range(0,len(f2),1):
            if (s[i],s[i+1]) == (f2[j][0],f2[j][1]):
                tab_f2.append((i,i+1,f2[j]))
    return tab_f2

def det_constante_1(s,c1):
    tab_c1=[]
    for i in range(0,len(s)-1,1):
        for j in range(0,len(c1),1):
            if (s[i],s[i+1]) == (c1[j][0],c1[j][1]):
                tab_c1.append((i,i+1,c1[j]))
    return tab_c1

def det_constante_2(s,c2):
    tab_c2=[]
    for i in range(0,len(s),1):
        for j in range(0,len(c2),1):
            if (s[i]) == (c2[j][0]):
                tab_c2.append((i,i,c2[j][0]))
    return tab_c2

def det_variable_x(s,v):
    tab_v=[]
    for i in range(0,len(s),1):
        for j in range(0,len(v),1):
            if (s[i]) == (v[j][0]):
                tab_v.append((i,i,v[j][0]))
    return tab_v

def det_parenthese(s,par):
    tab_par=[]
    for i in range(0,len(s),1):
        for j in range(0,len(par),1):
            if (s[i]) == (par[j][0]):
                tab_par.append((i,i,par[j][0]))
    return tab_par

def det_operation(s,op):
    tab_op=[]
    for i in range(0,len(s),1):
        for j in range(0,len(op),1):
            if (s[i]) == (op[j][0]):
                tab_op.append((i,i,op[j][0]))
    return tab_op

def det_nombre(s,tab_s):
    tab_n=[[]]
    tab_i=[[]]
    for i in range(0,len(s),1):
        if (s[i] == '@') and  (len(tab_n[len(tab_n)-1])>0):
            tab_n.append([])
            tab_i.append([])
            
        if s[i] != '@':
            tab_n[len(tab_n)-1].append(s[i])
            tab_i[len(tab_i)-1].append(i)
    if len(tab_n[len(tab_n)-1]) == 0:
        tab_n.remove(tab_n[len(tab_n)-1])
        tab_i.remove(tab_i[len(tab_i)-1])

    for i in range(0,len(tab_i),1):
        tab_i[i].append(tab_i[i][0])
        tab_i[i].append(float(''.join(tab_n[i])))
        tab_i[i]=tuple(tab_i[i])
    tab_s+=tab_i
    return tab_s

def creat_tab_f(tab_s):
    tab_f=[]
    for i in range(0,len(tab_s),1):
        tab_f.append(tab_s[i][len(tab_s[i])-1])
    return tab_f


def converte_string_to_tab(s):
    #fonction usuelle ------------------------------$
    f1=['tan','cos','sin','abs','fac','flr']
    f2=['ln']
    # constante ------------------------------------$
    c1=['pi']
    c2=['e']
    # variable -------------------------------------$
    v=['x']
    # parenthese -----------------------------------$
    par=['(',')']
    # chiffres et virgule --------------------------$
    ch=['0','1','2','3','4','5','6','7','8','9']+['.']
    # operation ------------------------------------$
    op=['+','-','*','/','^']

    tab_s=[]
    s_=s
    
    tab_s+=det_fonction_1(s_,f1)
    s_=cocher(s_,tab_s)
    tab_s+=det_fonction_2(s_,f2)
    s_=cocher(s_,tab_s)
    tab_s+=det_constante_1(s_,c1)
    s_=cocher(s_,tab_s)
    tab_s+=det_constante_2(s_,c2)
    s_=cocher(s_,tab_s)
    tab_s+=det_variable_x(s_,v)
    s_=cocher(s_,tab_s)
    tab_s+=det_parenthese(s_,par)
    s_=cocher(s_,tab_s)
    tab_s+=det_operation(s_,op)
    s_=cocher(s_,tab_s)
    tab_s=det_nombre(s_,tab_s)

    for i in range(0,len(tab_s),1):
        for j in range(0,len(tab_s)-1,1):
            if tab_s[j][0] > tab_s[j+1][0]:
                tmp=tab_s[j]
                tab_s[j]=tab_s[j+1]
                tab_s[j+1]=tmp

    tab=creat_tab_f(tab_s)

    return tab