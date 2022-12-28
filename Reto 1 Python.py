salariobase, horasextras, bonificaciones = input().split()
salariobase=float(salariobase)
horasextras=float(horasextras)
bonificaciones=float(bonificaciones)
valorhora=salariobase/192
horasextrasf=horasextras*valorhora*1.25
if bonificaciones==1:
    bonificaciones=salariobase*0.05
salariototal=salariobase+horasextrasf+bonificaciones
salariofinal=round(salariototal-(salariototal*0.035+salariototal*0.04+salariototal*0.01),1)
print(salariofinal)