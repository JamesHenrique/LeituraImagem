
import pytesseract
import cv2
import pandas as pd
import openpyxl
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


#função para extrair texto da imagem
def extract_img(img):
        
    imagem = cv2.imread(img)

    texto = pytesseract.image_to_string(imagem)
    
    return texto



# Função para extrair campos específicos do texto
def extract_text(texto):
    linhas = texto.split('\n')
    data_pagamento = None
    valor_total = None

    for linha in linhas:
        if "Data do pagamento" in linha:
            data_pagamento = linha.split("Data do pagamento")[1].strip()
        elif "Valor Total" in linha:
            valor_total = linha.split("Valor Total")[1].strip()

    return data_pagamento, valor_total


#função para percorrer a lista de arquivos e salvar os campos em excel
def main(folder):
    
    file_path = os.listdir(folder)
    dados = []
    for files in file_path:
        if '.jpg' in files:
            print(f'arquivo aberto {files}')
            arq_img = os.path.join(folder, files)
            text = extract_img(arq_img)
            data, valor = extract_text(text)
            if data and valor:
                dados.append({
                    'data_pagamento':data, 
                    'valor':valor
                })
        else:
           pass
       
    df = pd.DataFrame(dados)

    df.to_excel('dados_extracao.xlsx', index=False)

    print("Dados salvos em 'dados_extracao.xlsx'")   





