# Insere duas casas decimais no campo de string
def str_to_money(str):
    if str.find(",") == -1:
        str += ",00"
    elif str.find(",") == (len(str) - 2):
        str += "0"
    elif str.find(",") == (len(str) - 1):
        str += "00"
        
    return str

# Converte data do formato d/m/Y para Y-m-d
def converte_data(data):
    data = data.rsplit("/")
    nova_data = data[2] + "-" + data[1] + "-" + data[0]
    return nova_data