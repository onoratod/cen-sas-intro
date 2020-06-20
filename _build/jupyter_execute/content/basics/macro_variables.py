# Macro Variables 

Generally, the final component of a program header are the program-specific macro variables. SAS macro variables allow you to modify the text in a SAS program through symbolic substitution (think `local` and `global` from Stata). SAS macro variables are declared by a `%LET` statement followed by the macro name, an equals sign, and finally the value to be stored in the macro. You can store anything in a SAS macro. 

```sas
%let fcohort = 1978;
%let lcohort = 1991;
%let file_name = example.txt;
```

To refer to a previously declared SAS macro variable, you type the macro name (i.e. fcohort) contained by `&` and `.`. For example, to keep rows of data for kids born between 1978-1991 using the macro variables above, we would write:

```sas
if cohort >= &fcohort. and cohort <= &lcohort.;
```

## A note on the use of `&` and `.` with Macros and Nested Macros

Here we discuss macro processing in more detail, you should skip this portion for now and come back when useful. In general, there is no need to include the `.` delimiter at the end of the macro name when envoking a SAS macro variable - the `&` will suffice. For example, the sample code above will work without the periods: 

```sas
if cohort >= &fcohort and cohort <= &lcohort;
```

There are times, however, when the `.` is required to delimit the end of a macro variable, so it is good practice to include them. For example, when using macro variables nested within text or code, the `.` is needed to signify the end of the macro variable. This is illustrated below:

````{margin}
```{tip}
The `%PUT` command acts like a `print` (Python) or `display` (Stata) statement, displaying the following text in the SAS log. This can be a useful tool for debugging.
```
````

First we define our macro `suffix`

```sas
%let suffix = ing;
```

The safe way to invoke this macro is 

```sas
* This is the safe way;
%PUT swimm&suffix.;
```

which would output

```
57   * This is the safe way;
58   %PUT swimm&suffix.;
swimming
```

However, in this case we can omit the `.` and get the same result

```sas
* This gives the same result;
%PUT swimm&suffix;
```

which gives 

```
60   * This gives the same result;
61   %PUT swimm&suffix;
swimming
```

If there were characters following the macro that are not part of the macro then omitting the `.` character would cause an error as below where SAS looks for the macro named `suffixly`

```sas
* This will not work, SAS looks for macro "suffixly";
%PUT swimm&suffixly;
```
```
63   * This will not work, SAS looks for macro "suffixly";
WARNING: Apparent symbolic reference SUFFIXLY not resolved.
64   %PUT swimm&suffixly;
swimm&suffixly
```

Adding the `.` to denote the end of the macro fixes this 

```sas
* This works, SAS knows macro is suffix;
%PUT swimm&suffix.ly;
```

```
66   * This works, SAS knows macro is suffix;
67   %PUT swimm&suffix.ly;
swimmingly
```

You can see how SAS interprets the different macro variables we defined in the code above. The `%PUT` statement acts like a print statement here and the output can be seen under lines 61, 64, and 67.

### Nested Macros

We can also nest macro variables inside of each other, although things become a bit more complicated here. If you want to understand how SAS will resolve these macros you need to understand the rules of SAS macro variables

1. Never talk about SAS macro variables
2. Two ampersands always resolve to one ampersand. 
3. The macro parser always continues reading left to right until the end of the reference is reached.
4. If a reference contains consecutive ampersands, after resolution at least one more read will follow.

To illustrate these rules lets consider a few examples. First lets define some macro variables

```sas
%let year = 99;
%let century = 19;
%let cpi1999 = 1.05;
```

Think about how the macro parser will treat

```sas
%PUT &cpi&century&year;
```

First it will try to resolve `&cpi`, however this doesn't exist so it will leave it as is. Then it will resolve `&century` to `19` and `&year` to `99` which results in `&cpi1999` since there were no consecutive ampersands the macro processor terminates. 

```
WARNING: Apparent symbolic reference CPI not resolved.
74   %PUT &cpi&century&year;
&cpi1999
```

What if we use two ampersands in the beginning 

```sas
%PUT &&cpi&century&year;
```

First the macro parser resolves `&&` to `&` then it tries to resolve `&century` followed by `&year` resulting in `&cpi1999`. Since we had consecutive ampersands the macro parser does one more read and resolves `&cpi1999` to `1.05`

```
90   %PUT &&cpi&century&year;
1.05
```

Now let's try something a little more complicated


```sas
%let pre = cpi
%let suf = year
%let cpiyear = 1999
%let cpi1999 = 1.07
```

Let's try to invoke `cpi1999` using `pre`, `suf`, and `cpiyear`. Let's start from the final line we want

```sas
%PUT &cpi1999;
```

Now we want `&cpiyear` to resolve to `1999` and we want a singular ampersand in the front. So we sub `&cpiyear` for `1999` and `&&` for `&` (because two ampersands resolve to one)

```sas
%PUT &&cpi&cpiyear;
```

Now we need to sub in `&pre` for `cpi` and `&suf` for `year`

```sas
%PUT &&cpi&&pre&suf;
```

However, this will not work and will resolve to `&cpi&preyear`. This is because we forgot to deal with `&&` and `&`. To retain `&&` we should use `&&&&` and to retain `&` we should use `&&` which gives

```sas
%PUT &&&&cpi&&&pre&suf;
```

which gives

```sas
54 %PUT &&&&cpi&&&pre&suf;
1.07
55
```

Let's step through this. In the first pass, the macro parser first resolves `&&&&cpi` to `&&cpi`, then `&&` to `&`, then `&pre` to `cpi`, then `&suf` to `year` giving `&&cpi&cpiyear`. On the second pass, it resolves `&&cpi` to `&cpi` and `&cpiyear` to `1999` giving `&cpi1999`. Finally, since there was a double ampersand, the macro parser does one final pass and resolves `&cpi1999` to `1.07`. 

This example was needlessly complicated to illustrate some of the macro parser rules. You will rarely have to use something this complicated but it may come in handy at some point. 

### References

Referenced [this](https://support.sas.com/resources/papers/proceedings/proceedings/sugi29/063-29.pdf) source for this page.

