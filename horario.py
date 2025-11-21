import os
import json

class Horarios:
    def mostrar_horarios(self, dados):
        for horario in dados:
            print("")
            print("Horário:")
            print("Nome:", horario["nome"])
            print("Telefone:", horario["telefone"])
            print("Data:", horario["horario"]["data"])
            print("Hora:", horario["horario"]["hora"])
            print()


    