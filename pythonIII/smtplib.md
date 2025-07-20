Samozrejme! Tu je **učebný text o posielaní emailov v Pythone** – najprv základná teória, potom praktická práca s ukážkami kódu.

---

# Posielanie emailov v Pythone

## Teória

Python umožňuje posielať e-maily priamo z programov a skriptov pomocou vstavaných knižníc. Najčastejšie sa využíva modul **`smtplib`** (na odosielanie cez SMTP server) a **`email`** (na vytváranie a formátovanie správ).

* **SMTP** (Simple Mail Transfer Protocol) je štandardný protokol na odosielanie emailov cez internet.
* Posielanie emailov v Pythone je možné automatizovať – napríklad pre zasielanie upozornení, výsledkov, reportov a pod.

> **Pozor:** Na posielanie e-mailov potrebujete prístup k SMTP serveru (napríklad Gmail, Outlook, vlastný firemný server a pod.) a údaje na prihlásenie.

---

## Základné moduly

* **`smtplib`** – umožňuje komunikovať s SMTP serverom (posielanie správ).
* **`email`** – slúži na tvorbu správ, pridávanie predmetu, príloh, formátovanie HTML správ a pod.

---

## Základný príklad – posielanie jednoduchého emailu

Tento príklad ukazuje, ako poslať jednoduchý textový email cez Gmail SMTP.

```python
import smtplib
from email.message import EmailMessage

# Nastavenie údajov
odosielatel = "vas.email@gmail.com"
prijemca = "niekto@domena.com"
heslo = "VASE_HESLO_DO_GMAILU"  # alebo aplikacne heslo

# Vytvorenie správy
msg = EmailMessage()
msg.set_content("Toto je testovacia správa od Pythonu.")
msg["Subject"] = "Testovací email"
msg["From"] = odosielatel
msg["To"] = prijemca

# Pripojenie na Gmail SMTP server a odoslanie
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(odosielatel, heslo)
    smtp.send_message(msg)
```

> **Bezpečnosť:** Odporúča sa používať **aplikáčne heslo** pre Gmail, nie bežné prihlasovacie heslo! (Viac info: [Google - aplikáčné heslá](https://myaccount.google.com/apppasswords)).

---

## Vysvetlenie kódu

1. **Import knižníc:**

   * `smtplib` na komunikáciu so serverom,
   * `email.message.EmailMessage` na vytvorenie emailovej správy.

2. **Nastavenie údajov:**

   * Email odosielateľa, príjemcu a heslo.

3. **Vytvorenie správy:**

   * Nastavenie obsahu, predmetu, odosielateľa a príjemcu.

4. **Odoslanie:**

   * Pripojenie k SMTP serveru cez SSL.
   * Prihlásenie.
   * Odoslanie správy.

---

## Odosielanie HTML emailu

Ak chcete poslať email vo formáte HTML (s obrázkami, odkazmi, formátovaním):

```python
import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "HTML email"
msg["From"] = odosielatel
msg["To"] = prijemca
msg.set_content("Toto je verzia pre staré emailové klienty.", subtype="plain")
msg.add_alternative("""
<html>
  <body>
    <h1>Ahoj!</h1>
    <p>Toto je <b>HTML</b> verzia emailu.</p>
  </body>
</html>
""", subtype="html")

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(odosielatel, heslo)
    smtp.send_message(msg)
```

---

## Pridanie prílohy k emailu

```python
import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "Email s prílohou"
msg["From"] = odosielatel
msg["To"] = prijemca
msg.set_content("Pozri si prílohu.")

# Priloženie súboru (napr. PDF)
with open("dokument.pdf", "rb") as f:
    file_data = f.read()
    file_name = "dokument.pdf"
msg.add_attachment(file_data, maintype="application", subtype="pdf", filename=file_name)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(odosielatel, heslo)
    smtp.send_message(msg)
```

---

## Bezpečnostné rady

* Nikdy neukladajte skutočné heslá do verejných skriptov!
* Používajte **aplikáčne heslá** alebo šifrovanie hesiel.
* Overte si povolenia na SMTP serveri a limity (niektoré emaily môžu byť označené ako SPAM).

---

## Zhrnutie

* V Pythone môžete posielať emaily pomocou modulov `smtplib` a `email`.
* Potrebujete SMTP server a prístupové údaje.
* E-maily môžu byť textové, HTML alebo môžu obsahovať prílohy.
* Je dôležité dbať na bezpečnosť a správne nastavenie emailového účtu.

---

Ak chceš, môžem pridať aj cvičenia, otázky na precvičenie, alebo ďalšie pokročilé tipy (napr. odosielanie hromadných emailov). Stačí napísať!
