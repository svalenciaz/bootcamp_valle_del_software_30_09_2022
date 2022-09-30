from random import randint, choice
import pandas as pd
import time

def data_generation(iteration):
    address = address_generation()
    people = randint(1,7)
    reusable = randint(0,100)
    organic = randint(0,100)
    working_day = str(randint(1,7))+choice(["M", "T", "N"])
    sanction = "NN" if iteration%5!=0 else choice(["NN", "SS", "PP"])
    debt = 0 if sanction != "PP" else debt_generator(reusable, organic)
    return {
        "address":address,
        "people": people,
        "reusable": reusable,
        "organic": organic,
        "working_day": working_day,
        "sanction": sanction,
        "debt": debt
    }

def debt_generator(reusable, organic):
    if reusable >=90  or organic >=90:
        valor =  500000
    elif reusable >=70 or organic >= 70:
        valor =  400000
    elif reusable >= 50 or organic >=50:
        valor =  300000
    elif reusable >= 30 or organic >=30:
        valor =  200000
    else:
        valor = 10000
    return valor
    
def print_data(data, iteration):
    print("Dato número:", iteration)
    print("Dirección:", data["address"])
    print("Personas en la casa:", data["people"])
    print("Kilos de basura reciclable:", data["reusable"])
    print("Kilos de basura orgánica:", data["organic"])
    print("Jornada de recolección:", data["working_day"])
    if data["sanction"] != "NN":
        print("Sanción:", "Servicio social" if data["sanction"] == "SS" else "Sanción punitiva")
    else:
        print("Sanción: Sin sanción")
    if data["sanction"] == "PP":
        print("Deuda sanción:", data["debt"])
    print("")

def average_trash_family(data):
    families = len(data)
    trash = sum([family["organic"]+family["reusable"] for family in data])
    print("\nPromedio de basura por familia", round(trash/families,2),"Kg.\n")

def average_per_day(data):
    days = {
        "lunes": "1",
        "martes": "2",
        "miércoles": "3",
        "jueves": "4",
        "viernes": "5",
        "sábado": "6",
        "domingo": "7",
    }
    for day, number_day in days.items():
        per_day = [family["organic"]+family["reusable"] for family in data if number_day in family["working_day"]]
        print("Promedio de basura",day, round(sum(per_day)/len(per_day),2) if len(per_day)>0 else 0, "Kg.")
    print()

def average_per_time_in_day(data):
    times = {
        "mañana": "M",
        "tarde": "T",
        "noche": "N"
    }
    for time, letter_time in times.items():
        per_day = [family["organic"]+family["reusable"] for family in data if letter_time in family["working_day"]]
        print("Promedio de basura",time, round(sum(per_day)/len(per_day),2) if len(per_day)>0 else 0, "Kg.")
    print()

def address_generation():
    main_names = ["CR", "CL", "DG", "TV"]
    main_name = choice(main_names)
    main_number = str(randint(1,95))
    second_number = str(randint(0,9)) + str(randint(0,9))
    third_number = str(randint(0,9)) + str(randint(0,9))
    address = "{} {} {}-{}".format(main_name, main_number, second_number, third_number)

    return address

def data_validation():
    pass

def main():
    initial = time.time()
    print("Sin módulos")
    number_of_data = 2000 # randint(20, 30)
    data = [data_generation(i+1) for i in range(number_of_data+1)]
    for i in range(0, len(data)):
        print_data(data[i], i+1)
    average_trash_family(data)
    average_per_day(data)
    average_per_time_in_day(data)
    middle = time.time()
    
    print("")
    print("Usando módulos")

    data_pd = pd.DataFrame.from_dict(data)
    print(data_pd)

    average_per_family_pd = (data_pd["reusable"] + data_pd["organic"]).sum()/len(data_pd)
    print("Kilos de basura promedio por familia", round(average_per_family_pd,2), "Kg.")

    final = time.time()


    print("Tiempo sin módulos:", middle-initial)
    print("Tiempo con módulos", final - middle)
    print("Tiempo total:", final - initial)

    # average_per_family_pd = (data_pd["reusable"] + data_pd["organic"]).sum()/len(data_pd)
    # print(average_per_family_pd)

    # average_per_family_pd = (data_pd["reusable"] + data_pd["organic"]).sum()/len(data_pd)
    # print(average_per_family_pd)



if __name__ == "__main__":
    main()