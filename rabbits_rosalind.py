# Calculando total de coelhos após n meses
# Cada coelho irá gerar k casais, que precisam crescer
# Para também se reproduzirem.


def fibonacci(n,k):
    adult, offspring = 1, 1
    for i in range(2, n):
        current = adult + k * offspring
        offspring = adult
        adult = current
    return current


print (fibonacci(5,3))



