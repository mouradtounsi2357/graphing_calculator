
from Erreur_expression_mathematique import VAR_expression
from Convert_str_to_tab import converte_string_to_tab
from Calcul import calcul

def fonction(fonction_expression,input_x,detail_erreur):
    if VAR_expression(fonction_expression,detail_erreur):
        tab=converte_string_to_tab(fonction_expression)
        output=calcul(tab,input_x)
        return output
    return "Error"