#Variáveis: você não pode começar uma variavel com número, simbolos ou espaço. Use sempre o _ 
#para semparar as palavras. A linguagem python, e case sensitive.

#Números
velocidade_internet = 10 
print(velocidade_internet )
nota_filme = 8.5 #float

#Valores Boleanos
esta_aberto = True

#Strings
nome_do_curso: "Lógica de programação do curso.org"

#Como as variáveis seriam usadas em um programa real?
#Problema 1 - valor por hora
#Escreva um programa que retorna o valor hora de um funcionario
#com base no seu salário mensal e horas trabalhadas no mês. (abaixo e apenas um pseudocodigo)

#input salario_mensal
#input horas_trabalhadas_por_mes
#valor_hora = salario_mensal / horas_trabalhadas_por_mes
#print valor_hora

salario_mensal = input('Qual e o seu salário mensal?')
horas_trabalhadas_por_mes = input('Quantas horas trabalha por mês?')
valor_hora = int(salario_mensal) / int(horas_trabalhadas_por_mes) 
print(valor_hora)