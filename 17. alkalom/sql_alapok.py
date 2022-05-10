/*SQL nyelv alapjai*/

truncate table employee;

insert into employee (name, age, salary, position)
values ('Jolán', 65, 100000, 'nyugdijas'); 

insert into employee (name, age, salary, position)
values ('Gizi', 70, 4543214, 'vezető'); 

insert into employee (name, age, salary, position)
values ('Karcsi', 32, 3201000, 'fejlesztő'); 

insert into employee (name, age, salary, position)
values ('Pista', 45, 24515, 'nyugdijas'); 

insert into employee (name, age, salary, position)
values ('József', 50, 1000000, 'igazgató'); 
------------------------------------------------------------------------------

/*alias - adsz egy saját nevet oszlopoknak és tábláknak, amelyekre
* ezután a alias-al tudsz hivatkozni*/
--sales_cognos_dashboard_data
/*where feltétel - filtering funkció - szűrési feltételeket itt adod meg
* 
* aggregált függvényeket nem lehet where feltételben haszálni
* */

select e.* from employee e
where name = 'Karcsi';

/*in clause - több érték megadását jelenti
* 
* not in
* */
select e.* from employee e
where name in ('Karcsi', 'Pista', 'Jolán');

select e.* from employee e
where name not in ('Karcsi', 'Pista', 'Jolán');

/*min, max, count, avg, sum függvények
* aggregált függvények
* */
select max(age), min(age), count(age), avg(age), sum(age) from employee e;

/*group by - csoportositás*/
/* order by - rendezés valamilyen mező szerint, csökkenő, növekvő
* alapértelmezetten csökkenő sorrendet használ
* 
* csökkenő: desc
* növekvő: asc
* */
select e.name, e.age, max(e.age) from employee e
where 1 = 1
group by e.name, e.age
order by e.age desc

limit 1
;

select e.name, e.age from employee e 
order by e.age asc
limit 1;

/* having - ő egy speciális "where" feltétel*/

select e.name, count(e.name) from employee e
where e.name != 'Pista'
group by e.name
having count(e.name) = 1
;
-----------------------------------------------------------------
/* kulcsok, constraintek*/
drop table cars;

create table cars
(
id bigint,
type text,
fuel_type_id int,
color_id int,
created_date date default now()
);


create table colors (
id bigint,
color text
);

create table fuel_type(
id bigint,
fuel_type text
);


insert into colors(id, color) values (1, 'black');
insert into colors(id, color) values (2, 'white');
insert into colors(id, color) values (3, 'red');
insert into colors(id, color) values (4, 'blue');

insert into fuel_type(id, fuel_type) values (1, 'benzin');
insert into fuel_type(id, fuel_type) values (2, 'diesel');
insert into fuel_type(id, fuel_type) values (3, 'electric');


insert into cars(id, type, fuel_type_id, color_id)
values (1, 'BMW', 2, 1);

insert into cars(id, type, fuel_type_id, color_id)
values (2, 'Volvo', 1, 4);

insert into cars(id, type, fuel_type_id, color_id)
values (3, 'Opel', 1, 3);

insert into cars(id, type, fuel_type_id, color_id)
values (4, 'Tesla', 3, 2);

insert into cars(id, type, fuel_type_id, color_id)
values (5, 'Trabant', 1, 4);

insert into cars(id, type, fuel_type_id, color_id)
values (6, 'Skoda', 2, 2);

select * from cars;


/*kulcsok tipusai:
* 
* primary_key - elsődleges kulcs - unique, not null - egyedi és nem lehet null az értéke
* foreign_key - idegen kulcs, a kulcs egy másik tábla adott mezőjére hivatkozik
* 			     csak akkor tudsz hivatkozni egy mezőre, ha az primary_key egyben
* 
*/


/*
* táblák összekapcsolása
* 
* join utasitás
* 
* inner join --
* left join --
* rigth join --
* cross join
* left outer join
* right join
* full outer join
* */


select c.id, c.type, c2.color, ft.fuel_type  from cars c
inner join colors c2 on c.color_id = c2.id
inner join fuel_type ft on c.fuel_type_id = ft.id;

/*sequencia*/

