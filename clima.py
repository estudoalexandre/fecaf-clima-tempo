import time  # Importa a biblioteca time para manipulação de tempo
from selenium import webdriver  # Importa o webdriver do Selenium para automação de navegadores
from selenium.webdriver.common.keys import Keys  # Importa Keys do Selenium para simular pressionamento de teclas
from selenium.webdriver.common.by import By  # Importa By do Selenium para localizar elementos na página
from openpyxl import load_workbook  # Importa load_workbook do openpyxl para manipulação de arquivos Excel
from datetime import datetime  # Importa datetime para manipulação de datas e horas


class HistoricoTemperatura:
    # Inicializando a classe com o arquivo Excel e a planilha
    def __init__(self):
        self.arquivo_excel = 'historico_temperatura.xlsx'
        self.planilha_nome = 'temperatura'

    # Inicializando o navegador Chrome, abrindo o Google e pesquisando a temperatura atual
    def iniciar_navegador(self):
        self.navegador = webdriver.Chrome()  # Inicia o navegador
        self.navegador.get('https://www.google.com/')  # Abre o Google
        time.sleep(1)
        
        # Localizando o campo de pesquisa e inserindo o texto
        campo_pesquisa = self.navegador.find_element(By.XPATH, '//*[@id="APjFqb"]')
        campo_pesquisa.send_keys('temperatura atual')
        time.sleep(1)
        
        # Localiza o boao de pesquisa e clica no botão "Enter"
        botao_pesquisa = self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]')
        botao_pesquisa.send_keys(Keys.ENTER)
        time.sleep(1)

    # Carregar o arquivo Excel e a planilha
    def carregar_planilha(self):
        self.workbook = load_workbook(self.arquivo_excel)
        self.planilha = self.workbook[self.planilha_nome]
    
    
    # Obter a próxima linha vazia
    def proxima_linha(self):
        return self.planilha.max_row + 1
    
    # Obter a data e hora atual para preencher na planilha
    def obter_data_hora_atual(self):
        self.data_hora_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"Data e hora atual: {self.data_hora_atual}")
    
    # Obter a temperatura atual do Google
    def obter_temperatura_atual(self):
        # Pega o conteúdo do innerHTML do elemento
        self.temperatura = self.navegador.find_element(By.XPATH, '//*[@id="wob_tm"]').get_attribute('innerHTML')
        try:
            self.temperatura = int(self.temperatura)
        except:
            self.temperatura = None
        print(f"Temperatura atual: {self.temperatura}°C")
        
    # Obter o alerta de umidade
    def obter_alerta_umidade(self):
        self.alerta_umidade = self.navegador.find_element(By.XPATH, '//*[@id="wob_wc"]/div[4]/div[1]').get_attribute('innerHTML')
        print(f"Alerta de umidade: {self.alerta_umidade}")
    
    # Salvar os dados na planilha
    def salvar_dados(self):
        
        linha_atual = self.proxima_linha()
        self.planilha.cell(row=linha_atual, column=1).value = self.data_hora_atual
        self.planilha.cell(row=linha_atual, column=2).value = self.temperatura
        self.planilha.cell(row=linha_atual, column=3).value = self.alerta_umidade
    
    # Salvar o arquivo Excel
    def salvar_arquivo(self):
        # Salvar o arquivo Excel
        self.workbook.save(self.arquivo_excel)
        

# Criar uma instância da classe
historico = HistoricoTemperatura()
# Iniciar o navegador
historico.iniciar_navegador()
# Carregar a planilha
historico.carregar_planilha()
# Obter a temperatura atual
historico.obter_temperatura_atual()
# Salvar a data e hora na próxima linha disponível
historico.obter_data_hora_atual()
# Obter o alerta de umidade
historico.obter_alerta_umidade()
# Salvar os dados na planilha
historico.salvar_dados()
# Salvar o arquivo Excel
historico.salvar_arquivo()

        
# navegador = webdriver.Chrome()  # Instancia o navegador Chrome
# arquivo_excel = load_workbook('historico_temperatura.xlsx')  # Carrega o arquivo Excel
# planilha = arquivo_excel['temperatura']  # Seleciona a planilha 'temperatura'

# proxima_linha = planilha.max_row + 1  # Obtém a próxima linha vazia

# data_hora_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Obtém a data e hora atual


# planilha.cell(row=proxima_linha, column=1).value = data_hora_atual  # Insere a data e hora atual na célula A1

# arquivo_excel.save('historico_temperatura.xlsx')  # Salva o arquivo Excel
