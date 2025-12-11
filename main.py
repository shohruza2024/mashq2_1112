#1-misol
sozlar = ["Python", "Dastur", "KITOB"]
natija = {s.lower() for s in sozlar}
print(natija)

#2-misol
natija = {x for x in range(1, 101) if sum(map(int, str(x))) == 10}
print(natija)

#3-misol
matn = "Assalomu alaykum"
unli = "aeiouöüoaiAOEIU"
natija = {h for h in matn if h in unli}
print(natija)

#4-misol
sonlar = [10, -5, 25, 0, 15, -20]
natija = {x for x in sonlar if x > 0 and x % 5 == 0}
print(natija)

#5-misol
natija = {x for x in range(1, 51) if x > 1 and all(x % y != 0 for y in range(2, x))}
print(natija)

