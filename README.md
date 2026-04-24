# TOP — Twierdzenie o Periodyczności (Theorem on Periodicity)

> **Nota techniczna:** Projekt ma charakter badawczy i eksperymentalny. Jest to "toy PoC" dla hipotezy matematycznej, która wymaga dalszej formalizacji i ścisłego dowodu analitycznego.

## 📌 O projekcie
Projekt **TOP** koncentruje się na analizie zachowania ciągów potęgowych w pierścieniach reszt modulo $n$, ze szczególnym uwzględnieniem przypadków, w których podstawa i moduł **nie są względnie pierwsze** ($\gcd(a, n) > 1$). 

W klasycznej teorii liczb zbiory te (niebędące grupami, lecz monoidami) są rzadziej analizowane pod kątem ścisłej periodyczności. Celem tego projektu było przeprowadzenie szerokich **symulacji numerycznych** w celu znalezienia powtarzalnych wzorców (patternów) w strukturze tych zbiorów.

## 🧮 Model Matematyczny

Definiujemy zbiór reszt $R(a, n)$ jako:
$$R(a, n) = \{a^k \pmod n : k \in \mathbb{N}_0\}$$

### Dekompozycja parametrów
W moich badaniach przyjąłem następującą strukturę:
- $a = k \cdot b \cdot l$
- $n = k \cdot i \cdot j$

Gdzie:
- $\gcd(a, n) = k$
- $\gcd(j, i) = 1$, $\gcd(j, k) = 1$
- $\gcd(l, k) = 1$, $\gcd(l, b) = 1$

### Zaobserwowane własności (Patterny)
Dzięki symulacjom komputerowym udało się dostrzec następujące zależności:
1.  **Dla $j=1$:** Zachodzi $a^{\phi(n)} \equiv 0 \pmod n$ oraz $k^{\phi(n)} \equiv 0 \pmod n$.
2.  **Stała kardynalność:** $|R(n-1, n)| = 2$ dla każdego $n > 2$.
3.  **Punkt stały cyklu:** Dla $i=1$ oraz $j, k > 1$, symulacje sugerują zależność $k^{\phi(jk)+1} \equiv k \pmod{jk}$, co wskazuje na specyficzny mechanizm powrotu do cyklu mimo braku elementu odwrotnego.

## 🚀 Hipoteza TOP

Głównym przedmiotem badań prowadzonych w tym repozytorium jest następująca hipoteza:

$$|R(a, n^{k+1})| = n \cdot |R(a, n^k)|$$

### Wyniki symulacji
W ramach projektu zaimplementowano skrypty testujące powyższą zależność dla szerokiego spektrum par $(a, n)$. 
- **Skuteczność:** Hipoteza znajduje potwierdzenie w ogromnej większości przypadków.
- **Wyjątki:** Symulacje pozwoliły wykryć **2 konkretne przypadki (wyjątki)**, w których zależność ta nie jest zachowana. Ich analiza jest kluczowa dla zrozumienia granic stosowalności twierdzenia.
- **Status:** Obecnie brak ogólnego dowodu analitycznego — projekt dokumentuje dowody empiryczne i poszukuje matematycznego uzasadnienia mechanizmu "liftingu" okresowości.

## 💻 Rola symulacji w projekcie
Kod zawarty w tym repozytorium służy do:
- Generowania zbiorów $R(a, n)$ dla dużych wartości $n$.
- Automatycznego poszukiwania kontrprzykładów dla postawionej hipotezy.
- Wizualizacji gęstości występowania wzorców periodycznych.

## 🔐 Potencjalne zastosowania
Zrozumienie tej zależności może mieć wpływ na:
- **Kryptografię:** Optymalizacja operacji modularnych w strukturach monoidalnych.
- **Teorię liczb:** Nowe spojrzenie na funkcje wykładnicze modulo $n$ przy braku względnej pierwszości.

---
**Status:** In-progress / Research