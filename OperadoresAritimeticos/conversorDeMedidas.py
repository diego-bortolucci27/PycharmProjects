medida = float(input("Digite a medida em Metros: "))

cm = medida * 1000
mm = medida * 1000
km = medida / 1000
print("A medida de {}m é {:.0f}cm e é {:.0f}mm || {}km ".format(medida, cm, mm, km))