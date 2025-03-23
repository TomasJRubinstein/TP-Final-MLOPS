SELECT CAST(user_id as INT),
       CAST(movie_id as INT),
       CAST(rating as INT)
FROM "mlops"."source"."scores"