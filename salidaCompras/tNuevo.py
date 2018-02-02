

with open("Compras.inf", "r") as ins:
    l = []
    a = 0
    for line in ins:
        a += 1
        r = []
        line = line.split()
        r.append(line[0])
        cont = 1
        cr = 1
        sigo = True
        r.append("")
        #nombre palabras
        while(sigo):
            for x in line[cont]:
                if x.isdigit():
                    sigo = False
                    break
                else:
                    r[1] += x
            r[cr] += " "      
            cont += 1
        cont -= 1
        r.append("")
        cr = 2
        for x in line[cont]:
            if x.isdigit() or x == '-':
                r[cr] += x
        cont += 1
        p = ""
        cr = 3
        r.append("")
        for x in line[cont]:
            #si se paso
            if (len(r[cr]) > 12):
                p += x
            else:
                if x.isdigit() or x == '-':
                    r[cr] += x
        if(p != ""):
            line[cont] = p
        else:
            cont += 1
        f = " ".join(line[cont:])
        cr = 4
        r.append("")
        punto = -1
        for x in f:
            if ( x == '.'):
                punto = 0
            r[cr] += x
            if(punto > -1):
                punto += 1
            if(punto == 3):
                cr +=1
                r.append("") 
        l.append(r)

s = []
for x in l:
    r = []
    r.append(x[0])
    if  float(x[9]) <0:
        r.append("NCC")
    else:
        r.append("FCC")
    r.append("A" + x[3])
    r.append(x[2])
    r.append("Rl")
    r.append((x[1]))
    r.append(float(x[5]))
    r.append(float(x[6]))
    r.append(float(x[7]))
    r.append(float(x[8]))
    r.append(float(x[4]))
    r.append(float(x[9]))
    s.append(r)

    fecha = r[0]
    aux = ""
    cont = 0
    c = 0
    for n in fecha:
        if(cont < 2):
            aux +=n
            cont += 1
        else:
            c += 1
            cont = 1
            aux += '/'
            if( c == 2):
                aux += "20"
            aux += n
    r[0] = aux

#reordeno
final = []
for x in s:

    aux = []
    for i in x:
        aux.append(i)
    aux[8] = x[7]
    aux[6] = x[10]
    aux[7] = x[6]
    aux[9] = x[8]
    aux[11] = "0.00"
    aux[10] = x[9]
    aux.append(x[11])
    final.append(aux)
    
f = open('salidaCompras.txt', 'w')
for x in final:
    t = ""
    c = 0
    for y in x:
        c += 1
        if( type(y) != str):
            t +=  "{:10.2f}".format(y) + " "
        else:
            t += y + "  "
            if( c == 6):
                for x in range(len("DROG DEL SUD SA ") - len(y)):
                    t +=  " "
    t = t.replace(",", ".")
    f.write(t)
    f.write('\n')
f.close

