import math

angulo = float(input("Digite o angulo que voce deseja: "))
ang_rad = math.radians(angulo)
coss = math.cos(ang_rad)
seno = math.sin(ang_rad)
tang = math.tan(ang_rad)

print(f"""O angulo de {angulo}
tem o Seno de {seno:.2f}
tem o cosseno de {coss:.2f}
tem a tangete de {tang:.2f}
""")
