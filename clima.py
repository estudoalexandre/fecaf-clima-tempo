import time  # Importa a biblioteca time para manipulação de tempo
from selenium import webdriver  # Importa o webdriver do Selenium para automação de navegadores
from selenium.webdriver.common.keys import Keys  # Importa Keys do Selenium para simular pressionamento de teclas
from selenium.webdriver.common.by import By  # Importa By do Selenium para localizar elementos na página
from openpyxl import load_workbook  # Importa load_workbook do openpyxl para manipulação de arquivos Excel
from datetime import datetime  # Importa datetime para manipulação de datas e horas

navegador = webdriver.Chrome()  # Instancia o navegador Chrome

arquivo_excel = load_workbook('historico_temperatura.xlsx')  # Carrega o arquivo Excel

planilha = arquivo_excel['temperatura']  # Seleciona a planilha 'temperatura'

proxima_linha = planilha.max_row + 1  # Obtém a próxima linha vazia

data_hora_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Obtém a data e hora atual


planilha.cell(row=proxima_linha, column=1).value = data_hora_atual  # Insere a data e hora atual na célula A1

arquivo_excel.save('historico_temperatura.xlsx')  # Salva o arquivo Excel
