-- Tabuľka produktov
CREATE TABLE produkty (
    id SERIAL PRIMARY KEY,
    nazov TEXT NOT NULL,
    pocet INTEGER NOT NULL,
    cena NUMERIC(10,2) NOT NULL,
    kategoria INTEGER NOT NULL
);

-- Tabuľka dodávateľov
CREATE TABLE dodavatelia (
    id SERIAL PRIMARY KEY,
    nazov TEXT NOT NULL,
    adresa TEXT NOT NULL,
    ico VARCHAR(16) NOT NULL
);

-- Tabuľka odberateľov
CREATE TABLE odberatelia (
    id SERIAL PRIMARY KEY,
    nazov TEXT NOT NULL,
    adresa TEXT NOT NULL,
    ico VARCHAR(16) NOT NULL
);

-- Tabuľka objednávok (dodávateľské aj odberateľské)
CREATE TABLE objednavky (
    id SERIAL PRIMARY KEY,
    typ VARCHAR(20) NOT NULL,  -- 'dodavatelska' alebo 'odberatelska'
    datum TIMESTAMP NOT NULL,
    dodavatel_id INTEGER REFERENCES dodavatelia(id),
    odberatel_id INTEGER REFERENCES odberatelia(id)
);

-- Prepojovacia tabuľka objednávka <-> produkty
CREATE TABLE objednavky_produkty (
    id SERIAL PRIMARY KEY,
    objednavka_id INTEGER REFERENCES objednavky(id),
    produkt_id INTEGER REFERENCES produkty(id),
    mnozstvo INTEGER NOT NULL,
    cena NUMERIC(10,2) NOT NULL
);



INSERT INTO produkty (nazov, pocet, cena, kategoria) VALUES
('chlieb', 170, 2.67, 3),
('mlieko', 43, 7.67, 3),
('maslo', 174, 7.28, 3),
('vajcia', 134, 8.98, 3),
('ryža', 82, 7.99, 3),
('cestoviny', 102, 2.45, 3),
('soľ', 172, 6.59, 3),
('cukor', 19, 3.69, 3),
('olej', 112, 6.41, 3),
('jablko', 48, 1.37, 3),
('banán', 88, 7.15, 3),
('paradajka', 180, 3.84, 3),
('zemiaky', 110, 4.86, 3),
('mrkva', 55, 7.92, 3),
('syr', 69, 8.07, 3),
('jogurt', 13, 8.19, 3),
('paštéta', 140, 1.73, 3),
('pažítka', 70, 7.64, 3),
('bryndza', 61, 1.38, 3),
('cibuľa', 38, 8.72, 3),
('uhorka', 178, 3.33, 3),
('kuracie prsia', 23, 8.86, 3),
('kuracie stehná', 134, 1.24, 3),
('bravčové mäso', 182, 8.66, 3),
('šunka', 191, 5.32, 3),
('slanina', 190, 4.21, 3),
('parížsky šalát', 20, 4.82, 3),
('kyslá smotana', 136, 6.73, 3),
('pomaranč', 139, 0.95, 3),
('hrozno', 10, 1.34, 3),
('ananas', 109, 4.29, 3),
('mango', 86, 6.36, 3),
('cesnak', 158, 3.54, 3),
('brokolica', 14, 3.72, 3),
('kukurica', 130, 5.81, 3),
('hrášok', 62, 6.86, 3),
('karfiol', 136, 2.81, 3),
('mliečna čokoláda', 47, 7.52, 3),
('horalka', 137, 4.72, 3),
('lentilky', 61, 1.73, 3),
('med', 170, 5.11, 3),
('čokoládový puding', 81, 4.35, 3),
('puding', 135, 8.58, 3),
('piškóty', 121, 2.47, 3),
('slaný snack', 9, 2.03, 3),
('kečup', 81, 5.57, 3),
('horčica', 125, 6.71, 3),
('majonéza', 32, 7.45, 3),
('čierne korenie', 62, 6.23, 3),
('čaj', 153, 4.51, 3),
('káva', 197, 8.09, 3),
('minerálka', 176, 8.37, 3),
('balená voda 1.5l', 113, 1.5, 3),
('toastový chlieb', 91, 1.85, 3),
('zubná pasta', 75, 1.78, 1),
('mydlo', 105, 3.22, 1),
('prací prášok', 13, 15.6, 1),
('saponát', 188, 7.31, 1),
('šampón', 113, 11.8, 1),
('toaletný papier', 159, 5.24, 1),
('papierové utierky', 127, 4.89, 1),
('vreckovky', 31, 1.92, 1),
('osviežovač vzduchu', 130, 13.42, 1),
('kuchynské utierky', 72, 5.13, 1),
('čistiaci prostriedok', 117, 14.32, 1),
('batérie AAA', 28, 7.11, 1),
('batérie AA', 48, 11.82, 1),
('žiarovka', 110, 6.11, 1),
('zápalky', 66, 2.11, 1),
('sviečka', 109, 4.7, 1),
('vrece na odpadky', 89, 2.84, 1),
('alobal', 72, 1.39, 1),
('potravinová fólia', 157, 1.2, 1),
('servítky', 118, 0.92, 1),
('igelitové tašky', 59, 0.41, 1),
('vrecia na triedený odpad', 132, 6.92, 1),
('igelitový obrus', 144, 3.33, 1),
('kancelársky papier', 178, 15.49, 1),
('pero', 71, 0.93, 1),
('ceruzka', 95, 0.71, 1),
('lepidlo', 181, 1.18, 1),
('zošívačka', 21, 6.17, 1),
('nožnice', 141, 2.53, 1),
('pravítko', 99, 1.41, 1),
('fixka', 54, 1.15, 1),
('marker', 35, 2.07, 1),
('diár', 129, 4.88, 1),
('zošit', 176, 1.48, 1),
('lepiaca páska', 90, 2.26, 1),
('kalkulačka', 111, 8.16, 1),
('guma na gumovanie', 160, 0.64, 1),
('struhadlo na ceruzky', 50, 1.18, 1),
('pravítko 30 cm', 70, 1.57, 1),
('zakladač', 71, 2.87, 1),
('spisová obálka', 77, 0.99, 1),
('obálka', 88, 0.42, 1),
('písací blok', 109, 2.03, 1),
('farbičky', 182, 2.21, 1);


