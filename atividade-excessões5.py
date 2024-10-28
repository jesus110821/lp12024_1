def verificar_maiuscula(texto):
    tem_nao_letra = any(not char.isalpha() for char in texto)
    tem_nao_maiuscula = any(char.isalpha() and not char.isupper() for char in texto)

    if tem_nao_letra:
        return "A string contém um caractere que não é letra."
    elif tem_nao_maiuscula:
        return "A string contém um caractere que não é maiúsculo."
    else:
        return "A string é composta apenas por letras maiúsculas."

# Exemplo de uso
resultado = verificar_maiuscula("HELLO")
resultado2 = verificar_maiuscula("Hello")
resultado3 = verificar_maiuscula("HELLO123")

print(resultado)
print(resultado2)
print(resultado3)

# C:\Users\Jesus\Desktop\projetos\.venv\Scripts\python.exe C:\Users\Jesus\Desktop\projetos\lp12024_1\github\atividade-excessões5.py
# A string é composta apenas por letras maiúsculas.
# A string contém um caractere que não é maiúsculo.
# A string contém um caractere que não é letra.
#
# Process finished with exit code 0
