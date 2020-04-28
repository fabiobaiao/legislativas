
import csv

totalMandatos = 226

#circulosEleitorais = {'1': ['50']}
circulosEleitorais = {'1': ["01"], '2': ["02"], '3':["03"], '4': ["04"], '5': ["05"], '6': ["06"], '7': ["07"], '8': ["08"], '9': ["09"], '10': ["10"], '11': ["11"], '12': ["12"], '13': ["13"], '14': ["14"], '15': ["15"], '16': ["16"], '17': ["17"], '18': ["18"], '19': ["30"], '20':["40"]}

resultadosPorCirculo = {}

def circuloEleitoral(code):
    for circuloEleitoral in circulosEleitorais.keys():
        codes = circulosEleitorais[circuloEleitoral]
        if code in codes:
            codes.remove(code)
            return circuloEleitoral

    return -1

for row in csv.reader(open("resultados.csv")):
    code = row[0]

    circuloEleitoral = circuloEleitoral(code)

    if circuloEleitoral != -1:
        resultadosPorCirculo.setdefault(circuloEleitoral, {})
