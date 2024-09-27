import math

#penginputan
a =  float(input("masuka bilangan bulat a: "))
b = float (input("masukan bilangan kedua b: "))

#menghitung hasil perhitungan
jumlah = a + b 
selisih = b - a
kali = a * b
sisa_pembagian = a % b
pembagian = a / b
log_a = math.log10(a)
pangkat = a ** b

#hasil
print (f"jumlah a dan b: {jumlah}")
print (f"selisih b dan a: {selisih}")
print (f"hasil kali a dan b: {kali}")
print (f"hasil sisa_pembagian a dengan b: {sisa_pembagian}")
print (f"hasil pembagian a dengan b: {pembagian}")
print (f"hasil dari log(a):{log_a}")
print (f"hasil a pangkat b:{pangkat}")