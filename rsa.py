# https://repl.it/


done1 = 1
done2 = 1
sair = 1
mensagemfinal = " "
mensagemok = " "
jatemcodigo = False
primook = False

MMI = lambda A, n,s=1,t=0,N=0: (n < 2 and t%N or MMI(n, A%n, t, s-A//n*t, N or n),-1)[n<1]

while sair == 1:
    
    print ("1 - Definir um conjunto de chaves para RSA")
    print ("2 - Criptografar uma mensagem")
    print ("3 - Descriptografar uma mensagem")

    menuprinc = int(input("O que deseja fazer? "))


    
    if menuprinc == 1:
        
        # seleciona os primos

        p = int(input ("Insira um valor primo P: "))
        q = int(input ("Insira um valor primo Q: "))

        #determina n e f(n)
        n = p * q
        fn = (p - 1) * (q - 1)

        #recebe e
        print ("f(n) =", fn)
        while primook == False:
            e = int(input ("Insira um valor entre 1 e f(n) que seja primo em relação a f(n): "))
            if fn % e == 0:
                print ("O número inserido não é válido")
                primook = False;
            else:
                primook = True;
            
        #calcula inverso multiplicativo de e mod fn

        d = MMI(e,fn)
        print ("Inverso multiplicativo de", e, "no módulo", fn, "=", d)

        print ("")
        print ("---------------------------------")
        print ("Chaves calculadas!")
        print ("Públicas = (N =",n,"; E =",e, ")")
        print ("Privadas = (P =",p,"; Q =",q,"; D =",d,")")
        print ("---------------------------------")
        print ("")
        jatemcodigo = True                 
        print ("1 - Continuar no programa")
        print ("2 - Sair")
        sair = int (input("O que deseja fazer?"))
        if sair == 1:
            sair = 1
        else:
            sair = 2
            break
        
    ##CODIFICACAO
    if menuprinc ==2:
       
        if jatemcodigo == True:
            xxx = 0
        else:
            n = int (input("Insira o valor de N:" ))
            e = int (input("Insira o valor de E:" ))

        pre = input("Escreva a mensagem que deseja pré-codificar: ")
        precode = [ord(c) for c in pre]

        d = MMI = lambda A, n,s=1,t=0,N=0: (n < 2 and t%N or MMI(n, A%n, t, s-A//n*t, N or n),-1)[n<1]
        print ("")
        print ("A mensagem pré-codificada em ASCII é:")
        print (precode)
        print ("")
        print ("Insira cada bloco da mensagem. Digite 'fim' quando terminar.")
        print ("")
        while done1 == 1:
            blococode = input("Insira o bloco: ")
            if blococode == "fim":
                done1 = 2
                break
            else:
                blococode = int(blococode)
                done1 = 1
                blococoderes = (blococode**e) % n
                blococodetemp = str(blococoderes)
                mensagemfinal += " " + blococodetemp
                done = 1
        print ("")
        print ("Mensagem codificada!")
        print (mensagemfinal)
        print ("---------------------------------")
        print ("")
                     
        print ("1 - Continuar no programa")
        print ("2 - Sair")
        sair = int (input("O que deseja fazer?"))
        if sair == 1:
            sair = 1
        else:
            sair = 2
            break

    ## DECOFICACAO
                     
    if menuprinc ==3:

        if jatemcodigo == True:
            xxx = 0
        else:
            p = int (input("Insira o valor de P:" ))
            q = int (input("Insira o valor de Q:" ))
            d = int (input("Insira o valor de D:" ))
            n = p*q
                     

        print ("")
        print ("Insira cada bloco da mensagem codificada. Digite 'fim' quando terminar.")
        print ("")
        while done2 == 1:
            bloco_to_decode = input ("Insira o bloco: ")
            if bloco_to_decode == "fim":
                done2 = 2
                break
            else:
                bloco_to_decode = int(bloco_to_decode)
                bloco_decoded = (bloco_to_decode**d) % n
                letra = chr(bloco_decoded)
                mensagemok += letra
                done2 = 1
        print ("")
        print ("Mensagem Decodificada!")
        print (mensagemok)
        print ("---------------------------------")
        print ("")
                     
        print ("1 - Continuar no programa")
        print ("2 - Sair")
        sair = int (input("O que deseja fazer?"))
        if sair == 1:
            sair = 1
        else:
            sair = 2
            break
