# -*- coding: utf-8 -*-
import sys
from lib.meupia_libs import *

dados = 0
labels = 0
alt = 0
i = 0
def main():
    print("Iniciando Missão IA...")
    dados = [[100, 1], [200, 0]]
    labels = [1, 0]
    ia_definir_dados(dados, labels)
    ia_treinar(dados, labels)
    print("Dado[0][0]: ")
    print(dados[0][0])
    ksp_conectar()
    for i in range(1, 5 + 1, 1):
        alt = ksp_obter_altitude()
        print("Altitude: ")
        print(alt)
        if alt>5000:
            print("Ativando estágio!")
            ksp_ativar_estagio()

if __name__ == '__main__':
    main()