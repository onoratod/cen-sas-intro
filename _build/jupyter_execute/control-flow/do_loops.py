# DO Loops

`DO` loops can be used to execute a set of code over a series of items. These can be used in both `DATA` steps and open code inside of a `%macro`, however, we tend to use them most often in open code. 

The basic `DO` loop syntax is

```sas
do i = /* start */ to /* end */ (by /* by value */);
    /* SAS statements */
end;
```

The default value of the counter is 1 but you can modify this with the `by` option. Also, the index value `i` can be called whatever you want (i.e. `opportunity` would also work). This is similar to a `forval` loop in Stata.

```sas
data out.A;
    do i = 1 to 5;
        y = i*2;
        output;
    end;
run;
```

import pandas as pd

example = pd.read_sas("../data/a.sas7bdat", encoding="latin-1");
example.head(n=50)

```sas
data out.A;
    do i = 1 to 100 by 20;
        y = i*2;
        output;
    end;
run;
```

example = pd.read_sas("../data/a_by.sas7bdat", encoding="latin-1");
example.head(n=50)

Or in open code

```sas
%macro doloop;
    %do i = 1 %to 5;
        %put &i;
    %end;
%mend doloop;

%doloop;
```

```
686  %doloop;
1
2
3
4
5
```

```sas
%macro doloop;
    %do i = 1 %to 100 %by 20;
        %put &i;
    %end;
%mend doloop;

%doloop;
```

```
699  %doloop;
1
21
41
61
81
```


## DO-WHILE Loop

Sometimes it is useful to execute a set of commands while a condition is true. In these cases, we can use a `DO-WHILE` loop. 

```sas
do while (cond);
    /* SAS statements */
end;
```

The condition is evaluated at the top of the loop before statements in the `DO` loop are executed. This can be used in `DATA` steps or open code in a `%macro`. For the remainder of this page, we will only show examples in open code but syntax is very similar for `DATA` step. 
        

````{margin}
```{note}
Again we use `%sysfunc` to call the `sum` function to increment our counter.
```
````


```sas
%macro dowhile(end);
    %let i = 1;
    %do %while(&i < &end);
        %put &i;
        %let i = %sysfunc(sum(&i, 1));
    %end;
%mend dowhile;

%dowhile(2);
%dowhile(5);
```

```
762  %dowhile(2);
1
763  %dowhile(5);
1
2
3
4
```

## Iterate Over a List with DO Loop

If we want to execute some code over a list of values then we need to be a little clever. To do this, we're going to use a few helpful SAS functions. The code to loop over a list of items is below. The basic idea is we use a `DO-WHILE` loop to iteratively retrieve each element of our list until we reach the end of the list.

```{code-block} sas
---
lineno-start: 1
---
%macro listloop(list);

    %let i = 1;
    
    %do %while (%scan(&list, &i, " ") ~= );
        * Get the value in the ith spot;
        %let value = %scan(&list, &i, " ");
        
        * Print to log;
        %if %length(&value) ~= 0 %then %put &value;
        
        *Increment counter;
        %let i = %eval(&i + 1);
        
    %end;
    
%mend listloop;
```
Let's discuss the helper functions we use in this code block. The first new function here is `%scan(list, i, delim)` which returns the `i`th item in the specified `list` that is delimited by `delim` (specifying the delimiter is optional). We use this in line `5` and `7` 

```{code-block} sas
---
lineno-start: 1
emphasize-lines: 5, 7
---
%macro listloop(list);

    %let i = 1;
    
    %do %while (%scan(&list, &i, " ") ~= );
        * Get the value in the ith spot;
        %let value = %scan(&list, &i, " ");
        
        * Print to log;
        %if %length(&value) ~= 0 %then %put &value;
        
        *Increment counter;
        %let i = %eval(&i + 1);
        
    %end;
    
%mend listloop;
```

We use `%scan` to parse through the elements of the list we are trying to loop over. We use this with a `DO-WHILE` loop to continue scanning elements from our list until the element we scan is empty i.e. we reached the end of the list. We use `%scan` again in line `7` to retrieve the ith element in our list. 

Another new function we use is `%length` which returns the length of the given argument. We use this in line `10`

```{code-block} sas
---
lineno-start: 1
emphasize-lines: 0,10
---
%macro listloop(list);

    %let i = 1;
    
    %do %while (%scan(&list, &i, " ") ~= );
        * Get the value in the ith spot;
        %let value = %scan(&list, &i, " ");
        
        * Print to log;
        %if %length(&value) ~= 0 %then %put &value;
        
        *Increment counter;
        %let i = %eval(&i + 1);
        
    %end;
    
%mend listloop;
```

Here we use `%length` to check that the element we retrieved from our list is not empty i.e. has non-zero length. This is overkill since we already checked in line `5` that the element is not empty. 

The last new function we use here is `%eval` which allows us to evaluate expressions in open code. We use this in line `13`

```{code-block} sas
---
lineno-start: 1
emphasize-lines: 0, 13
---
%macro listloop(list);

    %let i = 1;
    
    %do %while (%scan(&list, &i, " ") ~= );
        * Get the value in the ith spot;
        %let value = %scan(&list, &i, " ");
        
        * Print to log;
        %if %length(&value) ~= 0 %then %put &value;
        
        *Increment counter;
        %let i = %eval(&i + 1);
        
    %end;
    
%mend listloop;
```

We use `%eval` to increment our counter. Recall that in a previous section we used `%sysfunc` combined with `sum` to increment our counter. 


