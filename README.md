Finalny projekt z przedmiotu NYPD - Mateusz Boruń

Opis plików/folderów:

- script.py - skrypt będący częścią zadania

- pit_analysis - pakiet biblioteczny będący częścią zadania

- data - dane, na których możemy uruchomić skrypt, pochodzą ze źródeł danych w treści zadania
(są tu po to by mieć na czym uruchomić skryp, a ścieżki do nich oczywiście nie występują w kodzie)

- sample_args.txt - argumenty linii komend, których można użyć, by uruchomić skrypt na danych z folderu dane
(załączam, aby można było łatwo przetestować skrypt)

UWAGA: zaznaczam, że dane są umieszczone wyłącznie po to, żeby zapewnić sprawdzającemu łatwą możliwość uruchomienia skryptu - zdaję sobię sprawę, że co do zasady umieszczanie danych w repozytorium NIE JEST najlepszym pomysłem (bo np. spowalnia klonowanie i w ogólności niepotrzebnie zwiększa rozmiar repozytorium)

- profile - wyniki profilowania (omówię je i opowiem o wnioskach podczas egzaminu)

- setup.py - plik umożliwiający instalację przez pip: bibliotekę instaluje się poleceniem: pip install git+https://github.com/CakePL/NYPD_final_project.git
(wszystkie inne potrzebne biblioteki zostaną zainstalowane automatycznie)

- raport, będący częścią zadania jest w formie interaktywnych wykresów (zrobionych w plotly) - 
można w nich m. in. wybrać fragment wykresu, który chce się obejrzeć (wystarczy zaznaczyć obszar)
oraz zobczyć dokładne wartości (wystarczy najechać myszką na słupek wykresu) - dzięki powyższemu jest to dobry sposób na zaprezentowanie nawet sporych danych
(dzięki dokładnym wartością tabelka nie jest konieczna, a dzięki możliwości dowolnego przybliżania umożliwia wizualizację danych, które umieszczone na standardowym, statycznym wykresie byłyby zupełnie nieczytelne przez ich ilość).
Wykresy powinny pokazać się w wyniku działania skryptu

