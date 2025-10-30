               ┌───────────────────────┐
               │      produkty         │
               │───────────────────────│
               │ id SERIAL PK          │
               │ nazov TEXT            │
               │ pocet INTEGER         │
               │ cena NUMERIC(10,2)    │
               │ kategoria INTEGER      │
               └──────────┬────────────┘
                          │
                          │ produkt_id
                          │
             ┌────────────┴────────────┐
             │ objednavky_produkty     │
             │─────────────────────────│
             │ id SERIAL PK            │
             │ objednavka_id INTEGER FK│
             │ produkt_id INTEGER FK   │
             │ mnozstvo INTEGER        │
             │ cena NUMERIC(10,2)      │
             └────────────┬────────────┘
                          │
                          │ objednavka_id
                          │
             ┌────────────┴────────────┐
             │      objednavky         │
             │─────────────────────────│
             │ id SERIAL PK            │
             │ typ VARCHAR(20)         │
             │ datum TIMESTAMP         │
             │ dodavatel_id INTEGER FK │
             │ odberatel_id INTEGER FK │
             └──────┬──────────┬───────┘
                    │          │
     dodavatel_id ──┘          └── odberatel_id
                    │
       ┌────────────┘
       │
┌──────┴─────────────┐           ┌──────────────────────┐
│    dodavatelia     │           │    odberatelia       │
│────────────────────│           │──────────────────────│
│ id SERIAL PK       │           │ id SERIAL PK         │
│ nazov TEXT          │           │ nazov TEXT           │
│ adresa TEXT         │           │ adresa TEXT          │
│ ico VARCHAR(16)     │           │ ico VARCHAR(16)      │
└─────────────────────┘           └──────────────────────┘
