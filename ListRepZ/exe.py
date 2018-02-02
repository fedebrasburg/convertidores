parser = []
with open("ListRepZ.txt", "r") as ins:
    l = []
    i = 1
    for line in ins:
        if( i > 12):
            line = line.split()
            e = []
            c = 0
            entro = False
            for a in line:
                if(a[1] == '-'):
                    entro = True
                if (c != 1):
                    e.append(a)
                else:
                    a = a.split('-')
                    e.append(a[0])
                    try:
                        e.append(a[1])
                    except:
                        entro = True
                c += 1
            if(not entro):
                l.append(e)
        i += 1
    ta = ""
    tb = ""
    for x in l:
        r = []
        r.append(x[0])
        r.append(x[1])
        r.append(x[2])
        if(int(x[1]) == 4):
            if(ta != ""):
                ta = ta +1
            r.append(ta)
            ta = int(x[3])
        else:
            if(tb != ""):
                tb = tb +1
            r.append(tb)
            tb = int(x[3])
        r.append(x[3])
        r.append(x[4])
        r.append(x[5])
        r.append(x[6])
        r.append(x[7])
        r.append(x[8])
        r.append(x[9])
        parser.append(r)
    
f = open('salidaListRepZ.txt', 'w')
final = []
#Ordeno para cumplir el orden especificado
for x in parser:
    aux = [x[0],"Z-0000"+str(int(x[1])), x[3],"Z-0000"+str(int(x[1])),x[4],"1","Consumidor final","0",x[10],x[5],x[9],x[6]]
    final.append(aux)
for x in final:
    t = ""
    line_new = '{:>12}  {:>12}  {:>12} {:>12}  {:>12}  {:>12} {:>12}  {:>12}  {:>12}  {:>12}  {:>12} {:>12}'.format(x[0], x[1], x[2],x[3], x[4], x[5],x[6], x[7], x[8],x[9], x[10],x[11])
    f.write(line_new)
    f.write('\n')
f.close()

