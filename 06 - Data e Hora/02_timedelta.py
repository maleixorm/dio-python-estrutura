from datetime import datetime, timedelta

tipo_carro = "M"
tempo_pequeno = 60
tempo_medio = 240
tempo_grande = 720
data_atual = datetime.now()

if tipo_carro == "G":
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"O carro chegou: {data_atual} e ficará pronto: {data_estimada}")
elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f"O carro chegou: {data_atual} e ficará pronto: {data_estimada}")
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f"O carro chegou: {data_atual} e ficará pronto: {data_estimada}")