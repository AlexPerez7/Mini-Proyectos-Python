import calendar
from pathlib import Path # Sirve para crear carpetas

# calendar.month_name[mes] devuelve el nombre del mes
meses_anio = (list(calendar.month_name[1:]))

# 
dia_mes = ['Dia 1', 'Dia 2', 'Dia 3', 'Dia 4', 'Dia 5', 'Dia 6', 'Dia 7', 'Dia 8', 'Dia 9', 'Dia 10', 'Dia 11', 'Dia 12', 'Dia 13', 'Dia 14', 'Dia 15', 'Dia 16', 'Dia 17', 'Dia 18', 'Dia 19', 'Dia 20', 'Dia 21', 'Dia 22', 'Dia 23', 'Dia 24', 'Dia 25', 'Dia 26', 'Dia 27', 'Dia 28', 'Dia 29', 'Dia 30', 'Dia 31']

for i, mes in enumerate(meses_anio):
    for dia in dia_mes:
        Path(f'2022/{i+1}.{mes}/{dia}').mkdir(parents=True, exist_ok=True) #Parents sirve para crear carpetas padre