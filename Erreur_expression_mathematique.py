#!/usr/bin/python3
#-------------------------------------------------------------------#
# MOURAD TOUNSI                                                     #
#-------------------------------------------------------------------#

# vérifier les parenthèses -----------------------------------------$
def var_par(s):
    compt=0
    for i in range(0,len(s),1):
        if s[i]=='(':
            compt+=1
        if s[i]==')':
            compt-=1
        if compt < 0:
            return False
    if compt > 0:
        return False
    else :
        return True

# vérifier si aux plus deux opérations sont liés -------------------$
def var_operation_suc(s):
    operation=['+','-','*','/','^']
    for i in range(0,len(s)-1,1):    
        for j in range(0,len(operation),1):
            for  k in range(0,len(operation),1):
                if (s[i],s[i+1]) == (operation[j],operation[k]):
                    return False
    return True

# vérifier si l'expression début ou finit par une opération --------$
def var_operation_fd(s):
    operation=['*','/','^']
    op=['+','-']
    for i in range(0,len(operation),1):
        if len(s) != 0:
            if s[0]==operation[i] or s[len(s)-1]==operation[i]:
                return False
    
    for i in range(0,len(op),1):
        if len(s) != 0:
            if s[len(s)-1]==op[i]:
                return False
    return True

# vérifier l'emplacement des opérations et les parenthèses ---------$
def var_op_par(s):
    operation=['+','*','/','^']
    for i in range(0,len(s)-1,1):
        for j in range(0,len(operation),1):
            if (s[i],s[i+1]) == (operation[j],')') or (s[i],s[i+1]) == ('(',operation[j]):
                return False
    for i in range(0,len(s)-1,1):
        if (s[i],s[i+1]) == ('-',')'):
            return False
    return True

# vérifier s'il y a des parenthèses vides ou mal placées -----------$
def var_parenthese_vide_dif(s):
    for i in range(0,len(s)-1,1):
        if (s[i],s[i+1]) == ('(',')') or (s[i],s[i+1]) == (')','('):
            return False
    return True

# vérifier le symbole qui est devant une fonction ------------------$
def var_fonction_par_ouv(s,f1,f2):
    for  i in range(0,len(s)-3,1):
        for j in range(0,len(f1),1):
            if (s[i],s[i+1],s[i+2]) == (f1[j][0],f1[j][1],f1[j][2]):
                if (s[i],s[i+1],s[i+2],s[i+3]) != (f1[j][0],f1[j][1],f1[j][2],'('):
                    return False
    for i in range(0,len(s)-2,1):
        for j in range(0,len(f2),1):
            if (s[i],s[i+1]) == (f2[j][0],f2[j][1]):
                if (s[i],s[i+1],s[i+2]) != (f2[j][0],f2[j][1],'('):
                    return False
    return True

# vérifier si une expression n'est pas terminée par une fonction ---$
def var_fonction_fin(s,f1,f2):
    if len(s) >= 3:
        for i in range(0,len(f1),1):
            if (s[len(s)-3],s[len(s)-2],s[len(s)-1]) == (f1[i][0],f1[i][1],f1[i][2]):
                return False
    if len(s) >= 2:
        for i in range(0,len(f2),1):
            if (s[len(s)-2],s[len(s)-1]) == (f2[i][0],f2[i][1]):
                return False
    return True

# vérifier le symbole qui est derrière une fonction ----------------$
def var_fonction_deb(s,f1,f2):
    sym=['+','-','*','/','^','(']
    for i in range(0,len(s)-3,1):
        for j in range(0,len(f1),1):
            if (s[i+1],s[i+2],s[i+3]) == (f1[j][0],f1[j][1],f1[j][2]):
                var_bool=False
                for k in range(0,len(sym),1):
                    if s[i] == sym[k]:
                        var_bool=True
                if var_bool == False:
                    return False
    for i in range(0,len(s)-2,1):
        for j in range(0,len(f2),1):
            if (s[i+1],s[i+2]) == (f2[j][0],f2[j][1]):
                var_bool=False
                for k in range(0,len(sym),1):
                    if s[i] == sym[k]:
                        var_bool=True
                if var_bool == False:
                    return False
    
    return True

# vérifier le symbole qui est devant ou derrière une constante -----$
def var_constante_dvdr(s,c1,c2):
    sym_dr=['+','-','*','/','^','(']
    for i in range(0,len(s)-2,1):
        for j in range(0,len(c1),1):
            if (s[i+1],s[i+2]) == (c1[j][0],c1[j][1]):
                var_bool=False
                for k in range(0,len(sym_dr),1):
                    if s[i] == sym_dr[k]:
                        var_bool=True
                if var_bool == False:
                    return False
    for i in range(0,len(s)-1,1):
        for j in range(0,len(c2)):
            if (s[i+1]) == (c2[j]):
                var_bool=False
                for k in range(0,len(sym_dr),1):
                    if s[i] == sym_dr[k]:
                        var_bool=True
                if var_bool == False:
                    return False
    
    sym_dv=['+','-','*','/','^',')']
    for i in range(0,len(s)-2,1):
        for  j in range(0,len(c1),1):
            if (s[i],s[i+1]) == (c1[j][0],c1[j][1]):
                var_bool=False
                for k in range(0,len(sym_dv),1):
                    if s[i+2] == sym_dv[k]:
                        var_bool=True
                if var_bool == False:
                    return False
    for i in range(0,len(s)-1,1):
        for j in range(0,len(c2)):
            if (s[i]) == (c2[j]):
                var_bool=False
                for k in range(0,len(sym_dv)):
                    if s[i+1] == sym_dv[k]:
                        var_bool=True
                if var_bool == False:
                    return False

    return True

