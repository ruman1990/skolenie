SELECT op.objednavka_id,
    op.mnozstvo,
    op.cena,
    o.typ,
    o.datum,
    p.nazov,
    d.nazov AS dodavatel,
    od.nazov AS odberatel
   FROM objednavky_produkty op
     JOIN objednavky o ON op.objednavka_id = o.id
     JOIN produkty p ON p.id = op.produkt_id
     LEFT JOIN dodavatelia d ON d.id = o.dodavatel_id
     LEFT JOIN odberatelia od ON od.id = o.odberatel_id;