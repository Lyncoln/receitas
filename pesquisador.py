# -*- coding: utf-8 -*-
"""
Created on Wed May  1 17:46:14 2019

@author: Lyncoln
"""

import pandas as pd
import numpy as np

receitas = pd.read_csv("https://github.com/Lyncoln/receitas/raw/master/receitas.csv")

def procura(vetor):   
    i = 0
    x = []      
    for item in receitas.ingredientes:
        aux = []
        for arg in vetor:
            if(arg in item):
                aux.append(True)
            else:
                aux.append(False)
        if(False in aux):
            pass
        else:
            x.append(i)
        i = i + 1
    return(x)
        
   
def pesquisado(vetor):
    return(receitas.iloc[vetor].drop(columns="Unnamed: 0").reset_index().drop(columns="index"))

            
            
            
def pesquisa(vetor):
    aux = procura(vetor)
    return(pesquisado(aux))
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            