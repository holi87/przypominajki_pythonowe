'''

Tutaj będe wrzucał różne funkcje związane z datami

'''
from datetime import date

dzien_tygodnia = date.today().strftime('%A')  # małe a zrobi skrócony dzień tygodnia
data_dzisiejsza = date.today()

print("Today is %s, %s" % (dzien_tygodnia, data_dzisiejsza))
