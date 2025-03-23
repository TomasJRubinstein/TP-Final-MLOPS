
  
    

  create  table "mlops"."source"."users__dbt_tmp"
  
  
    as
  
  (
    SELECT CAST(id as INT) as user_id,
       TO_TIMESTAMP("Active_Since", 'YY-MM-DD HH24:MI:SS') at time zone 'utc'as user_active_since,
                                                                        "Occupation" as user_occupation
FROM "mlops"."source"."users"
  );
  