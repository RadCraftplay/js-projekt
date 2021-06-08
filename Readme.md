# Program do wyszukiwania połączeń kolejowych
Opis zadania:
- Dwa okna:
	- Pierwsze: ustawianie połączeń (dwie kolumny przycisków opcji (radio button) lub listy rozwijane z nazwami miejscowości), przycisk "połącz", przycisk "rozłącz" oraz macierz istniejących połączeń (macierz sąsiedztwa grafu połączeń). Użytkownik wybiera miejscowości i tworzy między nimi połączenie.
	- Drugie: wyszukiwanie połączenia, dwie listy rozwijane, pierwsza oznaczająca miasto startowe, druga miasto docelowe, przycisk "szukaj", oraz lista przystanków na znalezionej trasie
- Program na początku ma zdefiniowane kilka (10) miast oraz połączeń między nimi (początkowo do każdego miasta da się dojechać, ale nie z każdego bezpośrednio do innego).
- Użytkownik wybiera miasto z którego chce dojechać, oraz miasto docelowe i wciska przycisk "szukaj':
	- Połączenie znalezione: wpisuje do listy kolejne przystanki, np: "Kraków -> Katowice", "Katowice -> Wrocław”, "Wrocław -> Ankh-Morpork"
	- Połączenia brak: wyskakuje okienko z informacją "Brak połączenia na tej trasie"
- Program powinien realizować wyszukiwanie połączeń za pomocą algorytmu BFS. Graf połączeń powinien mieć dwie możliwe reprezentacje (do wyboru w pierwszym oknie): macierz sąsiedztwa albo listy sąsiedztwa, realizowane jako dwie klasy dziedziczące po klasie AbstractGraph definiującej niezbędny interfejs (pobranie listy wierzchołków, pobranie krawędzi incydentnych z wierzchołkiem, pobranie wierzchołków łączonych przez krawędź itp.). Zmiana reprezentacji powinna być możliwa w dowolnym momencie działania programu. Implementacja algorytmu BFS powinna być jedna i działać na obu możliwych reprezentacjach grafu (ma wykorzystywać wyłącznie metody klasy AbstractGraph definiujące interfejs).

Testy:
1. Wyszukanie połączenia bezpośredniego między dwoma miastami.
2. Wyszukanie połączenia między dwoma miastami z przynajmniej dwoma przystankami pośrednimi.
3. Dodanie połączenia bezpośredniego między dwoma miastami z punktu b. - oczekiwana informacja o połączeniu bezpośrednim.
4. Usunięcie połączeń bezpośrednich między miastami z punktu a., wyszukanie połączenia - oczekiwana informacja o przesiadce.
5. Usunięcie wszystkich połączeń do danego miasta - oczekiwana informacja o braku połączenia.
6. Wykonanie testu b przy drugiej reprezentacji grafu.
7. Wykonanie testu c przy drugiej reprezentacji grafu.