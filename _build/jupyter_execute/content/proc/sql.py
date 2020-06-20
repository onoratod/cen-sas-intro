# Merging Data with PROC SQL

`PROC SQL` is the most useful and versatile SAS procedure. When you use `PROC SQL`, SAS can leverage some of the efficiencies of SQL processing, which can improve the processing time of your queries. The flexibility and specificity of SAS SQL statements are often preferable to the SAS provided alternatives. 

`PROC SQL` steps are generally of the form:

```sas
proc sql; 
    (create table NEW_TABLE as)
        select VARIABLES
        from SOURCES 
        (group by KEYS)
        (order by KEYS)
        (where);
quit;
```

The statements contained in parentheses are optional. When you write your `PROC SQL` statements, do not include the parentheses. If you omit the `create table` line, the result of you `PROC SQL` step will be written to the log but no data will be written to the disk. The optional `group by` and `order by` lines instruct SAS to collapse the data to a single row by the specified keys and sort the data by the specified keys, respectively. 

## Merging data in SAS using `PROC SQL` `JOINS`

Generally for our purposes, when we want to merge together two datasets in SAS we use `JOIN` commands in a `PROC SQL` step. All SQL joins are akin to many-to-many joins implemented by the `joinby` function in Stata &mdash; these joins are not on their face equivalent to `1:1`, `1:m`, or `m:1` joins unless you ensure that the tables you are joining are unique on the join variables yourself.

Conceptually, SQL joins involve a "left" table and one or more "right" tables to be joined. All joins are *Cartesian products* made on the the specified merge key variables. This means if there are two duplicate matching keys in the left table and two duplicate matching keys in the right table, there will be four duplicate keys in the output dataset. Another way to phrase this is that each observation is assigned all of the rows that it matches to. 

The most common join we use is the `LEFT JOIN` but all types are outlined below

### LEFT JOIN

![image](left_join.png "LEFT JOIN")

A `LEFT JOIN` selects all the obervations in the left table regardless of their key values but only selects observations with matching key values from the right table. Variables from the right table in rows where there is no match are assigned missing values. A `LEFT JOIN` is **not** commutative (i.e. reversing the order of the data sets can produce different results).

#### Example

In this example, we merge on `state` from `out.kid_geos` using a `LEFT JOIN` onto `in.fake_micro` and save the resulting dataset in `out.left_join_example`. 

Here, we use the `select` statement to only keep certain variables from each dataset, labeled `A` or `B`. These labels are assignedbelow in the `from` and `left join` statements.

The merge key here is `pik` and we require that `pik` is not null for the left table (`A`).

```sas

proc sql; 
    create table out.fake_micro_with_geo as
        select A.pik, A.mom_pik, A.dad_pik, B.state
            from out.fake_micro as A
            left join out.kid_geos as B
                on A.pik = B.pik and A.pik is not null;
quit;

```

The output data set `out.left_join_example` is:

```{margin} Note
The rows with missing `state` are rows that did not match to the right data set, they remain in the output data set but are assigned missing values of `state`.
```

import pandas as pd

df = pd.read_sas("../data/left_join_example.sas7bdat", encoding="latin-1");
df.head(n=10)

### RIGHT JOIN

![image](right_join.png "RIGHT JOIN")

A `RIGHT JOIN` selects all the observations in the right table. When observations do not match to the left table the key values are set to missing. A `RIGHT JOIN`, like a `LEFT JOIN`, is not commutative and is **not** the same as reversing the datasets in a `LEFT JOIN`.

#### Example

In the example below, we have the same setup as in the `LEFT JOIN` example, except that we use a `RIGHT JOIN`. 

**Note:** `out.kid_geos` is a subset of `out.fake_micro` so `pik` will never be missing in the output data set since all the keys in `out.kid_geos` appear in `out.fake_micro`.

```sas
proc sql; 
    create table out.fake_micro_with_geo as
        select A.pik, A.mom_pik, A.dad_pik, B.state
            from out.fake_micro as A
            right join out.kid_geos as B
                on A.pik = B.pik and B.pik is not null;
quit;

```

```{margin} Note 
Unlike in the example above, `state` is never missing because the `RIGHT JOIN` restricts to observations that appear in `out.kid_geos`, where `state` is never missing. Note that `pik = 005` and `pik = 006` are missing now (see the `LEFT JOIN` output), this is because they do not appear in `out.kid_geos`.
```

df = pd.read_sas("../data/right_join_example.sas7bdat", encoding="latin-1");
df.head(n=10)

### INNER JOIN

![image](inner_join.png "INNER JOIN")

An `INNER JOIN` selects all the observations that have keys in **both** the left and the right data set. 
An `INNER JOIN` is a logical AND between the two tables. Unlike a `RIGHT JOIN` or a `LEFT JOIN`, an `INNER JOIN` is commutative 
so tables can be joined in either order. 

#### Example

In the example below, we have the same setup as in the previous examples, except that we use an `INNER JOIN`. 

```sas
proc sql; 
    create table out.fake_micro_with_geo as
        select A.pik, A.mom_pik, A.dad_pik, B.state
            from out.fake_micro as A
            inner join out.kid_geos as B
                on A.pik = B.pik and B.pik is not null;
quit;

```

df = pd.read_sas("../data/inner_join_example.sas7bdat", encoding="latin-1");
df.head(n=10)

### FULL JOIN

![image](full_join.png "FULL JOIN")

A `FULL JOIN` selects all observations from both datasets and sets missing key values for observations that only appear in the right dataset.
A `FULL JOIN` is the logical OR between two datasets, but unlike an `INNER JOIN` it is not commutative because missing key values are 
set based on the right dataset. We illustrate this below. 

#### Example

In the example below, we have the same setup as in the previous examples, except that we use a `FULL JOIN` with `out.kid_geos` as the right dataset.

```sas
proc sql; 
    create table out.fake_micro_with_geo as
        select A.pik, A.mom_pik, A.dad_pik, B.state
            from out.fake_micro as A
            inner join out.kid_geos as B
                on A.pik = B.pik and B.pik is not null;
quit;

```

```{margin} Note 
`out.kid_geos` is a subset of `out.fake_micro` so there will never be missing keys (`pik`). A `FULL JOIN` where the right dataset is a subset of the left dataset is equivalent to a `LEFT JOIN`. 
```

df = pd.read_sas("../data/full_join_example.sas7bdat", encoding="latin-1");
df.head(n=10)

#### Reverse Example

Now lets reverse the datasets to illustrate why a `FULL JOIN` is not commutative. 

```sas
proc sql; 
    create table out.full_join_example as
        select A.pik, A.state, B.mom_pik, B.dad_pik
            from out.kid_geos as A
            full join out.fake_micro  as B
                on A.pik = B.pik and A.pik is not null;
quit;

```

```{margin} Note 
We can see that observations 4 and 5 are missing keys (`pik`) because these observations appear in `out.fake_micro` but do not appear in `out.kid_geos`. These are the same observations that are missing `state` above.
```

df = pd.read_sas("../data/full_join_example_reverse.sas7bdat", encoding="latin-1");
df.head(n=10)

#### References

[This](https://support.sas.com/resources/papers/proceedings/proceedings/sugi25/25/cc/25p109.pdf) file was referenced when creating this page. 

