messagem =  "hello world! Utilizando o Git junto o vscosde! Nova feature adicionada. Com sucesso!"
print(messagem)

def soma( a, b ):
    return a + b
def par_ou_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"
    
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

resultado = soma(num1, num2)

print(f"A soma de {num1} e {num2} é: {resultado}")

if resultado.is_integer():
    print (f"O núnmero {int(resultado)} é {par_ou_impar(int(resultado))}.")
else:
    print("o resultado não é um número inteiro. não é possível determinar se é par ou ímpar.")
