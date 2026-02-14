from IA_API import perguntar_api, saida
from IA_voz import saida_voz
from IA_entrada import ouvir_fala

while True:

    texto = ouvir_fala("pt-BR") # digite dentro da função a sua lingua como o modelo mosta. 
    if texto.lower() in ["sair", "exit"]:
        break
    response = perguntar_api(texto)
    resposta = saida(response)

    saida_voz(resposta)






