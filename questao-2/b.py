import re

def validar_arranjo_familiar(arranjo):
    # Expressão regular para casais heterossexuais mais velhos que os filhos com uma quantidade ímpar de filhas mulheres (v)

    regex = r"^(MH|HM)h*mh*(h*mh*mh*)*$"
    # Verificar se o arranjo familiar corresponde ao padrão
    return re.fullmatch(regex, arranjo) is not None

# Teste
    
arranjos = [
    ("MHm","casal heterosexual e uma filha"),
    ("HHmm","casal homosexual e duas filhas"),
    ("MMmhm","casal homosexual duas filhas e um filho"),
    ("MHhm","casal heterosexual um filho e uma filha"),
    ("HMmh","casal heterosexual uma filha e um filho"),
    ("MHhmmm","casal heterosexual um filho e tres ultimas filhas"),
    ("HMmhhh","casal heterosexual  uma filha tres ultimos filhos"),
    ("MHhhm","casal heterosexual dois filhos e uma filha")
]

print(f"Expressão regular para casais heterossexuais mais velhos que os filhos com uma quantidade ímpar de filhas mulheres:")

for arranjo, familia in arranjos:
    if validar_arranjo_familiar(arranjo):
        print(f"Arranjo familiar {familia}, '{arranjo}' é válido.")
    else:
        print(f"Arranjo familiar {familia}, '{arranjo}' é inválido.")
