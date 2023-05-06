# Projeto Integrador 1

import mysql.connector
from mysql.connector import Error
import time
import os

# Valor máximo das amostras
max_value = 10000

# Conecta no banco de dados
connection = mysql.connector.connect(host='localhost',
                                        database='projeto_integrador',
                                        user='root',
                                        password='root')
try:
    if connection.is_connected():
        print("Conectado ao banco de dados\n\n")
except Error as e:
    print('Erro ao conectar com o banco de dados')
    print(e)
    raise SystemExit

def clear_terminal():
    os.system('cls')

def query(query, fetchall=False):
    #print(query)
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        if fetchall:
            return cursor.fetchall()
        else:
            return cursor.rowcount and cursor.close() and connection.commit() and connection.close()
        
    except Error as e:
        print('Erro na query')
        print(e)
        raise SystemExit

def check_for_empty_table():
    if query("SELECT COUNT(*) FROM Amostra", True)[0][0] == 0:
        os.system('cls')
        print("\n-------------------------------------")
        print("\n| Não há amostras no banco de dados |\n")
        print("-------------------------------------\n")
        return True

def user_input():
    while True:
        try:
            mp10 = float(input("Digite o valor do MP10: "))
            mp25 = float(input("Digite o valor do MP2,5: "))
            o3 = float(input("Digite o valor do Ozonio: "))
            co = float(input("Digite o valor do CO: "))
            no2 = float(input("Digite o valor do NO2: "))
            so2 = float(input("Digite o valor do SO2: "))
            if mp10 < max_value and mp25 < max_value and o3 < max_value and co < max_value and no2 < max_value and so2 < max_value and mp10 >= 0 and mp25 >= 0 and o3 >= 0 and co >= 0 and no2 >= 0 and so2 >= 0:
                return mp10, mp25, o3, co, no2, so2
            else:
                print("\n\n[Digite novamente um valor válido]\n\n")
        except ValueError:
            print("\n\n[Digite novamente um valor válido]\n\n")

def classify(mp10,mp25,o3,co,no2,so2):
    clear_terminal()
    #Verifica se os valores das variáveis são válidos
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

def menu():
    while True:
        try:
            option = int(input("Digite a opção desejada:\n1 - Inserir amostra\n2 - Mostra TODAS as Amostras\n3 - Mostra Qualidade do Ar\n4 - Deletar amostra\n5 - Alterar Amostra\n6 - Sair\n\nOpção Desejada: "))
            if option == 1:
                try:
                    final_input = user_input()
                    mp10 = final_input[0]
                    mp25 = final_input[1]
                    o3 = final_input[2]
                    co = final_input[3]
                    no2 = final_input[4]
                    so2 = final_input[5]
                    clear_terminal()
                    query(f"INSERT INTO Amostra (mp10, mp25, o3, co, no2, so2) VALUES ({mp10}, {mp25}, {o3}, {co}, {no2}, {so2});")
                    print("\n\n[Amostra inserida com sucesso]\n\n")
                except ValueError:
                    print("\n\n[Digite novamente um valor válido]\n\n")


            elif option == 2:
                if check_for_empty_table() == True:
                    pass
                else:
                    for x in query("SELECT * FROM Amostra", True):
                        time.sleep(2)
                        print(f"_______________\n\n[AMOSTRA: {x[0]}]\n\n|MP10: {x[1]}\n|MP2,5: {x[2]}\n|O3: {x[3]}\n|CO: {x[4]}\n|SO2: {x[5]}\n_______________\n\n")
            

            elif option == 3:
                if check_for_empty_table() == True:
                    pass
                else: 
                    for x in query("SELECT AVG(MP10), AVG(MP25), AVG(O3), AVG(CO), AVG(NO2), AVG(SO2) FROM Amostra;", True):
                        time.sleep(2)
                        classify(x[0],x[1],x[2],x[3],x[4],x[5])
            

            elif option == 4:
                if check_for_empty_table() == True:
                    pass
                else:
                    for x in query("SELECT * FROM Amostra", True):
                        time.sleep(2)
                        print(f"_______________\n\n[AMOSTRA: {x[0]}]\n\n|MP10: {x[1]}\n|MP2,5: {x[2]}\n|O3: {x[3]}\n|CO: {x[4]}\n|SO2: {x[5]}\n_______________\n\n")
                    
                    delete = int(input("Digite o ID da amostra que deseja deletar: "))
                    if query(f"SELECT * FROM Amostra WHERE id = {delete}", True) == []:
                        print("\n\n[Amostra não encontrada]\n\n")
                    else:
                        query(f"DELETE FROM Amostra WHERE id = {delete};")
                        print("\n\n[Amostra deletada com sucesso]\n\n")


            elif option == 5:
                if check_for_empty_table() == True:
                    pass
                else:
                    for x in query("SELECT * FROM Amostra", True):
                        time.sleep(2)
                        print(f"_______________\n\n[AMOSTRA: {x[0]}]\n\n|MP10: {x[1]}\n|MP2,5: {x[2]}\n|O3: {x[3]}\n|CO: {x[4]}\n|SO2: {x[5]}\n_______________\n\n")
                    
                    while True:
                        try:
                            update = int(input("Digite o ID da amostra que deseja alterar: "))
                        except ValueError:
                            print("\n\n[Digite novamente um valor válido]\n\n")
                        else:
                            if query(f"SELECT * FROM Amostra WHERE id = {update}", True) == []:
                                print("\n\n[Amostra não encontrada]\n\n")
                            else:
                                particle_option = ["MP10", "MP25", "O3", "CO", "NO2", "SO2"]
                                break
                    
                    while True:
                        try:
                            option_table = int(input("Digite o número da opção que deseja alterar:\n1 - MP10\n2 - MP2,5\n3 - O3\n4 - CO\n5 - NO2\n6 - SO2\n\nOpção Desejada: "))
                        except ValueError:
                            print("\n\n[Digite novamente um valor válido]\n\n")
                        else:
                            if option_table >= 1 and option_table <= 6:
                                atual = particle_option[option_table - 1]
                                break
                            else:
                                print("\n\n[Digite novamente um valor válido]\n\n")

                    while True:
                        try:
                            value = int(input(f"Digite o novo valor: "))
                        except ValueError:
                            print("\n\n[Digite novamente um valor válido]\n\n")
                        else:
                            if value >= 0:
                                query(f"UPDATE Amostra SET {atual} = {value} WHERE id = {update};")
                                print("\n\n[Amostra alterada com sucesso]\n\n")
                                break


            elif option == 6:
                print("OBRIGADO POR USAR O PROJETO INTEGRADOR 1 DO GRUPO 7")
                exit()

            else:
                clear_terminal()
                print("\nOpção Inexistente, Tente Novamente.\n")
        except ValueError:
            clear_terminal()
            print("\nDigite um NÚMERO válido\n")

print("[SEJA BEM VINDO AO PROJETO INTEGRADOR 1]\n\n")
menu()
