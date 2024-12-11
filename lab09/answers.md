## SQL Questions

1. SELECT - Retrieving Data. Write a query to list the titles and release years of all movies in the film table.

SELECT title, release_year FROM film;

2. WHERE - Filtering Data. Write a query to find all customers whose last name starts with the letter 'S'.

SELECT \* FROM customer WHERE last_name LIKE 'S%';

3. ORDER BY - Sorting Results. List all films titles and their durations, sorted by their rental duration in descending order. If two films have the same rental duration, sort them alphabetically by title.

SELECT title, rental_duration
FROM film
ORDER BY rental_duration DESC, title ASC;

4. JOIN - Combining Tables. Write a query to list all films along with their categories. Show the film title and category name.

SELECT f.title, c.name AS category_name
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id;

5. AGGREGATE FUNCTIONS - Summarizing Data. Write a query to find the average rental duration for movies in each category.

SELECT c.name AS category_name, AVG(f.rental_duration) AS avg_rental_duration
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
GROUP BY c.name;

6. COUNT - Counting Rows. Write a query to count how many films are in the Action category.

SELECT COUNT(\*) AS action_films_count
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
WHERE c.name = 'Action';

7. INSERT - Adding Data. Insert a new customer into the customer table. The new customer should have a first name, last name, email, and be linked to an existing store.

INSERT INTO customer (first_name, last_name, email, store_id, create_date)
VALUES ('John', 'Doe', 'johndoe@example.com', 1, CURRENT_TIMESTAMP);

8. UPDATE - Modifying Data. Update the rental rate of all films in the Comedy category, increasing it by 10%.

UPDATE film
SET rental_rate = rental_rate \* 1.1
WHERE film_id IN (
SELECT f.film_id
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
WHERE c.name = 'Comedy'
);

9. DELETE - Removing Data. Write a query to delete all films that have never been rented. Make sure to use a subquery to identify the films that haven't been rented.

DELETE FROM film
WHERE film_id NOT IN (
SELECT DISTINCT inventory.film_id
FROM rental
JOIN inventory ON rental.inventory_id = inventory.inventory_id
);

10. CREATE TABLE & ALTER TABLE - Managing Database Structure. Create a new table called movie_reviews with columns for review_id, film_id, reviewer_name, rating, and comments. Then, add a foreign key constraint linking film_id to the film table.

CREATE TABLE movie_reviews (
review_id SERIAL PRIMARY KEY,
film_id INT NOT NULL,
reviewer_name VARCHAR(100),
rating INT CHECK (rating BETWEEN 1 AND 10),
comments TEXT
);

ALTER TABLE movie_reviews
ADD CONSTRAINT fk_film
FOREIGN KEY (film_id)
REFERENCES film (film_id)
ON DELETE CASCADE;

## SQLAlchemy Questions

1. Understanding SQLAlchemy Automap: How do you think the `AutoModels` class works to dynamically generate SQLAlchemy ORM models from the database schema?

The AutoModels class leverages SQLAlchemy's automap_base to dynamically generate ORM models from the database schema. It uses metadata reflection to inspect the database and automatically map tables to Python classes. The prepare method binds these mappings, enabling access to the tables as attributes of the AutoModels instance. This approach eliminates the need for manually defining models and is especially useful in scenarios where the database schema may change frequently or when interacting with legacy databases.

2. Async Database Operations: Explain the use of asynchronous database sessions in this script. Why does the script use AsyncSession instead of a regular Session, and how does this improve the efficiency of database operations?

Asynchronous database sessions, implemented using AsyncSession, allow the script to perform non-blocking database operations within an event loop. Unlike a regular Session, which blocks execution while waiting for database responses, AsyncSession enables other tasks to proceed concurrently. This improves efficiency, especially in applications that require high concurrency or perform many I/O-bound operations, as it reduces idle time and enhances overall responsiveness.

3. SQLAlchemy Query Construction: In the `model_examples` function, there is a query that selects all customers whose last names start with the letter "P". See if you can write another questy that selects customers whose first name ends with the letters "n" or "a" using SQLAlchemy syntax.

async with AsyncSession(engine) as session:
customers = await session.execute(
select(Customer).where(
Customer.first_name.like('%n') | Customer.first_name.like('%a')
)
)
for customer in customers.scalars().all():
print(customer.first_name)

4. In the `raw_sql_examples` function, there are two ways to execute SQL queries: directly via the engine using conn.execute() and using an ORM session with session.execute(). Discuss the pros and cons of executing raw SQL directly compared to using SQLAlchemy’s ORM methods.
   Hint: Consider the trade-offs in terms of readability, safety (e.g., SQL injection risks), and flexibility when using raw SQL versus ORM abstractions.

   Executing raw SQL directly via `conn.execute()` provides maximum flexibility and allows developers to utilize database-specific optimizations and advanced SQL features that might not be fully supported by the ORM. This approach is particularly beneficial for complex or performance-critical queries. However, it comes with significant drawbacks, including reduced code readability, increased risk of SQL injection vulnerabilities if parameters are not properly escaped, and tighter coupling to the database's SQL dialect, making the code less portable. In contrast, using SQLAlchemy's ORM methods via `session.execute()` offers better safety through parameterized queries and enhanced readability by abstracting SQL syntax into Pythonic operations. While the ORM may introduce slight overhead and limit access to some database-specific features, it simplifies complex relationships, encourages consistency, and makes the codebase more maintainable and secure, especially in large or collaborative projects.
