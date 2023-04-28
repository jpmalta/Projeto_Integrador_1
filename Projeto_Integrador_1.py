# Projeto Integrador 1

def do_again():
    response = int(input("Gostaria de rodar novamente? [0 - SIM | 1 - NÃO]: "))
    while True:
        try:
            if (response == 0):
                user_input()
            elif (response == 1):
                print("\n\n\n\nOBRIGADO POR USAR O PROJETO INTEGRADOR 1 DO GRUPO 7\n\n\n\n")
                exit()  
                
        except ValueError:
            print("Digite 0 - SIM ou 1 - NÃO")

def user_input():
    while True:
        try:
            mp10 = float(input("Digite o valor do MP10: "))
            mp25 = float(input("Digite o valor do MP2,5: "))
            o3 = float(input("Digite o valor do Ozonio: "))
            co = float(input("Digite o valor do CO: "))
            no2 = float(input("Digite o valor do NO2: "))
            so2 = float(input("Digite o valor do SO2: "))
            classificacao(mp10,mp25,o3,co,no2,so2)
        except ValueError:
            print("\n\n[Digite novamente um valor válido]\n\n")

def classificacao(mp10,mp25,o3,co,no2,so2):
    #Verifica se os valores das variáveis são válidos
    try:
        if(mp10 > -1 and mp25 > -1 and o3 > -1 and co > -1 and no2 > -1 and so2 > -1):
            #Verifica a classificação do ar
            if mp10 <= 50 and mp25 <= 25 and o3 <= 100 and co <= 9 and no2 <= 200 and so2 <= 20:
                print("\n\nQualidade do ar: Boa\n\n")
            elif mp10 <= 100 and mp25 <= 50 and o3 <= 130 and co <= 11 and no2 <= 240 and so2 <= 40:
                print("\n\nQualidade do ar: Moderada - Pessoas de grupos sensível (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar sintomas como tosse seca e cansaço. A população, em geral, não é afetada.\n\n")
            elif mp10 <= 150 and mp25 <= 75 and o3 <= 160 and co <= 13 and no2 <= 320 and so2 <= 365:
                print("\n\nQualidade do ar: Ruim - Toda a população pode apresentar sintomas como tosse seca, cansaço ardor nos olhos, nariz e garganta. Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar efeitos mais sérios na saúde.\n\n")
            elif mp10 <= 250 and mp25 <= 125 and o3 <= 200 and co <= 15 and no2 <= 1130 and so2 <= 800:
                print("\n\nQualidade do ar: Muito Ruim - Toda a população pode apresentar agravamento dos sintomas como tosse seca, cansaço ardor nos olhos, nariz e garganta e ainda falta de ar e respiração ofegante. Efeitos ainda mais graves à saúde de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas).\n\n")
            elif mp10 >= 250 or mp25 >= 125 or o3 >= 200 or co >= 15 or no2 >= 1130 or so2 >= 800:
                print("\n\nQualidade do ar: Pessima - Toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares. Aumento de mortes prematuras em pessoas de grupos sensíveis.\n")
            else:
                print("\n\n[Valor digitado não possui categoria]\n\n")
                user_input()
        else:
            print("\n\n[Digite novamente um valor válido]\n\n")
            user_input()

        do_again()

    except ValueError:
        print("\n\n[Digite novamente um valor válido]\n\n")
        user_input()

print("SEJA BEM VINDO AO PROJETO INTEGRADOR 1\n\nDigite os valores para classificar a qualidade de ar\n")

while True:
    try:
        mp10 = float(input("Digite o valor do MP10: "))
        mp25 = float(input("Digite o valor do MP2,5: "))
        o3 = float(input("Digite o valor do Ozonio: "))
        co = float(input("Digite o valor do CO: "))
        no2 = float(input("Digite o valor do NO2: "))
        so2 = float(input("Digite o valor do SO2: "))
        classificacao(mp10,mp25,o3,co,no2,so2)
    except ValueError:
        print("\n\n[Digite novamente um valor válido]\n\n")
        user_input()