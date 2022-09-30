from sys import stdin, stdout
import re

def data_collection():

    address_regex =r"\b^([ACDFGIKLTVZ]|[acdfgikltvz])\S{0,14}\s*\d{1,3}\s*(([A-Z]\s*([A-G]\s*){0,2})|([a-z]\s*([a-g]\s*){0,2}))?\s*(((N|S|E|O)|(n|s|e|o))\w{0,4})?\s*[N#]?\S*\s*\d{1,3}\s*(([A-Z]\s*([A-G]\s*){0,2})|([a-z]\s*([a-g]\s*){0,2}))?\s*(((N|S|E|O)|(n|s|e|o))\w{0,4})?\s*[-\/]?\s*\d{1,3}\b"

    try:
        address: str = stdin.readline().strip()
        assert re.search(address_regex, address), "Dirección debe ser alfanumérico, inténtelo nuevamente, te quedan 2 intentos."
    except Exception as error:
        print(error)
        try:
            address: str = stdin.readline().strip()
            assert re.search(address_regex, address), "Dirección debe ser alfanumérico, inténtelo nuevamente, te queda un intento."
        except Exception as error:
            print(error)
            try:
                address: str = stdin.readline().strip()
                assert re.search(address_regex, address), "Dirección debe ser alfanumérico, no te quedan más intentos."
            except:
                print(error)
                return None
    
    try:
        cantidad: str = stdin.readline().strip()
        assert address.isnumeric(), "Dirección debe ser alfanumérico, inténtelo nuevamente, te quedan 2 intentos."
    except Exception as error:
        print(error)
        try:
            cantidad: str = stdin.readline().strip()
            assert address.isnumeric(), "Dirección debe ser alfanumérico, inténtelo nuevamente, te queda un intento."
        except Exception as error:
            print(error)
            try:
                cantidad: str = stdin.readline().strip()
                assert address.isnumeric(), "Dirección debe ser alfanumérico, no te quedan más intentos."
            except:
                print(error)
                return None

    days = ["1", "2", "3", "4", "5", "6", "7"]


    try:
        print("Inserte día entre 1 Lunes y 7 Domingo")
        day: str = stdin.readline().strip()
        assert day.isnumeric() and day in days, "Días debe ser entre 1 Lunes y 7 Domingo, inténtelo nuevamente, te quedan 2 intentos."
    except Exception as error:
        print(error)
        try:
            print("Inserte día entre 1 Lunes y 7 Domingo")
            day: str = stdin.readline().strip()
            assert day.isnumeric() and day in days, "Días debe ser entre 1 Lunes y 7 Domingo, inténtelo nuevamente, te queda 1 intento."
        except Exception as error:
            print(error)
            try:
                print("Inserte día entre 1 Lunes y 7 Domingo")
                day: str = stdin.readline().strip()
                assert day.isnumeric() and day in days, "Días debe ser entre 1 Lunes y 7 Domingo, inténtelo nuevamente, no te quedan intentos."
            except:
                print(error)
                return None

    jornadas = ["M", "T", "N"]

    try:
        jornada: str = input("Ingrese jornada (M, T, N)\n")
        assert jornada in jornadas, "Dirección debe ser alfanumérico, inténtelo nuevamente, te quedan 2 intentos."
    except Exception as error:
        print(error)
        try:
            jornada: str = input("Ingrese jornada (M, T, N)\n")
            assert jornada in jornadas, "Dirección debe ser alfanumérico, inténtelo nuevamente, te queda un intento."
        except Exception as error:
            print(error)
            try:
                jornada: str = input("Ingrese jornada (M, T, N)\n")
                assert jornada in jornadas, "Dirección debe ser alfanumérico, no te quedan más intentos."
            except:
                print(error)
                return None
    
    try:
        reciclable: str = input("Kilos de basura reciclable:\n")
        assert reciclable.isnumeric and int(reciclable) >=0, "Kilos de basura debe ser entero positivo, te quedan 2 intentos."
    except Exception as error:
        print(error)
        try:
            reciclable: str = input("Kilos de basura reciclable:\n")
            assert reciclable.isnumeric and int(reciclable) >=0, "Kilos de basura debe ser entero positivo, te quedan 1 intento."
        except Exception as error:
            print(error)
            try:
                reciclable: str = input("Kilos de basura reciclable:\n")
                assert reciclable.isnumeric and int(reciclable) >=0, "Kilos de basura debe ser entero positivo, te quedaste sin intentos."
            except Exception as error:
                print(error)
                return None
    
    try:
        organico: str = input("Kilos de basura organico:\n")
        assert organico.isnumeric and int(organico) >=0, "Kilos de basura debe ser entero positivo, te quedan 2 intentos."
    except Exception as error:
        print(error)
        try:
            organico: str = input("Kilos de basura organico:\n")
            assert organico.isnumeric and int(organico) >=0, "Kilos de basura debe ser entero positivo, te quedan 1 intento."
        except Exception as error:
            print(error)
            try:
                organico: str = input("Kilos de basura organico:\n")
                assert organico.isnumeric and int(organico) >=0, "Kilos de basura debe ser entero positivo, te quedaste sin intentos."
            except Exception as error:
                print(error)
                return None

    sanciones = ["NN", "SS", "PP"]

    try:
        sancion: str = input("Ingrese sancion (NN, SS, PP)\n")
        assert sancion in sanciones, "Sanción debe ser NN, SS o PP, inténtelo nuevamente, te quedan 2 intentos."
    except Exception as error:
        print(error)
        try:
            sancion: str = input("Ingrese sancion (NN, SS, PP)\n")
            assert sancion in sanciones, "Sanción debe ser NN, SS o PP, inténtelo nuevamente, te queda 1 intento."
        except Exception as error:
            print(error)
            try:
                sancion: str = input("Ingrese sancion (NN, SS, PP)\n")
                assert sancion in sanciones, "Sanción debe ser NN, SS o PP, no te quedan intentos."
            except Exception as error:
                print(error)
                return None
    
    registro = {
        "address": address,
        "cantidad": cantidad,
        "day": day,
        "jornada": jornada,
        "reciclable": reciclable,
        "organico": organico,
        "sancion": sancion, 
    }

    return registro



    
    stdout.write(str(address))