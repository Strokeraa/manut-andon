import re

# Especifique os caminhos completos para os arquivos de entrada e saída
entrada_arquivo = 'C:/manut-andon/manutencao.txt'
saida_arquivo = 'C:/manut-andon/formatado.txt'

# Função para verificar se uma string é uma data no formato dd.mm.yyyy
def eh_data(data_str):
    padrao_data = re.compile(r'\d{2}\.\d{2}\.\d{4}')
    return padrao_data.match(data_str) is not None

# Função para processar os dados
def formatar_dados(entrada, saida):
    with open(entrada, 'r') as f:
        linhas = f.readlines()
    
    with open(saida, 'w') as f:
        for linha in linhas:
            # Remover barras duplas '||'
            linha = linha.replace('||', '|')
            
            # Dividir a linha por '|'
            partes = linha.split('|')
            
            # Remover a terceira coluna (índice 2)
            if len(partes) > 2:
                partes.pop(2)
            
            # Se a linha começar com 'A', remover a coluna com valor '00.00.0000  00:00:00'
            if partes[0].startswith('A'):
                partes = [parte for parte in partes if parte != '00.00.0000  00:00:00']
            
            # Se a linha começar com 'O' e a sexta coluna for uma data, mover a data para a sétima coluna
            if partes[0].startswith('O') and len(partes) > 5 and eh_data(partes[5]):
                data = partes[5]
                partes[5] = ''  # Colocar uma coluna vazia na sexta posição
                partes.insert(6, data)  # Inserir a data na sétima posição
            
            # Se a linha começar com 'W' e as colunas 7 e 8 forem '00.00.0000  00:00:00', remova-as
            if partes[0].startswith('W') and len(partes) > 7 and partes[6] == '00.00.0000  00:00:00' and partes[7] == '00.00.0000  00:00:00':
                del partes[6:8]
            
            # Remover as duas últimas barras '|', se a penúltima parte estiver vazia
            if len(partes) >= 2 and partes[-2] == '':
                partes.pop()
                partes.pop()
            
            # Rejuntar as partes restantes
            linha_formatada = '|'.join(partes) + '\n'
            
            # Escrever a linha formatada no arquivo de saída
            f.write(linha_formatada)

# Executar a função
formatar_dados(entrada_arquivo, saida_arquivo)
print("sucesso")
