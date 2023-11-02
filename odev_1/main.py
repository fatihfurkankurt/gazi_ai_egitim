yas = int(input("Yaşınızı giriniz:"))
boy = int(input("Boyunuzu cm olarak giriniz:"))

if yas >=18 and boy >=170:
    print("Bu kaydırağı kullanabilirsiniz.")
elif yas <18 and boy >170:
    print("Yaşınız kaydırağı kullanmak için yeterli değil")
elif yas >18 and boy <170:
    print("Boyunuz kaydırağı kullanmak için yeterli değil")
else:
    print("Bu kaydırağı kullanamazsınız.")