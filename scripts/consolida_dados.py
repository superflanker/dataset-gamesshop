"""
    Autor: Augusto Mathias Adams <superflankerCTBA@gmail.com>
    Copyright 2014-2024 Augusto Mathias Adams
"""
import pandas as pd
import os

def consolida_dados(diretorio: str, 
                    arquivo_saida: str ="../data/processed_data/Magelanium_Consolidated_Sales_data.csv"):
    """
        Consolida os dados das tabelas de vendedores
        Args:
            diretorio (str): diretório que contém os arquivos csv de entrada, separados por vendedor
            arquivo_saida (str): nome do arquivo consolidado, em formato csv
        Returns:
            None
    """
    # Listar todos os arquivos CSV no diretório
    lista_arquivos = [os.path.join(diretorio, f) for f in os.listdir(diretorio) if f.endswith(".csv")]
    
    if not lista_arquivos:
        print("Nenhum arquivo CSV encontrado no diretório.")
        return

    tabelas = []

    # juntando tudo na mesma tabela - já verifiquei e os campos são os mesmos
    # não é necessária transformação de dados no momento

    for arquivo in lista_arquivos:
        df = pd.read_csv(arquivo)
        tabelas.append(df)
    
    tabela_consolidada = pd.concat(tabelas, ignore_index=True)
    
    tabela_consolidada.to_csv(arquivo_saida, index=False)
    print(f"Tabela consolidada salva como {arquivo_saida}")


diretorio = "../data/raw_data/"
consolida_dados(diretorio)
