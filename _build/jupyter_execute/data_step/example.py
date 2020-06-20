# DATA Step Example 

In the below `DATA` step, we read in a file specified by the `set` statement, `in.fake_micro`, retaining only the first 100 observations `(obs = 100)` using a data step option (we will discuss these in more detail later). We then create several new variables, subset the data, and save the result to the output dataset, `in.fake_micro_10`. The `length` statement sets the length of the new variable `married` to 3 - the shortest numeric length. SAS automatically sets new numeric variables to length 8, the largest possible numeric length. This is wasteful and you can save space by carefully setting all the lengths of your variables to the minimum required to store the data you need (although be careful to not lose information here by setting the variable length to be too small).

We create a `married` indicator by evaluating whether or not another variable is equal to 1. We then restrict to rows with non-missing `mom_pik` or `dad_pik`. An `if` statement without a subsequent `then` statement drops any observations that do not meet that criteria specified by the `if` condition. 

Then we create two version of a parent income variable. `par_inc_2015_miss` will be missing if `mom_inc_2015` is missing or `dad_inc_2015` is missing or both. `par_inc_2012_nomiss` will never be missing, since the `sum()` function assigns missing arguments to zero. This is similar to the distinction between using `+` and `egen, rowtotal()` in Stata. 

The `keep` statement specifies which variables are to be kept and written to the output file. In SAS, `:` acts like a wildcard and is similar to the `*` in Stata, except it can only be used for variable name suffixes. Be mindful of this when naming variables. 

First let's look at the input data set. Note that missing values here are displayed as `NaN` because we use Python to display the data. In SAS missing values are displayed as `.` similar to Stata.

import pandas as pd

fake_micro = pd.read_sas("../data/fake_micro.sas7bdat", encoding="latin-1");
fake_micro.head(n=10)

```{admonition} Tip
:class: tip
The `~` is the logical not symbol in SAS, you may be familiar with `!` as the logical not (as in Stata, although you can use `~` in Stata as well).
```

```sas
* Set the directory where the data is; 
libname in "/media/sf_myfolders";

data in.fake_micro_10;
    set in.fake_micro(obs=100);
    
    * Set length of the marriage variable;
    length married 3; 
    
    * Create married indicator;
    married = kid_married_2015=1;
    
    * Restrict to kids with a mom_pik or dad_pik;
    if ~missing(mom_pik) or ~missing(dad_pik);
    
    * Combine parent income, this will be missing if either component is missing;
    par_inc_2015_miss = mom_inc_2000 + dad_inc_2000;
    
    * Combine parent_income, this will treat missing values as zero and will never be missing;
    par_inc_2015_nomiss = sum(mom_inc_2000, dad_inc_2000);
    
    keep pik mom_pik dad_pik par_inc_2015: ;
    
run; 
```

No we look at the output data set and we can see the difference between using `+` and `sum`. 

fake_micro = pd.read_sas("../data/fake_micro_10.sas7bdat", encoding="latin-1");
fake_micro.head(n=10)