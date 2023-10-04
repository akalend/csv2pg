# csv2pg
Python utility read csv file and  create postgres table 

This utility transform field mane to lower and change ' ' to '_'.

**Example**
```
'Produrt Name' => product_name
'Product_key'  => product_key
```

Field types are only : 
 - text
 -  bigint
 -  double

**usage**
```
./scv2pg <fileName> [<tablename>]
```
