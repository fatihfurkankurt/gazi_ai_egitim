insan1 = input("1.ismi giriniz:")
insan2 = input("1.ismi giriniz:")

combined = insan1 + insan2
lower_combined = combined.lower()

s = lower_combined.count("s")
e = lower_combined.count("e")
v = lower_combined.count("v")
g = lower_combined.count("g")
i = lower_combined.count("i")

score = s + e + v + g + i
print (f"Sevgi Skorunuz: {score} \n")

if score <3:
    print("Sevmiyor :(")
elif 3<=score<=5:
    print("Arkadaş olarak görüyor :|")
else:
    print ("Çok seviyor :)")