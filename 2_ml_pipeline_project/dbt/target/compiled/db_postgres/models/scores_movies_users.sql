SELECT *
FROM "mlops"."source"."scores" sc
INNER JOIN "mlops"."source"."movies" using(movie_id)
INNER JOIN "mlops"."source"."users" using(user_id)