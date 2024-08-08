None
mem = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            'ROFL':'Una respuesta a una broma',
            'SHEESH':'Ligera desaprobación',
            'CREEPY':'Aterrador, siniestro',
            'AGGRO':'Ponerse agresivo/enojado',
            'YUNIKUA':'Como mi compañero llama a otro compañero'
       }
pepe = input("Escribe una palabra que no entiendas (¡CON MAYÚSCULAS!): ")
if pepe in mem.keys():
    print(mem[pepe])
else:
    print('Lo siento no tenemos esa palabra en nuestro diccionario😢')
