import numpy as np
from faker import Faker

fake = Faker()

numEstudiantes = 6500

codigos = np.random.randint(1000, 9999, numEstudiantes)  
nombres = [fake.name() for _ in range(numEstudiantes)]
promediosAcumulados = np.random.uniform(2.0, 5.0, numEstudiantes)  
añosIngreso = np.random.randint(1980, 2023, numEstudiantes)  
estadoCondicionales = np.random.choice(['Si', 'No'], numEstudiantes)


dtype_estudiante = [('codigo', int), ('nombre', 'U50'), ('promedioAcumulado', float), ('añoIngreso', int), ('estadoCondicional', 'U3')]
registrosEstudiantes = np.empty(numEstudiantes, dtype=dtype_estudiante)


registrosEstudiantes['codigo'] = codigos
registrosEstudiantes['nombre'] = nombres
registrosEstudiantes['promedioAcumulado'] = promediosAcumulados
registrosEstudiantes['añoIngreso'] = añosIngreso
registrosEstudiantes['estadoCondicional'] = estadoCondicionales


carreraAbuscar = input("Ingrese el codigo de la carrera: ")
estudiantesCarreraX = registrosEstudiantes[(registrosEstudiantes['codigo'] == int(carreraAbuscar)) & (registrosEstudiantes['promedioAcumulado'] >= 4)]

print(f"Estudiantes de la carrera {carreraAbuscar} con promedio acumulado >= 4:")
for estudiante in estudiantesCarreraX:
    print(f"Codigo: {estudiante['codigo']}, Nombre: {estudiante['nombre']}")

print(f"Total de estudiantes en la carrera {carreraAbuscar} con promedio acumulado >= 4: {len(estudiantesCarreraX)}")


estudiantes_condicionales_antes_1990 = registrosEstudiantes[(registrosEstudiantes['añoIngreso'] < 1990) & (registrosEstudiantes['estadoCondicional'] == 'Sí')]

print("Estudiantes ingresados antes de 1990 y en condicional:")
for estudiante in estudiantes_condicionales_antes_1990:
    print(f"Codigo: {estudiante['codigo']}, Nombre: {estudiante['nombre']}")
