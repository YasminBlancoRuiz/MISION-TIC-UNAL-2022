
fraseAdivina="El Caballero de la Noche"
letras="t,s,l,h,i,d,ñ,E,u,R,M,p,a,F,V,C,b,N,o,G"

def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

print(normalize(letras))

y="t,s,l,h,i,d,ñ,á,u,R,M,p,a,F,Á,C,b,N,o,"
y=(y.replace("á","a").replace("Á","A"))
y=(y.replace("é","e").replace("É","E"))
y=(y.replace("í","i").replace("Í","I"))
y=(y.replace("ó","o").replace("Ó","O"))
y=(y.replace("ú","u").replace("Ú","U"))

y=y.upper()
print(y)