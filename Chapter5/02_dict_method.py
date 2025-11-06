marks = {
    "Manish": 100,
    "Keshav":90,
    "Raja":85,
    0: "Harry"

}

print(len(marks))
print(marks.items())
print(marks.keys())
print(marks.values())


marks.update({"Keshav":95 , "Rahul":80})
print(marks)


print(marks.get("Manish"))
