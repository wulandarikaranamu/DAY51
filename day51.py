#merry wulandari

print("\n"+"mencari angka terkecil"+"\n"+22*"=")

a = int(input("masukkan angka a:"))
b = int(input("masukkan angka b:"))
c = int(input("masukkan angka c:"))

if a < b and a < c:
    print("A yang terkecil")
elif b < a and b < c:
    print("B yang terkecil")
else:
    print("C yang terkecil")


print("\n"+"mencari nilai tengah"+"\n"+22*"=")

a = int(input("masukkan nilai a:"))
b = int(input("masukkan nilai b:"))
c = int(input("masukkan nilai c:"))

if (b > a > c) or (c > a < b):
    print("A adalah nilai tengah")
elif (a > b > c)or (c > b > a):
    print("B adalah nilai tengah")
else:
    print("C nllai adalah tengah")




