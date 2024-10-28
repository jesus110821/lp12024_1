class RespostaInvalidaError(Exception):
    pass

def solicitar_confirmacao():
    while True:
        resposta = input("Deseja confirmar? (sim/não): ").strip().lower()
        if resposta in ['sim', 's']:
            return "Confirmação registrada."
        elif resposta in ['não', 'n']:
            return "Confirmação negada."
        else:
            print("Erro: Resposta inválida. Tente novamente.")

print(solicitar_confirmacao())

# Saída: C:\Users\Jesus\Desktop\projetos\.venv\Scripts\python.exe C:\Users\Jesus\Desktop\projetos\lp12024_1\github\atividade-excessões7.py
# Deseja confirmar? (sim/não): ababad
# Erro: Resposta inválida. Tente novamente.
# Deseja confirmar? (sim/não): nao
# Erro: Resposta inválida. Tente novamente.
# Deseja confirmar? (sim/não): sim
# Confirmação registrada.
#
# Process finished with exit code 0
