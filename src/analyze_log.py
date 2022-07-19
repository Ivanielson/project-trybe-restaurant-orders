import csv
import operator


def most_requested_to_maria(data):
    answer_1 = {}
    for name, request, _ in data:
        if name == "maria":
            if request not in answer_1:
                answer_1[request] = 1
            else:
                answer_1[request] += 1
    return max(answer_1.items(), key=operator.itemgetter(1))[0]

def how_many_hamburgers(data):
    answer_2 = 0
    for name, request, _ in data:
        if name == "arnaldo" and request == "hamburguer":
            answer_2 += 1
    return answer_2

def never_asked(data):
    menu = set()
    joao_requests = set()
    for name, request, _ in data:
        menu.add(request)
        if name == "joao":
            joao_requests.add(request)
    return menu.difference(joao_requests)

def is_not_present(data):
    days = set()
    presence_of_joao = set()
    for name, _, day in data:
        days.add(day)
        if name == "joao":
            presence_of_joao.add(day)
    return days.difference(presence_of_joao)


def analyze_log(path_to_file):
    if ".csv" not in path_to_file:
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
    try:
        with open(path_to_file, encoding="utf-8") as file:
            read_file = csv.reader(file, delimiter=",", quotechar='"')
            data = [tuple(value) for value in read_file]
            answer_1 = most_requested_to_maria(data)
            answer_2 = how_many_hamburgers(data)
            answer_3 = never_asked(data)
            answer_4 = is_not_present(data)
            LINES = [f"{answer_1}\n",f"{answer_2}\n",f"{answer_3}\n",f"{answer_4}\n"]
        with open("data/mkt_campaign.txt", "w") as file:
            file.writelines(LINES)
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")
