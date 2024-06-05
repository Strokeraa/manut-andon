import shutil

# Caminhos dos arquivos de origem e destino
origem_andon = r"\\192.168.30.27\interfacePRD\andon\manutencao.txt"
destino = r"C:\manut-andon"

# Executa a cópia do arquivo andon.txt
try:
    shutil.copy(origem_andon, destino)
    print("Arquivo manutencao.txt copiado com sucesso!")
except FileNotFoundError:
    print("Arquivo manutencao.txt não encontrado.")