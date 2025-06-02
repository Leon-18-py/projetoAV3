import calculadora # type: ignore
import calculadoraAvancada # type: ignore

num1 = float(input("Digite o número 1: "))
num2 = float(input("Digite o número 2: "))
operacao = input("Digite a operção (+ - / * dobro potência):")

resultado = None

if(operacao == '+'):
 resultado = calculadora.somar(num1, num2)
elif(operacao == '-'):
 resultado = calculadora.subtrair(num1, num2)
elif(operacao == '/'):
    resultado = calculadora.dividir(num1, num2)
elif(operacao == '*'):
 resultado = calculadora.multiplicar(num1, num2)
elif(operacao == 'dobro'):
  resultado = calculadoraAvancada.dobro(num1)
elif(operacao == 'potência'):
  resultado = calculadoraAvancada.potencia(num1, num2)
else:
 print("Erro! Opção inválida")
if(resultado != None):
   print(f"Resultado = {resultado}")