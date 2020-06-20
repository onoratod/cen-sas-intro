# DATA Step Options

`DATA` step options provide a set of tools to interact with input and output datasets. They are declared in parenthese after the filenames in `data` or `set` statements:

```sas
data library.out_filename ( /* data step options */ );
    set library.in_filename ( /* data step options */ );
        /* data step statements */;
run;
```

If a data set option follows the `set` statement, the options apply to the data being read in. If it follows the `data` statement, SAS applies the action to the output dataset. The general order of operations is:

1. SAS applies `data` step options specified in the `set` statement to the input data
2. SAS evaluates the programming statements in the `DATA` step
3. SAS applies `data` step options specified in the `data` statement to the output data

Last thing to keep in mind is that SAS always evaluates `keep`/`drop` options before `rename` options. This means you need to use the original variable names in the `keep`/`drop` options when using a `rename` option in the same statement.

## Important `DATA` Step Options

Below we summarize some of the most important data step options and give examples of their use. You can find a comprehensive list [here](https://documentation.sas.com/?docsetId=ledsoptsref&docsetTarget=p1mde8kd2by1sen1k3h2stj7kj69.htm&docsetVersion=3.1&locale=en).

### `KEEP` and `DROP` Options

The `keep` data step option allows us to only keep certain variables from the input or output dataset. Similarly, the `drop` data step option allows us to drop variables from the input or output dataset. 

To use the `keep`/`drop` options, write `keep = ` or `drop = ` followed by the list of variables you would like to keep or drop.

#### Example

Below we drop the `kid_married_2015` variable from the `in.fake_micro` dataset using the `drop` option. Then we create a `par_inc_2000` in the `data` step and only keep `pik`, `mom_pik`, `dad_pik`, and `par_inc_2000` in the `out.par_income` output dataset using the `keep` option. 


```sas
data out.par_income(keep = pik mom_pik dad_pik par_inc_2000);
    set in.fake_micro(drop = kid_married_2015); 
        par_inc_2000 = sum(mom_inc_2000, dad_inc_2000); 
run; 
```

Here is the `in.fake_micro` data:

import pandas as pd

df = pd.read_sas("../data/fake_micro.sas7bdat", encoding="latin-1");
df.head(n=10)

And the `out.par_income` dataset: 

df = pd.read_sas("../data/keep_example.sas7bdat", encoding="latin-1");
df.head(n=10)

### `RENAME` Option

The `rename` data step option allows us to change variable names from the input or output datasets. If you use `rename` in the `data` statement, the variable name is changed in the output data set. If you use `rename` in the `set` statement, the variable name is changed in the input data set and **the new name is used for all the subsequent `DATA` step commands.**

To use the `rename` option to rename `old_name` to `new_name` we would write `rename = (old_name = new_name)`.

Don't forget that the `rename` option is evaluated after `keep`/`drop` options!

#### Example

In the example below, we load in the `pik` variable from `in.fake_micro` and immediately rename it to `kid_pik` &mdash; this is the name that should be used in subsequent data step commands. Then we restrict the data set to rows where the last digit of `pik` is 4 using `substr` and an `if` statement (more on these later). Finally, we only keep the `kid_pik` variable and rename `kid_pik` to `pik`. Note that we reference `kid_pik` in the `keep` statement, this is because `keep` is evaluated before we rename `kid_pik` to `pik`.

```sas
data out.kid_piks(keep = kid_pik rename = (kid_pik = pik));
    set in.fake_micro(keep = pik rename = (pik = kid_pik));
    
        * Keep PIKs that end in a 4;
        if substr(kid_pik, 3, 1) = "4"; 
        
run; 
```

Here is the input data `in.fake_micro`:

df = pd.read_sas("../data/fake_micro.sas7bdat", encoding="latin-1");
df.head(n=10)

And the output data `out.kid_piks`:

df = pd.read_sas("../data/rename_example.sas7bdat", encoding="latin-1");
df.head(n=10)

### `WHERE` Option

The `where` option lets us select observations from the input or output data sets by applying conditions to the data. This is similar to using a `use if` in Stata:

```stata
use file_name if x > 100, clear 
```

To apply a condition using a `where` option we would write `where = (condition)`.

```{margin} Note
This could also be done with a `where` option in the `data` statement. In general,  selecting observations during input is more efficient than during output.
```


#### Example

Recall that in the example above we used an `if` statement to restrict to rows where `kid_pik` ended in a 4. We make the same restriction below using a `where` option in the `set` statement. 

```{note} 
The `where` option is evaluated after the `rename` statement, so we use the name `kid_pik` in the `where` option.
```




```sas
data out.kid_piks(keep = kid_pik rename = (kid_pik = pik));
    set in.fake_micro(keep = pik rename = (pik = kid_pik) where = (substr(kid_pik, 3, 1) = "4"));
run; 
```

Here is the input data `in.fake_micro`:

df = pd.read_sas("../data/fake_micro.sas7bdat", encoding="latin-1");
df.head(n=10)

Here is the output data `out.kid_piks`:

df = pd.read_sas("../data/where_example.sas7bdat", encoding="latin-1");
df.head(n=10)

