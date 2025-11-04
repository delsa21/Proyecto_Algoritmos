# main.py
import time
import lcsubstring
import lcsubsequence
import etapa6

def mostrar_encabezado():
    print("-----------------------------------------------")
    print("PROYECTO: BÚSQUEDA DE SIMILITUDES ENTRE TEXTOS")
    print("Autores: Diana Fernanda Delgado S. y Liliana Ramos V.")
    print("Profesor: Omar Mendoza")
    print("Fecha: 03 de noviembre de 2025")
    print("-----------------------------------------------\n")

def mostrar_menu():
    print("Seleccione la etapa que desea ejecutar:\n")
    print("1. Substring común más largo")
    print("2. Subsecuencia común más larga")
    print("3. Comparación completa (LCSstr, LCS, Levenshtein, Jaccard)")
    print("4. Ejecutar todas las etapas (demostración completa)")
    print("0. Salir\n")

def ejecutar_todas():
    print("\nEjecutando Etapa 3: Longest Common Substring...\n")
    time.sleep(1)
    lcsubstring.main()

    print("\nEjecutando Etapa 4: Longest Common Subsequence...\n")
    time.sleep(1)
    lcsubsequence.main()

    print("\nEjecutando Etapa 6: Comparación de los cuatro métodos...\n")
    time.sleep(1)
    etapa6.main()

    print("\nDemostración completa finalizada.")
    print("===============================================")

def main():
    mostrar_encabezado()

    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la opción deseada: ").strip()

        if opcion == "1":
            print("\nEjecutando Etapa 3: Longest Common Substring...\n")
            lcsubstring.main()
        elif opcion == "2":
            print("\nEjecutando Etapa 4: Longest Common Subsequence...\n")
            lcsubsequence.main()
        elif opcion == "3":
            print("\nEjecutando Etapa 6: Comparación de los cuatro métodos...\n")
            etapa6.main()
        elif opcion == "4":
            ejecutar_todas()
        elif opcion == "0":
            print("\nSaliendo del programa. Gracias por usar la aplicación.")
            break
        else:
            print("\nOpción inválida, intente nuevamente.\n")


if __name__ == "__main__":
    main()
