import re

def validar_arranjo_familiar(arranjo):
    # Expressão regular para casais homossexuais mais velhos que os filhos, em que o sexo dos filhos é alternado conforme a ordem de nascimento (v)

    regex = r"^(?!.*((h|m))\1)((MM)|(HH))(h|m)+$"
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
    ("MMhhhmhmhm","casal homosexual com seis filhos, dois primeiros são homens e os ultimos um casal"),
    ("MMmhmhmh","casal homosexual em que o sexo dos filhos é alternado conforme a ordem de nascimento, sendo uma primogenita"),
    ("MMhmhmh","casal homosexual em que o sexo dos filhos é alternado conforme a ordem de nascimento, sendo um primogenito")
]

print(f"Expressão regular para casais homossexuais mais velhos que os filhos, em que o sexo dos filhos é alternado conforme a ordem de nascimento:")

for arranjo, familia in arranjos:
    if validar_arranjo_familiar(arranjo):
        print(f"Arranjo familiar {familia}, '{arranjo}' é válido.")
    else:
        print(f"Arranjo familiar {familia}, '{arranjo}' é inválido.")
