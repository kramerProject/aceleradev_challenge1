from datetime import datetime

records = [
    {'source': '48-996355555', 'destination': '48-666666666', 'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097', 'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097', 'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788', 'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788', 'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099', 'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697', 'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099', 'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697', 'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097', 'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564627800, 'start': 1564626000}
]


def classify_by_phone_number(records):
    """

    :param records: A dictionary list with source phone number, destination phone number
    end and beginning of the call in timestamp format
    :return: A dictionary list grouped by the source phone number and sorted by the call charge.
    """
    #creates a list with exclusive numbers
    lista_telefones = []
    for registros in records:
        numero_telefone = registros['source']
        if numero_telefone not in lista_telefones:
            lista_telefones.append(numero_telefone)

    #creates a dicionary with the source phone numbers and call charge
    dicionario={}
    lista_final=[]
    for numero in lista_telefones:
        soma_tarifas=0
        for registros in records:
            if numero == registros['source']:
                tarifa = calculo_tarifa(registros['start'],registros['end'])
                soma_tarifas+=tarifa
        dicionario['source']=numero
        dicionario['total']=round(soma_tarifas,2)
        lista_final.append(dicionario.copy())
        dicionario.clear()

    return sorted(lista_final,key=lambda k: k['total'],reverse=True)

def converte_stamp(numero):
    """

    :param numero: Timestamp Data.
    :return:A time format %H:%M:%S
    """
    inicio=datetime.fromtimestamp(numero).time()

    return inicio


def calculo_tarifa(inicio,fim):
    """
    :param inicio: Timestamp Data representing the beginning of the call.
    :param fim: Timestamp Data representing the end of call.
    :return: Charge of the call based on a bussiness rule.
    """
    vinte_duas_horas = datetime.now().replace(hour=22, minute=00, second=00, microsecond=00).time()
    seis_horas = datetime.now().replace(hour=6, minute=00, second=00, microsecond=00).time()
    if converte_stamp(inicio) > seis_horas and converte_stamp(fim) < vinte_duas_horas:
        tarifa=0.36+((fim-inicio)//60)*0.09
    else:
        tarifa=0.36

    return tarifa

