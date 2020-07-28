-- use this to check which users have logged in.  use the comment field to clarify the session

show users;
select
    "name",
    "login_name",
    "created_on",
    "last_success_login",
    "expires_at_time"
from table(result_scan(last_query_id()))
where "comment" = '2020-09-28'
order by "name";