import re
# Entrada
# 0: fecha
# 1: Nombre de la drogueria
# 2: cuit
# 3: numero de factura
# 4: exento
# 5: gravado
# 6: iva
# 7: Perc. IB
# 8: Perc. iva
# 9: Total
# 10: Nada. No usar

# Salida
# Fecha (0)
# Tipo: NCC si es nota de credito (el total es negativo). FCC si no
# 'A' + Numero de factura
# cuit
# condicion: siempre R
# nombre de la drogueria
# 4: exento
# 5: gravado
# 6: iva
# 7: Perc. IB
# Ret. IB: siempre 0
# 8: Perc. iva
# 9: Total

class LineaConFormatoIncorrecto(Exception):
  pass

cuitRegex = re.compile(r'\d-\d\d\d\d\d\d\d\d-\d')
def main():
    salidas = []
    with open('Compras.inf') as f:
        for l in f:
            linea = l.split()
            index = 1
            try:
              while(index > 0):
                  if (cuitRegex.search(linea[index])):
                      linea[1:index] = [' '.join(linea[1:index])]
                      break
                  index  += 1
              fecha         = linea[0]
              nombre        = linea[1]
              cuit          = linea[2]
              numeroFactura = linea[3]
              exento        = linea[4]
              gravado       = linea[5]
              iva           = linea[6]
              percIB        = linea[7]
              perIva        = linea[8]
              total         = linea[9]
              salidas.append([
                  '/'.join(fecha[i:i+2] for i in range(0, len(fecha), 2)),
                  nombre,
                  "RI",
                  cuit,
                  "NCC" if float(total.replace(",", ".")) < 0 else "FCC",
                  "A" + str(numeroFactura),
                  exento,
                  gravado,
                  iva,
                  percIB,
                  "0,00",
                  perIva,
                  total
              ])
            except:
              print("Falle al procesar la linea: " + l)
              raise LineaConFormatoIncorrecto

    with open('salidaCompras.txt', 'w') as file:
        for linea in salidas:
            linea = [x.replace(",",".") for x in linea]
            file.write(','.join(linea) + "\n")

main()