# vérifier le symbole qui est devant ou derrière la variable x -----$
def var_variable_dvdr(s,v):
    sym_dr=['+','-','*','/','^','(']
    for i in range(0,len(s)-1,1):
        if (s[i+1]) == (v[0]):
            var_bool=False
            for k in range(0,len(sym_dr),1):
                if s[i] == sym_dr[k]:
                    var_bool=True
            if var_bool == False:
                return False
    
    sym_dv=['+','-','*','/','^',')']
    for i in range(0,len(s)-1,1):
        if (s[i]) == (v[0]):
            var_bool=False
            for k in range(0,len(sym_dv),1):
                if s[i+1] == sym_dv[k]:
                    var_bool=True
            if var_bool == False:
                return False

    return True

# vérifier le symbole qui est devant ou derrière un chiffre --------$
def var_chiffre_dvdr(s,ch):
    sym_dr=['+','-','*','/','^','(']+ch+['.']
    #print(sym_dr)
    for i in range(0,len(s)-1,1):
        for j in range(0,len(ch),1):
            if (s[i+1]) == (ch[j]):
                var_bool=False
                for k in range(0,len(sym_dr),1):
                    if s[i] == sym_dr[k]:
                        var_bool=True
                if var_bool == False:
                    return False
    
    sym_dv=['+','-','*','/','^',')']+ch+['.']
    for i in range(0,len(s)-1,1):
        for j in range(0,len(ch),1):
            if (s[i]) == (ch[j]):
                var_bool=False
                for k in range(0,len(sym_dv),1):
                    if s[i+1] == sym_dv[k]:
                        var_bool=True
                if var_bool == False:
                    return False

    return True

# vérifier si une expression n'est pas seulement une virgule -------$
def var_virgule_singleton(s,point):
    if len(s) == 1:
        if s[0] == point[0]:
            return False
    return True

# vérifier si deux virgules sont séparées --------------------------$
def var_double_virgule(s):
    for i in range(0,len(s)-1,1):
        if (s[i],s[i+1]) == ('.','.'):
            return False
    return True

# vérifier si une virgule n'est pas associée à un nombre -----------$
def var_virgule_seul(s,point,ch):
    if len(s) >= 2:
        if s[0] == point[0]:
            var_bool=False
            for j in range(0,len(ch),1):
                if s[1] == ch[j]:
                    var_bool=True
            if var_bool == False:
                return False
        if s[len(s)-1] == point[0]:
            var_bool=False
            for j in range(0,len(ch),1):
                if s[len(s)-2] == ch[j]:
                    var_bool=True
            if var_bool == False:
                return False

    for i in range(0,len(s)-2,1):
        if s[i+1] == point[0]:
            var_bool=False
            for j in range(0,len(ch),1):
                if s[i] == ch[j] or s[i+2] == ch[j]:
                    var_bool=True
            if var_bool == False:
                return False
    return True

# vérifier s'il y a aux plus deux virgules dans un même nombre ------$
def var_virgule_au_plus(s,point,ch):
    tab_point=[]
    for i in range(0,len(s),1):
        if s[i] == point[0]:
            tab_point.append(i)
    for i in range(0,len(tab_point)-1,1):
        tab_var=[0]*(tab_point[i+1]-tab_point[i]-1)
        compt_tab_var=0
        sum_bool=1
        for j in range(tab_point[i]+1,tab_point[i+1],1):
            for k in range(0,len(ch),1):
                if s[j] == ch[k]:
                    tab_var[compt_tab_var]=1
                    compt_tab_var+=1
        for l in range(0,len(tab_var),1):
            sum_bool*=tab_var[l]
        if sum_bool == 1:
            return False 
    return True

