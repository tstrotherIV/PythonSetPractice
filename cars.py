showroom = set()

# carSet = {"mustang", "charger", "Cuda"}

showroom.add("mustang")
showroom.add("charger")
showroom.add("cuda")

print("print set", showroom)

print("set length", len(showroom))

showroom.add("cuda")
print("print set", showroom)

newSet = {"accord", "tundra"}
print(newSet)

showroom.update(newSet)
print("adding newSet to showroom set", showroom)

showroom.remove("accord")
print("remove accord from showroom set", showroom)

junkyard = {"Explorer", "Suburban", "Ck15", "mustang", "cuda"}
print("junkyard set", junkyard)

inter = showroom.intersection(junkyard)
print("check for matching cars", inter)

combined = showroom.union(junkyard)
print("combine sets", combined)

combined.remove("Ck15")
print("removed Ck15", combined)
