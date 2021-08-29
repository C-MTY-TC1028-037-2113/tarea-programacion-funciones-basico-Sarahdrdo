def area(b,a):
    area_cara = b*a
    return area_cara


def area_prisma(ba,al,pr):
    area_prisma_completo = area(ba,al)*2+area(al,pr)*2+area(ba,pr)*2
    return area_prisma_completo

def main():
    #escribe tu código abajo de esta línea
    base = float(input("Dame la base: "))
    altura = float(input("Dame la altura: "))
    profundidad = float(input("Dame la profundidad: "))

    r = area_prisma(base,altura,profundidad)

    print("El área total del prisma es:",r)
if __name__=='__main__':
    main()
    