INSERT INTO dodavatelia (nazov, adresa, ico) VALUES
('AgroTrade, s.r.o.',        'Hlavná 1, 90001 Modra',         '10000001'),
('SlovPotraviny, a.s.',      'Potravinárska 45, 82009 BA',    '10000002'),
('Mliečna farma, s.r.o.',    'Lúčná 17, 03861 Vrútky',        '10000003'),
('FreshFruit Import',        'Ovocná 88, 03601 Martin',       '10000004'),
('BioZelenina SK',           'Záhradnícka 8, 91701 Trnava',   '10000005'),
('SuperMarket SK',           'Centrum 12, 04001 Košice',      '10000006'),
('Gastro Dodávky',           'Gastronómov 9, 85101 BA',       '10000007'),
('Papiernictvo+, s.r.o.',    'Kancelárska 19, 04013 KE',      '10000008'),
('DrogeriaMax',              'Hygienická 14, 82106 BA',       '10000009'),
('OfficeTrade',              'Papierová 3, 91101 TN',         '10000010'),
('Potraviny Expert',         'Potravinárska 12, 82101 BA',    '10000011'),
('Veggie Land',              'Zelená 3, 01001 Žilina',        '10000012'),
('Pečiváreň Dobrota',        'Cesta 4, 05201 Spišská N.',     '10000013'),
('Mäsoprodukt',              'Mäsová 22, 03101 Liptovský M.', '10000014'),
('Sladké Sny',               'Cukrová 7, 91701 Trnava',       '10000015'),
('CaféShop',                 'Kávová 10, 85001 BA',           '10000016'),
('DairyBest',                'Mliekárenská 5, 97401 BB',      '10000017'),
('Ovocný Raj',               'Jablková 9, 90021 Svätý Jur',   '10000018'),
('ZeleninaMarket',           'Šalátová 16, 04001 KE',         '10000019'),
('SkladMix',                 'Skladová 31, 08001 Prešov',     '10000020'),
('MäsoVeľkoobchod',          'Mäsová 19, 04012 Košice',       '10000021'),
('Delikatesy',               'Delikátna 2, 90042 Dun. Lužná', '10000022'),
('Voda Plus',                'Vodnička 44, 04023 KE',         '10000023'),
('Papier Profi',             'Papierenská 8, 01012 Žilina',   '10000024'),
('Hygiena s.r.o.',           'Čistá 1, 84101 Bratislava',     '10000025'),
('Kancelár Expert',          'Kancelárska 2, 82109 BA',       '10000026'),
('Domáce potreby',           'Potrebná 12, 91105 Trenčín',    '10000027'),
('SuperObchod',              'Obchodná 22, 08501 Bardejov',   '10000028'),
('TOP Dodávky',              'Špičková 7, 94901 Nitra',       '10000029'),
('ABC Supplies',             'Dodávateľská 15, 04013 KE',     '10000030');


