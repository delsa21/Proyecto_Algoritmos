import time
from typing import Tuple
from itertools import islice

#longest common substring (LCSstr)
def longest_common_substring(s1: str, s2: str) -> Tuple[int, str]:
    n, m = len(s1), len(s2)
    prev = [0] * (m + 1)
    max_len = 0
    end_index = 0
    for i in range(1, n + 1):
        curr = [0] * (m + 1)
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                curr[j] = prev[j - 1] + 1
                if curr[j] > max_len:
                    max_len = curr[j]
                    end_index = i
        prev = curr
    fragment = s1[end_index - max_len:end_index]
    return max_len, fragment


#longest common subsequence (LCS)
def longest_common_subsequence(s1: str, s2: str) -> str:
    n, m = len(s1), len(s2)
    dp = [[""] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + s1[i - 1]
            else:
                dp[i][j] = dp[i - 1][j] if len(dp[i - 1][j]) > len(dp[i][j - 1]) else dp[i][j - 1]
    return dp[n][m]

#distancia de Levenshtein
def levenshtein_distance(s1: str, s2: str) -> int:
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,      # eliminación
                dp[i][j - 1] + 1,      # inserción
                dp[i - 1][j - 1] + cost  # sustitución
            )
    return dp[n][m]

#similaridad de Jaccard usando n-gramas
def jaccard_similarity(s1: str, s2: str, n: int = 3) -> float:
    def ngrams(text, n):
        return {text[i:i + n] for i in range(len(text) - n + 1)}
    set1 = ngrams(s1, n)
    set2 = ngrams(s2, n)
    inter = len(set1 & set2)
    union = len(set1 | set2)
    return inter / union if union != 0 else 0

#código de comparación de todos los métodos
def main():
    with open("prideandprejudice_clean.txt", "r", encoding="utf-8") as f:
        text1 = f.read()[:5000]  # se limita para evitar excesivo tiempo
    with open("senseandsensibility_clean.txt", "r", encoding="utf-8") as f:
        text2 = f.read()[:5000]

    resultados = []

    #LCSstr
    start = time.time()
    lcsstr_len, frag = longest_common_substring(text1, text2)
    t1 = time.time() - start
    sim1 = (lcsstr_len / min(len(text1), len(text2))) * 100
    resultados.append(("LCSstr", f"{sim1:.4f}%", f"{t1:.2f}s", frag[:80]))

    #LCS
    start = time.time()
    subseq = longest_common_subsequence(text1[:2000], text2[:2000])
    t2 = time.time() - start
    sim2 = (len(subseq) / min(len(text1[:2000]), len(text2[:2000]))) * 100
    resultados.append(("LCS", f"{sim2:.4f}%", f"{t2:.2f}s", subseq[:80]))

    #Levenshtein
    start = time.time()
    dist = levenshtein_distance(text1[:1000], text2[:1000])
    t3 = time.time() - start
    max_len = max(len(text1[:1000]), len(text2[:1000]))
    sim3 = ((max_len - dist) / max_len) * 100
    resultados.append(("Levenshtein", f"{sim3:.4f}%", f"{t3:.2f}s", "N/A"))

    #Jaccard n-gramas
    start = time.time()
    sim4 = jaccard_similarity(text1, text2, n=3) * 100
    t4 = time.time() - start
    resultados.append(("Jaccard (3-gramas)", f"{sim4:.4f}%", f"{t4:.2f}s", "N/A"))

    #Mostrar resultados
    print(f"{'Método':<25}{'Similitud':<15}{'Tiempo':<15}{'Ejemplo / Fragmento'}")
    print("-" * 80)
    for r in resultados:
        print(f"{r[0]:<25}{r[1]:<15}{r[2]:<15}{r[3]}")

main()