import sys

for line in sys.stdin:
    # Eliminar espazos innecesarios e dividir a liña polos tabuladores
    data = line.strip().split("\t")

    # Comprobar que a liña ten un número de columnas válido
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        # Imprimir o resultado no formato solicitado usando o método format
        print('{}\t{}'.format(payment, cost))
#        print('{}\t{}'.format(store, cost))  # Para Python 2
    else:
        # Ignorar liñas que non son válidas
        continue
