-- egy soros comment

/* több soros commentre
 egy lehetséges opció
 igy ni*/

-- connection: egy db adatbázis kapcsolat a dbeaverben
-- 			ez ahhoz kell, hogy az adatbázist elérjük


-- session: egy db kapcsolat az adatbázishoz a dbeaverből
--         ez ahhoz kell, hogy sql utasitásokat el tudjuk küldeni az adatbázisnak

/*
 * táblák
 * nézetek
 * vannak olyan objektumok, amelyek a táblák között épülneki ki: kulcsok
 * indexek - performancia okból hozzuk létre
 * */


-- Relációs adatbázis - RDBSM - Relational Data Base System Management

-- mi az a reláció: kapcsolat az adat között 

-- amikor relációs adatbázisról beszélünk,
-- az adja meg, hogy milyen a megközelitése az adat tárolásának

-- táblák: olyanok mint az excel táblázat


--employee tábla létrehozása: name, age, salary, position

/*
 * Azok az utasitások, amelyek objektumokat hoznak létre, törölnek,
 * módositanak, DDL utasitásoknak nevezzük
 * 
 * DDL - Data Definition Language
 * 
 * create: objektum létrehozás
 * drop: objektum "eldobása" - törlése
 * truncate: ürit bizonyos objektumokat: táblákat, particiókat
 * comment on: kommentet tudsz tenni bizonyos objektumokra: táblákra, táblák oszlopaira
 * rename: átnezeni objektumokat - veszélyes, kerülendő
 * alter: módositani bizonyos objektumok szerkezetét: táblát, sessiont, táblák oszlopait
 * 
 * 
 * */

/* tábla létrehozása*/
create table if not exists employee (
name text, 
age int, 
salary bigint, 
position text

);

/* tábla eldobása - törlése*/
drop table if exists employee;

/*minden adat lekérdezése a táblából*/
select * from employee;

/*adat beszúrása a táblába*/
/*minden esetben add meg a mezők neveit*/

insert into employee (name, age, salary, position)
values ('Jolán', 65, 100000, 'nyugdijas'); 

/*
 * insert "commit köteles" utasitás
 * 
 * */

/*
 * lock mechanizmus történhet akkor, amikor adatbázis módositő
 *utasitást adok ki
 */


/* tranzakció
 * 
 * az adatbázis művelet lezárása:
 * 
 * commit - OK, sikeres lezárás, a váégrehajtott utasitás megtörténhet úgy, ahogy 
 * végrehajtottuk
 * 
 * rollback - Cancel, vissza vonom lezáratlan adatbázis utasitást
 */

/*delete - törlés*/

delete from employee;

truncate table employee;

/* update - módositás*/

update employee set name='Gizi', age=70;

/*
 * webes ökoszitémában az adatbázis
 * insert, select, update , delete
 * create, read, update, delete -> CRUD műveletek
 * */

/* DML - Data Manupulation Language
 * 
 * insert 
 * update 
 * delete
 * lock
 * 
 * */

/*
 * DQL - Data Query Language
 * 
 * select
 * */


/*
 * DCL - Data Control Language
 * 
 * Grant
 * Revoke
 * */