# IF-THEN/ELSE Statements

`IF-THEN` and `IF-THEN/ELSE` statements are conditional statements in SAS that we can use to control the execution of our code. These can be used in a `DATA` step or in open code in a `%macro` with a `%` preceding the key words as illustrated below. 

In a `DATA` step

````{margin}
```{tip}
If you want to combine conditional statements in SAS, you can use `and` and `or` to represent logical AND and logical OR. You can also use `&` and `|` respectively, as in Stata. I prefer `and` and `or` because I feel they are more conversational and lead to more readable code.
```
````

```sas
data out.if_then_example;
    set out.fake_micro(keep = pik mom_pik dad_pik);
    
        * Identify parent status;
        if mom_pik ~= "" and dad_pik ~= "" then singleparent = 0;
        else singleparent = 1;  
run; 
```

import pandas as pd

example = pd.read_sas("../data/if_then_example.sas7bdat", encoding="latin-1");
example.head(n=50)

And in open code 

````{margin}
```{tip}
`%sysfunc` lets you evaluate `DATA` step functions in open code. Here we use it to call the SAS modul0 function `mod`
```
````

```sas
%macro ifthen(year);

    %if %sysfunc(mod(&year, 2)) = 0 %then %put Even.;
    %else %put Odd.;

%mend ifthen;

%ifthen(1);
%ifthen(2);
```
```
581  %ifthen(1);
Odd.
582  %ifthen(2);
Even.
```

## IF-THEN/ELSE DO Statements

Sometimes we want to execute a series of statements depending on a certain condition rather than just one statement. In these instances, we use `IF-THEN/ELSE DO` statements. The syntax for these statements in a `DATA` step is:
```sas
data out.output;
    set in.input;
    
    * IF-THEN DO;
    if (cond) then do;
        /* SAS statements if condition is met */
    end;
    
    * IF-THEN/ELSE DO;
    if (cond) then do;
        /* SAS statements if condition is met */
    end;
    else do;
        /* SAS statements if condition is not met */
    end;
run;
```

Or in open code (wrapped in a `%macro`)
```sas
* IF-THEN DO;
%macro ifthendo;
    %if (cond) %then %do;
        /* SAS statements if condition is met */
    %end;

    * IF-THEN/ELSE DO;
    %if (cond) %then %do;
        /* SAS statements if condition is met */
    %end;
    %else %do;
        /* SAS statements if condition is not met */
    %end;
%mend ifthendo;
```


