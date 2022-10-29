def jogarforca():
  import random
  from time import sleep

  usuario = input("Digite seu nome: ")
 
  print(f"Bem vindo ao jogo da Forca, {usuario}!")
  sleep(2)
  print("A regra é clara: você só tem 6 chances de errar a letra.")
  sleep(2)
  print("As palavras estão relacionadas a comida. Boa sorte!")
  sleep(2)
 
  palavras_forca = ["laranja","acerola","melancia","uva","pera","melao","pitanga","tangerina","arroz","feijao","macarrao",
                    "brocolis","pure","cenoura","alface","azeite","ovo","pao","leite","refrigerante","aveia","frango",
                    "carne","picanha","vinagrete","camarao","peixe","lagosta","camarao","suco","limao","queijo"] 
  
  numero = random.randrange(0,len(palavras_forca))
  palavra_secreta = palavras_forca[numero].upper()

  letras_acertadas = ["_" for letra in palavra_secreta]
  enforcou = False
  acertou = False
  tentativas = 0

  print(letras_acertadas)

  while(not enforcou and not acertou):      
    chute = input("Qual a letra?: ")
    chute = chute.strip().upper()
    if (chute in palavra_secreta):
      i = 0
      for letra in palavra_secreta:
        if chute.upper() == letra.upper():
          letras_acertadas[i] = letra
        i += 1
    else:
      print(f"Não tem essa letra: {chute}")
      tentativas += 1
      
    enforcou = tentativas == 6
    acertou = "_" not in letras_acertadas
    print(letras_acertadas)

  if (acertou):
    print("Você acertou!")
  else:
    print("Suas chances acabaram :(")
    
  print(letras_acertadas)

jogarforca()

