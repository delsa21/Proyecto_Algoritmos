# longest common subsequence
import time


def longest_common_subsequence(s1: str, s2: str) -> str:
    n, m = len(s1), len(s2)
    dp = [[""] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + s1[i - 1]
            else:
                dp[i][j] = (
                    dp[i - 1][j]
                    if len(dp[i - 1][j]) > len(dp[i][j - 1])
                    else dp[i][j - 1]
                )
    return dp[n][m]


def dividirBloques(texto: str, tamaño: int = 3000) -> list:
    # divide el texto en fragmentos de un tamaño en especifico
    return [texto[i : i + tamaño] for i in range(0, len(texto), tamaño)]


def main():
    # lee los textos ya limpios
    with open("prideandprejudice_clean.txt", "r", encoding="utf-8") as f:
        texto1 = f.read()
    with open("senseandsensibility_clean.txt", "r", encoding="utf-8") as f:
        texto2 = f.read()

    # divide los textos en bloques para mejorar su lectura
    bloques1 = dividirBloques(texto1, tamaño=2000)
    bloques2 = dividirBloques(texto2, tamaño=2000)

    mejor_subseq = ""  # mejor subsecuencia encontrada
    inicio = time.time()  # inicia el conteo de tiempo

    # compara bloque i con bloque i de ambos textos
    for i in range(min(len(bloques1), len(bloques2))):
        subseq = longest_common_subsequence(bloques1[i], bloques2[i])
        if len(subseq) > len(mejor_subseq):
            mejor_subseq = subseq

    duracion = time.time() - inicio  # calcula el tiempo de ejecución
    porcentaje = (
        len(mejor_subseq) / min(len(texto1), len(texto2))
    ) * 100  # calcula el porcentaje de similitud

    # mostrar resultados
    print(f"Longitud LCS: {len(mejor_subseq)}")
    print(f"Porcentaje de similitud: {porcentaje:.4f}%")
    print(f"Tiempo de ejecución: {duracion:.2f} s")
    print("Fragmento:", mejor_subseq[:300] + ("..." if len(mejor_subseq) > 300 else ""))


main()
