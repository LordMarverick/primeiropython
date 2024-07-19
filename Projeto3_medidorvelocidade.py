#Levando em conta a velocidade permitida de 80km em uma rua, o programa determina se
#o infrator levou uma multa leve em caso de 10km, grave entre 11km e 20km ou gravissima 
#em mais de 20km

velocidade - int(input("Digite a velocidade do condutor:"))
velocidade_maxima = 80
if velocidade <= velocidade_maxima:
   print("Você não leva multa, parabéns!")
elif velocidade > velocidade_maxima and velocidade <= velocidade_maxima +10:
   print("Você levou uma multa, leve!")
elif velocidade >= velocidade_maxima + 11 and velocidade <= velocidade_maxima +20:
    print("Você levou multa, grave")
elif velocidade > velocidade_maxima +20:
    print("Você levou uma multa, gravíssima")