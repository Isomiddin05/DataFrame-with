# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11fXD92vojDQtmM7rn7UbpsTO5LpW68_g
"""

import pandas as pd
baza={
    "FISH":['Aliyeva Rano','Valiyev Vali','arslonov vohid','qodirov toshmat','ermatova x','ahmedova','Jeparova','durov','messixon','Ronaldobe'],
    "Yoshi":["11","15",'12','33','34','21','15','23','43','19'],
    "Maktabi":["11","Prezident maktabi",'22','22','36','66','77','99','22','22'],
    "jinsi":['qiz bola',"erkak","erkak","erkak","ayol","ayol","ayol","erkak","erkak","erkak"],
    "manzili":["Andijon","Fargona","Namangan",'Toshkent','Trabzon',"Istanbul","Asaka","Moskva","Buenes-ayres","Lissabon"]
    }
db=pd.DataFrame(baza)
print(db)

filtr=db[(db["Maktabi"]=='22')&(db[ "jinsi" ]=="erkak")]
print (filtr)