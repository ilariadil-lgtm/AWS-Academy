stringhe: list[str] = ["Pippo"]

stringhe.append("Pluto")
stringhe.append("Topolino")

deleted_value = stringhe.pop()
deleted_values: list[str] = []

deleted_values.append(deleted_value)

print(stringhe)
print(deleted_values)