import re

def validar_arranjo_familiar(arranjo):
    # Expressão regular para casais heterossexuais mais velhos que os filhos com pelo menos duas filhas mulheres, ou pelo menos um filho homem, ou ainda pelo menos dois filhos homens e uma filha mulher (v)
    
    regex = r"^(?=.*h|.*m.*m)((MH)|(HM))[hm]+$"
    # Verificar se o arranjo familiar corresponde ao padrão
    return re.fullmatch(regex, arranjo) is not None

# Testes

arranjos = [
    ("MHm","casal heterosexual e uma filha"),    # casal heterosexual e uma filha
    ("HHmm","casal homosexual e duas filhas"),   # casal homosexual e duas filhas
    ("MMmhm","casal homosexual duas filhas e um filho"),  # casal homosexual duas filhas e um filho
    ("MHhm","casal heterosexual com um filho e uma filha"),   # casal heterosexual pelo menos um filho e uma filha
    ("HMmh","casal heterosexual com uma filha e um filho"),   # casal heterosexual pelo menos dois filhos e uma filha
    ("MHhmmm","casal heterosexual um filho e tres ultimas filhas"), # casal heterosexual um filho e tres ultimas filhas
    ("HMmhhh","casal heterosexual  uma filha tres ultimos filhos"), # casal heterosexual  uma filha tres ultimos filhos 
    ("MHhhm","casal heterosexual dois filhos e uma filha")   # casal heterosexual dois filhos e uma filha
]

print(f"Expressão regular para casais heterossexuais mais velhos que os filhos com pelo menos duas filhas mulheres, ou pelo menos um filho homem, ou ainda pelo menos dois filhos homens e uma filha mulher:")

for arranjo, familia in arranjos:
    if validar_arranjo_familiar(arranjo):
        print(f"Arranjo familiar {familia}, '{arranjo}' é válido.")
    else:
        print(f"Arranjo familiar {familia}, '{arranjo}' é inválido.")
