import re

def validar_arranjo_familiar(arranjo):
    # Expressão regular para casais homossexuais mais velhos que os filhos, com pelo menos seis filhos, em que os dois primeiros filhos formam um casal e os últimos também

    regex = r"^(MM|HH)(hm|mh)(h|m)+(h|m)+(hm|mh)$"
    # Verificar se o arranjo familiar corresponde ao padrão
    return re.fullmatch(regex, arranjo) is not None

# Teste

arranjos = [
    ("MHm","casal heterosexual e uma filha"),
    ("HHmm","casal homosexual e duas filhas"),
    ("MMmhm","casal homosexual duas filhas e um filho"),
    ("MHhm","casal heterosexual com um filho e uma filha"),
    ("HMmh","casal heterosexual com uma filha e um filho"),
    ("MHhmmm","casal heterosexual um filho e tres ultimas filhas"),
    ("HMmhhh","casal heterosexual  uma filha tres ultimos filhos"),
    ("MHhhm","casal heterosexual dois filhos e uma filha"),
    ("MMhmhmhmhm","casal homosexual com seis filhos, dois primeiros são um casai e os ultimos tambem"),
    ("MMhhhmhmhm","casal homosexual com seis filhos, dois primeiros são homens e os ultimos um casal")
]

print(f"Expressão regular para casais homossexuais mais velhos que os filhos, com pelo menos seis filhos, em que os dois primeiros filhos formam um casal e os últimos também:")

for arranjo, familia in arranjos:
    if validar_arranjo_familiar(arranjo):
        print(f"Arranjo familiar {familia}, '{arranjo}' é válido.")
    else:
        print(f"Arranjo familiar {familia}, '{arranjo}' é inválido.")
