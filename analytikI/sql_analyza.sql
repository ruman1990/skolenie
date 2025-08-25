
with a as (
select typ,objednavka_id,sum(mnozstvo * cena * -1) as suma from objednavky_view where datum < '2024-02-01' and typ='dodavatelska' group by objednavka_id,typ
), b as (
select typ,objednavka_id,sum(mnozstvo * cena) as suma from objednavky_view where datum < '2024-02-01' and typ='odberatelska' group by objednavka_id,typ
), c as(
select * from a union select * from b
)
select sum(suma) from c;




create view objednavky_view as
 SELECT op.objednavka_id,
    o.datum,
    o.typ,
    p.nazov,
    op.mnozstvo,
    op.cena,
    p.kategoria
   FROM objednavky_produkty op
     JOIN produkty p ON p.id = op.produkt_id
     JOIN objednavky o ON op.objednavka_id = o.id;
