import json
import pandas as pd

URL = 'https://raw.githubusercontent.com/Colin-Riley/monitoring/main/transacoes_reversed_minuto_a_minuto_fis_cw__desfazimentos__2022-02-22T21_16_12.064248Z.csv'  # noqa = E501


def train_model_helper(data, flag):
    values = {}
    flag_analysis = data[data["status"] == flag]
    values['Q1'] = flag_analysis["f1_"].quantile(0.25)
    values['Q3'] = flag_analysis["f1_"].quantile(0.75)
    values['IQR'] = values['Q3'] - values['Q1']
    return values


def train_model(data):
    transactions = pd.read_csv(data)
    flag = {}
    flag['denied'] = train_model_helper(transactions, 'denied')
    flag['reversed'] = train_model_helper(transactions, 'reversed')
    flag['failed'] = train_model_helper(transactions, 'failed')
    with open('trained_model.txt', 'w') as file:
        file.write(json.dumps(flag))


train_model(URL)
