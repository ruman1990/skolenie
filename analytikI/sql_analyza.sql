
with a as (
select typ,objednavka_id,sum(mnozstvo * cena * -1) as suma from objednavky_view where datum < '2024-02-01' and typ='dodavatelska' group by objednavka_id,typ
), b as (
select typ,objednavka_id,sum(mnozstvo * cena) as suma from objednavky_view where datum < '2024-02-01' and typ='odberatelska' group by objednavka_id,typ
), c as(
select * from a union select * from b
)
select sum(suma) from c;


create view objednavky_view as (
select op.id as polozka,
		o.id,
		o.typ,
		o.datum,
		p.nazov as produkt,
		op.mnozstvo,
		op.cena,
		p.kategoria,
		d.nazov as dodavatel,
		od.nazov as odberatel 
	from objednavky_produkty as op 
		join objednavky as o on op.objednavka_id=o.id 
		join produkty as p on op.produkt_id=p.id
		left join dodavatelia as d on o.dodavatel_id=d.id
		left join odberatelia as od on o.odberatel_id=od.id)