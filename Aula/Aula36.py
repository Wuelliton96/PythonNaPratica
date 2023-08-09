'''
Como mover, copiar, apagar arquivos
'''
import os
import shutil

caminho_original = ''
caminho_novo = ''

try:
    os.mkdir(caminho_novo)
except FileNotFoundError as e:
    print(f'Pasta {caminho_novo} já existe.')

for root, dirs, files in os.walk(caminho_novo):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path =  os.path.join(caminho_novo, file)

        if '.srt' in file:
            os.remove(new_file_path)
