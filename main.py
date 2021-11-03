#Varbutibu kalkulators
# Autors: X
# Datums: 03.11.2021 V2V

def statistiska():
    
    
    a = float(input(" Ievadiet A notikuma kopejo skaitli: "))
    b = float(input(" Ievadiet cik A notikuma iestajas skaitli: "))
    c = b/a
    d = c*100
    if a<0:
        return print("Jusu pirmais skailtlis nevar but negativs, meginiet velreiz")
    elif b<0:
         return print("Jusu otrais skailtlis nevar but negativs, meginiet velreiz")
    print("Ir " , d,"%", "iespējamība, ka no", a ,"reizēm notikums notiks ",b," rizes")
    #Ja 𝑘 neatkarīgos mēģinājumos notikums 𝐴 iestājas 𝑚 reizes,
    # tad 𝑚 sauc par 𝐴 absolūto biežumu,
    # bet attiecību 𝑊(𝐴)=𝑚/𝑘 par notikuma 𝐴 relatīvo biežumu. Rezultātu izsaki procentos

    #lietotāja vertibu ievade
    # aprekins
    #izvade
    


def geometriksa():
    #Šis varbūtību aprēķināšanas likums ir spēkā arī telpiskiem ķermeņiem.
    # Pieņemsim, ka telpā doti ģeometriski ķermeņi 𝐺 un 𝑔,
    # pie kam, ķermenis 𝐺 ietver sevī ķermeni 𝑔.
    # Uz labu laimi izvēlas punktu no ķermeņa 𝐺.
    # Varbūtība, ka izvēlētais punkts piederēs arī ķermenim 𝑔, ir 𝑃(𝐴)=𝑉(𝑔)/𝑉(𝐺)

    # lietotāja vertibu ievade
    # aprekins
    # izvade
    
    a = float(input("Ievadiet lielas figuras laukumu(skaitlis): "))
    b = float(input("Ievadiet mazas figuras laukumu(skaitlis): "))
    c = b/a
    d = c*100
    if a<0:
        return print("Jusu pirmais skailtlis nevar but negativs, meginiet velreiz")
    elif b<0:
         return print("Jusu otrais skailtlis nevar but negativs, meginiet velreiz")
    print( d,"%", "ir varbutiba , ka izveletais punkts piekrit abam figuram")
    

def klasiska():
    #P(A) = (labvēlīgo notikumu skaits) / (visu notikumu kopskaits)

    # lietotāja vertibu ievade
    # aprekins
    # izvade
    
    a = float(input("Ievadiet labvēlīg notikumu skaitu: "))
    b = float(input("Ievadiet kopejo notikumu skaitu: "))
    c = a/b*100
    d = c
    if a<0:
        return print("Jusu pirmais skailtlis nevar but negativs, meginiet velreiz")
    elif b<0:
         return print("Jusu otrais skailtlis nevar but negativs, meginiet velreiz")
    print( "",a, "labvēlīg notikumi ",b, "reizes notiks:", c ,"%"  )
    

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    choice = input("Kada veida varbutibas aprekini Tev sodien padoma? \n"
                   "Ievadi burtu:\n-K klasiska metode n no n\n"
                   "-G geometriksa varbutiba\n"
                   "-S statiska varbutiba k m reizes\n")
    if choice.lower() == 'k':
        klasiska()
    if choice.lower() == 'g':
        geometriksa()
    if choice.lower() == 's':
        statistiska()
    
