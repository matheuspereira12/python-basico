# Solicita o caminho de um arquivo MP3 e reproduz o áudio informado; há um arquivo de demonstração disponível na pasta assets.

from playsound3 import playsound

caminho_mp3 = input("Digite o caminho do arquivo MP3:\n")
playsound(caminho_mp3)
