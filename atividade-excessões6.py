class FahrenheitError(Exception):
    pass

def fahrenheit_para_celsius(f):
    if f < -459.67:
        return "Erro: valor abaixo do zero absoluto."
    return 5 * (f - 32) / 9

# Exemplo de entradas:
print(fahrenheit_para_celsius(32))      # Saída: 0.0
print(fahrenheit_para_celsius(-500))    # Saída: "Erro: valor abaixo do zero absoluto."
print(fahrenheit_para_celsius(212))     # Saída: 100.0