# vérifier s'il y a un symbole non autorisé ------------------------$
def var_symbole(s,f1,f2,c1,c2,v,ch,point):
    tab_rmp=[]
    # pour les fonctions (2/3 charater) ----------------------------$
    for i in range(0,len(s)-2,1):
        for j in range(0,len(f1),1):
            if (s[i],s[i+1],s[i+2]) == (f1[j][0],f1[j][1],f1[j][2]):
                tab_rmp.append((i,i+2))
    for i in range(0,len(s)-2,1):
        for j in range(0,len(f2),1):
            if (s[i],s[i+1]) == (f2[j][0],f2[j][1]):
                tab_rmp.append((i,i+1))
    # pour les constante (1/2 character) ---------------------------$
    for i in range(0,len(s)-1,1):
        for j in range(0,len(c1),1):
            if (s[i],s[i+1]) == (c1[j][0],c1[j][1]):
                tab_rmp.append((i,i+1))
    for i in range(0,len(s),1):
        for j in range(0,len(c2),1):
            if s[i] == c2[j]:
                tab_rmp.append((i,i))
    # pour la variable x -------------------------------------------$
    for i in range(0,len(s),1):
        if s[i] == v[0]:
            tab_rmp.append((i,i))
    # pour les chiffres --------------------------------------------$
    for i in range(0,len(s),1):
        for j in range(0,len(ch),1):
            if s[i] == ch[j]:
                tab_rmp.append((i,i))
    # pour la virgule ----------------------------------------------$
    for  i in range(0,len(s),1):
        if s[i] == point[0]:
            tab_rmp.append((i,i))
    # pour les operations ------------------------------------------$
    operation=['+','-','*','/','^']
    for i in range(0,len(s),1):
        for j in range(0,len(operation),1):
            if s[i] == operation[j]:
                tab_rmp.append((i,i))
    # pour les parenheses ------------------------------------------$
    for  i in range(0,len(s),1):
        if s[i] == '(' or s[i] == ')':
            tab_rmp.append((i,i))
    # verifier les symbole de l'expression s -----------------------$
    for i in range(0,len(s),1):
        var_bool=False
        for j in range(0,len(tab_rmp),1):
            if (i <= tab_rmp[j][1]) and (i >= tab_rmp[j][0]):
                var_bool=True
        if var_bool == False:
            return False
    return True

# vérifier l'expression mathématique -------------------------------$
def VAR_expression(s,detail):
    #fonction usuelle ------------------------------$
    f1=['tan','cos','sin','abs','fac','flr']
    f2=['ln']
    # constante ------------------------------------$
    c1=['pi']
    c2=['e']
    # variable -------------------------------------$
    v=['x']
    # chiffres -------------------------------------$
    ch=['0','1','2','3','4','5','6','7','8','9']
    # virgule --------------------------------------$
    point=['.']

    if detail:
        print("VAR parentheses                             :  ", var_par(s))
        print("VAR deux operations successif               :  ", var_operation_suc(s))
        print("VAR operations fin et debut                 :  ", var_operation_fd(s))
        print("VAR operations et parentheses               :  ", var_op_par(s))
        print("VAR parenthese vide ou differente           :  ", var_parenthese_vide_dif(s))
        
        print("VAR fonction et parenthese ouverte          :  ", var_fonction_par_ouv(s,f1,f2))
        print("VAR fonction a la fin                       :  ", var_fonction_fin(s,f1,f2))
        print("VAR fonction au debut                       :  ", var_fonction_deb(s,f1,f2))

        print("VAR derrier et devant une constante         :  ", var_constante_dvdr(s,c1,c2))

        print("VAR derrier et devant une variable          :  ", var_variable_dvdr(s,v))

        print("VAR derrier et devant une chiffre           :  ", var_chiffre_dvdr(s,ch))

        print("VAR une virgule dans un singleton           :  ",var_virgule_singleton(s,point))
        print("VAR une double virgule                      :  ",var_double_virgule(s))
        print("VAR une virgule seule                       :  ",var_virgule_seul(s,point,ch))
        print("VAR au plus deux variable dans un nombre    :  ",var_virgule_au_plus(s,point,ch))

        print("VAR symboles autorises                      :  ",var_symbole(s,f1,f2,c1,c2,v,ch,point))
    
    # var_par(s) var_operation_suc(s) var_operation_fd(s) var_op_par(s) var_parenthese_vide_dif(s) 
    # var_fonction_par_ouv(s,f1,f2) var_fonction_fin(s,f1,f2) var_fonction_deb(s,f1,f2)
    # var_constante_dvdr(s,c1,c2) var_variable_dvdr(s,v) var_chiffre_dvdr(s,ch)
    # var_virgule_singleton(s,point) var_double_virgule(s) var_virgule_seul(s,point,ch)
    # var_virgule_au_plus(s,point,ch) var_symbole(s,f1,f2,c1,c2,v,ch,point)

    if var_par(s) and var_operation_suc(s) and var_operation_fd(s) and var_op_par(s) and var_parenthese_vide_dif(s) and var_fonction_par_ouv(s,f1,f2) and var_fonction_fin(s,f1,f2) and var_fonction_deb(s,f1,f2) and var_constante_dvdr(s,c1,c2) and var_variable_dvdr(s,v) and var_chiffre_dvdr(s,ch) and var_virgule_singleton(s,point) and var_double_virgule(s) and var_virgule_seul(s,point,ch) and var_virgule_au_plus(s,point,ch) and var_symbole(s,f1,f2,c1,c2,v,ch,point):
        if detail:
            print("\nVAR expression                              : [",True,"]")
        return True
    else:
        if detail:
            print("\nVAR expression                              : [",False,"]")
        return False
#fin