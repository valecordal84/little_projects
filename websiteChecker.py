print ("Esto es un tester de websites. 'Verifica' rápidamente si una web es segura o no.")

continuar = True

while continuar == True:
    url = input("Ingresa el link completo de la página que deseas 'verificar': ")
    if url.startswith("https") or url.startswith("HTTPS"):
        print("Esta página es segura, puedes navegar! ")
        continuar = False
    elif url.startswith("http") or url.startswith("http"):
        print("Esta página no es segura, no se recomienda continuar")
        continuar = False
    else:
        print("Esto no es una página web o no es link completo, por favor vuelve a intentarlo!")