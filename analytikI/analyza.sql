1) Mesačné počty a obrat podľa typu
SELECT
  date_trunc('month', ov.datum)::date AS mesiac,
  ov.typ,                                -- 'dodavatelska' | 'odberatelska'
  COUNT(DISTINCT ov.objednavka_id) AS pocet_objednavok,
  SUM(ov.mnozstvo) AS ks_spolu,
  SUM(ov.mnozstvo * ov.cena) AS obrat
FROM objednavky_view ov
GROUP BY 1, 2
ORDER BY 1, 2;


2) Mesačné saldo (tržby – nákupy) v jednej tabuľke
SELECT
  date_trunc('month', ov.datum)::date AS mesiac,
  SUM(CASE WHEN ov.typ = 'odberatelska' THEN ov.mnozstvo * ov.cena ELSE 0 END) AS trzby,
  SUM(CASE WHEN ov.typ = 'dodavatelska' THEN ov.mnozstvo * ov.cena ELSE 0 END) AS nakupy,
  SUM(CASE WHEN ov.typ = 'odberatelska' THEN ov.mnozstvo * ov.cena
           WHEN ov.typ = 'dodavatelska' THEN - ov.mnozstvo * ov.cena
           ELSE 0 END) AS saldo
FROM objednavky_view ov
GROUP BY 1
ORDER BY 1;

3) Najobjednávanejší produkt po mesiacoch (podľa množstva)
WITH s AS (
  SELECT
    date_trunc('month', datum)::date AS mesiac,
    nazov AS produkt,
    SUM(mnozstvo) AS ks
  FROM objednavky_view
  GROUP BY 1, 2
)
SELECT s.mesiac, s.produkt, s.ks
FROM s
JOIN (
  SELECT mesiac, MAX(ks) AS max_ks
  FROM s
  GROUP BY mesiac
) m ON m.mesiac = s.mesiac AND m.max_ks = s.ks
ORDER BY s.mesiac;


(alternatíva) Najvýnosnejší produkt po mesiacoch (podľa obratu)
WITH s AS (
  SELECT
    date_trunc('month', datum)::date AS mesiac,
    nazov AS produkt,
    SUM(mnozstvo * cena) AS obrat
  FROM objednavky_view
  GROUP BY 1, 2
)
SELECT s.mesiac, s.produkt, s.obrat
FROM s
JOIN (
  SELECT mesiac, MAX(obrat) AS max_obrat
  FROM s
  GROUP BY mesiac
) m ON m.mesiac = s.mesiac AND m.max_obrat = s.obrat
ORDER BY s.mesiac;


-- Tržby (odberatelia)
SELECT
  date_trunc('month', o.datum)::date AS mesiac,
  od.nazov AS odberatel,
  SUM(op.mnozstvo * op.cena) AS trzby
FROM objednavky o
JOIN objednavky_produkty op ON op.objednavka_id = o.id
JOIN odberatelia od ON od.id = o.odberatel_id
WHERE o.typ = 'odberatelska'
GROUP BY 1, 2
ORDER BY 1, 3 DESC;

-- Nákupy (dodávatelia)
SELECT
  date_trunc('month', o.datum)::date AS mesiac,
  d.nazov AS dodavatel,
  SUM(op.mnozstvo * op.cena) AS nakupy
FROM objednavky o
JOIN objednavky_produkty op ON op.objednavka_id = o.id
JOIN dodavatelia d ON d.id = o.dodavatel_id
WHERE o.typ = 'dodavatelska'
GROUP BY 1, 2
ORDER BY 1, 3 DESC;

-- 6) Priemerná jednotková cena produktu v čase (vážený priemer)

SELECT
  ov.nazov AS produkt,
  SUM(ov.mnozstvo * ov.cena) / NULLIF(SUM(ov.mnozstvo), 0) AS priemerna_cena
FROM objednavky_view ov where typ ='odberatelska'
GROUP BY 1
ORDER BY 1;