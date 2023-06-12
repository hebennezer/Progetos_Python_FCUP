def tempo(t):
   horas = t // 3600
   minutos = (t % 3600) // 60
   segundos = (t % 3600) % 60

   return f"{horas:02d}:{minutos:02d}:{segundos:02d}"

print(tempo(4000))