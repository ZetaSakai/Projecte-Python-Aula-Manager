# AulaManager - Operació Aula Zero

equips = []  # Lista de equipos
contador_id = 1  # Variable ID automático

# Bucle principal
while True:
    print("\n===== AulaManager =====")
    print("1) Registrar equip")
    print("2) Consultar equip")
    print("3) Canviar estat")
    print("4) Modificar dades")
    print("5) Gestionar incidencia")
    print("0) Sortir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        equipo = {
            "id": contador_id,
            "tipo": input("Tipo (PC, Portátil, Impresora, Switch, AP, Servidor): "),
            "nombre": input("Nombre del equipo: "),
            "aula": input("Aula: "),
            "serie": input("Número de serie: "),
            "so": input("Sistema operativo: "),
            "ram": int(input("RAM (ej: 16): ")),
            "disc": input("Disco (ej: 512GB SSD): "),
            "estado": input("Estado (operativo/avariado/reparación/baja): "),
            "ip": input("IP (opcional): "),
            "mac": input("MAC (opcional): "),
            "observaciones": input("Observaciones: ")
        }

        equips.append(equipo)
        print(f"Equipo registrado con ID: {contador_id}")
        contador_id += 1

    elif opcion == "2":
        if not equips:
            print("No hay equipos registrados.")
        else:
            for equipo in equips:
                print("----------------------------")
                print(f"ID: {equipo['id']}")
                print(f"Tipo: {equipo['tipo']}")
                print(f"Nombre: {equipo['nombre']}")
                print(f"Aula: {equipo['aula']}")
                print(f"Serie: {equipo['serie']}")
                print(f"SO: {equipo['so']}")
                print(f"RAM: {equipo['ram']} GB")
                print(f"Disco: {equipo['disc']}")
                print(f"Estado: {equipo['estado']}")
                print(f"IP: {equipo['ip']}")
                print(f"MAC: {equipo['mac']}")
                print(f"Observaciones: {equipo['observaciones']}")

    elif opcion == "3":
        serie_buscar = input("Introduce el número de serie del equipo: ")
        for equipo in equips:
            if equipo["serie"] == serie_buscar:
                print(f"El estado actual es: {equipo['estado']}")
                nuevo_estado = input("Introduce el nuevo estado: ")
                equipo["estado"] = nuevo_estado
                print("Estado actualizado correctamente.")
                break
        else:
            print("No se ha encontrado ningún equipo con ese número de serie.")

    elif opcion == "4":
        print("Función de modificación aún no implementada.")

    elif opcion == "5":
        print("Gestión de incidencias aún no implementada.")

    elif opcion == "0":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida.")