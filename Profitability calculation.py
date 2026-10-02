import math

def risk(profits, probabilities):
    M = 0
    for i in range(len(profits)):
        M += profits[i]*probabilities[i]

    V = 0
    for i in range(len(profits)):
        V += ((profits[i] - M) ** 2) * probabilities[i]

    serdkvad_vidh = math.sqrt(V)

    SSV = 0
    for i in range(len(profits)):
        if profits[i] < M:
            SSV += ((profits[i] - M) ** 2) * probabilities[i]

    SSV = math.sqrt(SSV)

    CSV = SSV/M

    print(f"Математичне сподівання: {M}")
    print(f"Варіація: {V}")
    print(f"Середньоквадратичне відхилення: {serdkvad_vidh}")
    print(f"Семіваріація: {SSV}")
    print(f"Коефіцієнт семіваріації: {CSV}")

    return CSV

X_A_prof = [80, 50, -20]
X_A_prob = [0.2, 0.7, 0.1]
X_B_prof = [300, 100, -100]
X_B_prob = [0.2, 0.5, 0.3]

print("Стара модель:\n")
csv_a = risk(X_A_prof, X_A_prob)
print("\nНова модель:\n")
csv_b = risk(X_B_prof, X_B_prob)

print("Висновок:\n")
if csv_a > csv_b:
    print("Нова модель не ризикована, запускаємо її в виробництво.")
else:
    print("Нова модель ризикована, не потрібно її запускати в виробництво.")
