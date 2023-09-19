import numpy as np
votos = np.random.randint(1, 5000, 30)
totalVotos = sum(votos) 
votosNormalizados = votos / totalVotos * 5000 
votosNormalizados = np.round(votosNormalizados).astype(int) 
candidatos = {}
for i in range(30):
    candidatos[i] = i + 1
for i in range(30):
    for j in range(30):
        if votosNormalizados[i] > votosNormalizados[j]:
            votosNormalizados[i], votosNormalizados[j] = votosNormalizados[j], votosNormalizados[i]
            candidatos[i], candidatos[j] = candidatos[j], candidatos[i]
print("El número de votos obtenidos por cada candidato es:")
for i in range(30):
    print("El candidato", candidatos[i], "obtuvo", votosNormalizados[i], "votos")