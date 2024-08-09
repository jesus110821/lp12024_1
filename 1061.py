dia_inicio = int(input().split()[1])
hora_inicio, minuto_inicio, segundo_inicio = map(int, input().split(" : "))
dia_termino = int(input().split()[1])
hora_termino, minuto_termino, segundo_termino = map(int, input().split(" : "))
total_segundos_inicio = segundo_inicio + minuto_inicio * 60 + hora_inicio * 60 * 60 + dia_inicio * 24 * 60 * 60
total_segundos_termino = segundo_termino + minuto_termino * 60 + hora_termino * 60 * 60 + dia_termino * 24 * 60 * 60
duracao_segundos = total_segundos_termino - total_segundos_inicio
dias = duracao_segundos // (24 * 60 * 60)
duracao_segundos %= 24 * 60 * 60
horas = duracao_segundos // (60 * 60)
duracao_segundos %= 60 * 60
minutos = duracao_segundos // 60
duracao_segundos %= 60
segundos = duracao_segundos

print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")