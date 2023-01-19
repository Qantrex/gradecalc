print("░██████╗░██████╗░░█████╗░██████╗░███████╗  ░█████╗░██╗░░░██╗░██████╗░")
print("██╔════╝░██╔══██╗██╔══██╗██╔══██╗██╔════╝  ██╔══██╗██║░░░██║██╔════╝░")
print("██║░░██╗░██████╔╝███████║██║░░██║█████╗░░  ███████║╚██╗░██╔╝██║░░██╗░")
print("██║░░╚██╗██╔══██╗██╔══██║██║░░██║██╔══╝░░  ██╔══██║░╚████╔╝░██║░░╚██╗")
print("╚██████╔╝██║░░██║██║░░██║██████╔╝███████╗  ██║░░██║░░╚██╔╝░░╚██████╔╝")
print("░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚══════╝  ╚═╝░░╚═╝░░░╚═╝░░░░╚═════╝░\n\n")
print("Only input number in X or X.X format\n")
print("To skip any grade just use 0 as a placeholder.\n")

arr = [float(input("Deutsch:")),
       float(input("System-Information:")),
       float(input("Software-Entwicklung:")),
       float(input("Naturwissenschaft:")),
       float(input("Sport:")),
       float(input("Werkstäte:")),
       float(input("IT-Sicherheit:")),
       float(input("Englisch:")),
       float(input("Mathe:")),
       float(input("Medientechnik:")),
       float(input("Geografie:")),
       float(input("Netzwerktechnik:")),
       float(input("Religion:"))]

amount = 0
summ = 0

for i in arr:
    if i == 0:
        amount -= 1
    summ += i
    amount += 1

avg = round((summ / amount)*100)/100

print("\n>> Average: ", str(avg), " <<\n")

exitin = input("Press any key to exit:")
