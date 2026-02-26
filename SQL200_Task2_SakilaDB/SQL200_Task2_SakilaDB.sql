-- Q1 — Film prices
-- From film, show: film_id, title, rental_rate
-- Get only the films where rental_rate is 9.99 or 4.99.
SELECT film_id, title, rental_rate FROM film WHERE rental_rate=9.99 or rental_rate=4.99;	-- 336 rows affected




-- Q2 — Film length + rating
-- From film, show: title, length, rating
-- Find films that are 90 to 120 minutes (inclusive) and rating is PG or PG-13.

-- You can use these any one of these 3 versions of the queries (basic principle to advance)	---- 93 rows affected
SELECT fil.title, fil.length, fil.rating FROM film AS fil WHERE (fil.length>=90 and fil.length<=120) and (fil.rating='PG' or fil.rating='PG-13');
SELECT fil.title, fil.length, fil.rating FROM film AS fil WHERE (fil.length BETWEEN 90 and 120) and (fil.rating='PG' or fil.rating='PG-13')
SELECT fil.title, fil.length, fil.rating FROM film AS fil WHERE (fil.length BETWEEN 90 and 120) and (fil.rating IN ('PG','PG-13'))



-- Q3 — Actor last names
-- From actor, show: actor_id, first_name, last_name
-- Find actors whose last_name starts with S OR ends with N.
SELECT actor_id, first_name, last_name from actor where last_name LIKE 'S%' OR last_name LIKE '%N'	-- 50 rows affected



-- Q4 — Active customers + email filter
-- From customer, show: customer_id, first_name, last_name, email
-- Find active customers whose email contains “.org” OR “.net”.
SELECT customer_id, first_name, last_name, email FROM customer WHERE (activebool=True) and (email LIKE '%.org%' or email LIKE '%.net%'); 	-- 599 rows affected




-- Q5 — Inactive customers in store 1
-- From customer, show: customer_id, store_id, active
-- Find customers from store 1 who are not active.
SELECT customer_id, store_id, active FROM customer WHERE (activebool=False)  -- 0 rows affected (not constumer is inactive)



-- Q6 — Payment amount + date range
-- From payment, show: payment_id, customer_id, amount, payment_date
-- Find payments with amount between 2.00 and 5.00 and made in February 2007.
SELECT payment_id, customer_id, amount, payment_date
FROM payment
WHERE amount BETWEEN 2.00 AND 5.00
	-- payment_date feb 2007 === between 1 feb 2007 to less_than(1 march 2007) - because feb's last date can be 28 or 29
  AND payment_date >= '2007-02-01'
  AND payment_date < '2007-03-01';		-- 0 rows affected (there is no data which satisfies this condition)


-- Q7 — Rentals not returned
-- From rental, show: rental_id, rental_date, return_date, customer_id
-- Find rentals where return_date is NULL
SELECT rental_id, rental_date, return_date, customer_id FROM rental WHERE return_date=NULL;	-- there is no rental's data which has return_date is NULL



-- Q8 — Address district + postal code present
-- From address, show: address_id, address, district, postal_code
-- Find addresses where district is Texas or California AND postal_code is not NULL.
SELECT address_id, address, district, postal_code 
FROM address 
WHERE (district='Texas' or district='California') and (postal_code=NULL);	-- no data - 0 rows affected



-- Q9 — Replacement cost + exclude titles
-- From film, show: film_id, title, replacement_cost
-- Find films where replacement_cost is 12.99, 16.99, or 28.99
-- AND the title does NOT contain the letter A.
SELECT film_id, title, replacement_cost FROM film WHERE (replacement_cost=12.99 or replacement_cost=16.99 or replacement_cost=28.99) and (title NOT LIKE '%A%'); -- 29 rows affected




-- Q10 — Inventory logic challenge
-- From inventory, show: inventory_id, film_id, store_id
-- Find inventory items where:
-- • (store_id = 1 AND film_id between 1 and 50)
-- OR
-- • (store_id = 2 AND film_id between 51 and 100)
SELECT inventory_id, film_id, store_id FROM inventory WHERE (store_id = 1 AND film_id between 1 and 50) or (store_id = 2 AND film_id between 51 and 100);	-- 215 rows affected