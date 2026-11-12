-- nazov produktov, nazov dodavatela, odberatela, cenu, mnozstvo, datum objednavky, typ objednavky
create view vlado.objednavka_view AS
select op.objednavka_id,
		op.mnozstvo,
		op.cena,
		o.typ,
		o.datum,
		p.nazov,
		case when o.typ = 'odberatelska' then od.nazov
		when o.typ = 'dodavatelska' then d.nazov else null end as spolocnost
	from vlado.objednavky_produkty op 
		join vlado.objednavky o on op.objednavka_id=o.id 
		join vlado.produkty p on op.produkt_id=p.id
		left join vlado.dodavatelia d on o.dodavatel_id=d.id
		left join vlado.odberatelia od on o.odberatel_id=od.id