INSERT INTO odberatelia (nazov, adresa, ico) VALUES
('Jednota obchod',           'Námestie 1, 96001 Zvolen',        '20000001'),
('ZŠ Jarná',                 'Jarná 2, 82108 Bratislava',       '20000002'),
('Potraviny u Kováča',       'Kováčska 7, 08501 Bardejov',      '20000003'),
('Reštaurácia Na rohu',      'Rohová 1, 04001 Košice',          '20000004'),
('Obchod Doma',              'Doma 24, 91105 Trenčín',          '20000005'),
('Lekáreň Zdravie',          'Zdravotná 5, 90201 Pezinok',      '20000006'),
('Kancel Office',            'Pracovná 9, 91702 Trnava',        '20000007'),
('Hotel Centrum',            'Centrum 1, 01001 Žilina',         '20000008'),
('SuperMarket Novák',        'Novákova 16, 90203 Pezinok',      '20000009'),
('Materská škola Slniečko',  'Slniečkova 1, 94501 Komárno',     '20000010'),
('Gastro Klub',              'Klubová 5, 04001 Košice',         '20000011'),
('Kaviareň Biela Ruža',      'Biely dom 4, 96001 Zvolen',       '20000012'),
('Fitness Gym',              'Športová 10, 01002 Žilina',       '20000013'),
('Bio Trh',                  'Trhová 7, 82107 Bratislava',      '20000014'),
('MŠ Dúha',                  'Dúhová 3, 97401 Banská Bystrica', '20000015'),
('Obchod Zuzka',             'Obchodná 6, 85101 BA',            '20000016'),
('IT Company',               'Technologická 2, 83104 Bratislava','20000017'),
('Papiernictvo XYZ',         'Papierová 10, 04013 KE',          '20000018'),
('Drogerka',                 'Drogistická 2, 91701 Trnava',     '20000019'),
('Veľkoobchod Mix',          'Veľká 22, 04014 Košice',          '20000020'),
('Hotel Most',               'Mostová 11, 94501 Komárno',       '20000021'),
('ZŠ Nová',                  'Školská 15, 84104 Bratislava',    '20000022'),
('Papierová Fantázia',       'Papiernická 3, 01013 Žilina',     '20000023'),
('Kuchyňa Luna',             'Lunárna 19, 83103 Bratislava',    '20000024'),
('Cukráreň Sneh',            'Cukrová 1, 90201 Pezinok',        '20000025'),
('Obchod u Petra',           'Petrova 16, 08001 Prešov',        '20000026'),
('Kvetinárstvo Green',       'Kvetinová 5, 81109 Bratislava',   '20000027'),
('Lekáreň Harmónia',         'Harmónia 12, 96002 Zvolen',       '20000028'),
('MŠ Slnečnica',             'Slnečná 7, 04015 Košice',         '20000029'),
('Obchod Gurmán',            'Gurmánska 13, 08501 Bardejov',    '20000030');




