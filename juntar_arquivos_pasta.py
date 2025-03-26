import os
import pandas as pd

# altere esse campo para o caminho da sua pastas
caminho_pasta='C:/Temp/arquivos_base/'

def juntar_arquivos_pasta(caminho_pasta):
# lista todos os arquivos da pasta
    arquivos = os.listdir(caminho_pasta)
    
#cria uma lista para armazenar os dataframes
    lista_df=[]
    
# carrega cada arquivo excel da pasta 
    for arquivo in arquivos: 
        caminho_arquivo = os.path.join(caminho_pasta, arquivo)

# carrega o excel para um dataframe e armazena em uma lista
        df = pd.read_excel(caminho_arquivo)
        lista_df.append(df)

# junta todos os dataframes
        resultado = pd.concat(lista_df, ignore_index=True)

# salva o resultado na mesma pasta
        resultado.to_excel(os.path.join(caminho_pasta, 'resultado.xlsx'), index=False)

        print("arquivos unidos com sucesso!")
        
        juntar_arquivos_pasta(caminho_pasta)