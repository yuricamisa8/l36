# Inicializa uma lista vazia para as notas
notas = []
for i in range(4):
    nota = float(input(f"Digite a {i + 1}ª nota: "))
    notas.append(nota)
print("Notas digitadas:")
for i, nota in enumerate(notas):
    print(f"Nota {i + 1}: {nota}")
media = sum(notas) / len(notas)
print(f"Média das notas: {media:.2f}")
