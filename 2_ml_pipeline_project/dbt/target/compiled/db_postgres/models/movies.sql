SELECT CAST(id as INT) as movie_id,
       TO_DATE("Release_Date", 'YY-MM-DD') as release_date,
       "IMDB_URL" as imdb_url,
       CAST(CAST("Film_Noir" as INT)as BOOLEAN) as Film_Noir,
       CAST(CAST("War" as INT)as BOOLEAN) as War,
       CAST(CAST("Crime" as INT)as BOOLEAN) as Crime,
       CAST(CAST("Drama" as INT)as BOOLEAN) as Drama,
       CAST(CAST("Action" as INT)as BOOLEAN) as Action,
       CAST(CAST("Comedy" as INT)as BOOLEAN) as Comedy,
       CAST(CAST("Horror" as INT)as BOOLEAN) as Horror,
       CAST(CAST("Sci_Fi" as INT)as BOOLEAN) as Sci_Fi,
       CAST(CAST("Fantasy" as INT)as BOOLEAN) as Fantasy,
       CAST(CAST("Musical" as INT)as BOOLEAN) as Musical,
       CAST(CAST("Mystery" as INT)as BOOLEAN) as Mystery,
       CAST(CAST("Romance" as INT)as BOOLEAN) as Romance,
       CAST(CAST("Western" as INT)as BOOLEAN) as Western,
       CAST(CAST("Thriller" as INT)as BOOLEAN) as Thriller,
       CAST(CAST("Adventure" as INT)as BOOLEAN) as Adventure,
       CAST(CAST("Animation" as INT)as BOOLEAN) as Animation,
       CAST(CAST("Children_s" as INT)as BOOLEAN) as Children_s,
       CAST(CAST("Documentary" as INT)as BOOLEAN) as Documentary,
       CAST(CAST("unknown" as INT)as BOOLEAN) as unknown
FROM "mlops"."source"."movies"