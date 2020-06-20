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

Here we discuss macro processing in more detail, you should skip this portion for now and come back when useful. In general, there is no need to include the `.` delimiter at the end of the macro name when envoking a SAS macro variable - the `&` will suffice. For example the sampe code above will work without the periods: 

```sas
if cohort >= &fcohort and cohort <= &lcohort;
```

There are times, however, when the `.` is required to delimit the end of a macro variable so it is good practice to include them. For example, when using macro variables nested within text or code, the `.` is needed to signify the end of the macro variable. This is illustrated below:

**Note:** The `%PUT` command acts like a `print` (Python) or `display` (Stata) statement, displaying the following text in the SAS log. This can be a useful tool for debugging.

%let suffix = ing;

* This is the safe way;
%PUT swimm&suffix.;

* This gives the same result;
%PUT swimm&suffix;

* This will not work, SAS looks for macro "suffixly";
%PUT swimm&suffixly;

* This works, SAS knows macro is suffix;
%PUT swimm&suffix.ly;

It may be hard to understand the SAS log above, don't worry we will go over navigating SAS logs later. But above you can see how SAS interprets the different macro variables we defined in the code above. The `%PUT` statement acts like a print statement here and the output can be seen under lines 39, 42, 45, and 50. 

### Nested Macros

We can also nest macro variables inside of each other, although things become a bit more complicated here. The same principles apply as above, except that when you have more than one macro you need to tell SAS by beggining with the appropriate number of `&`s. This is illustrated below when we try to access macros storing inflation factors for different years. 

%let cpi1999 = 1.09;
%let cpi2000 = 1.02;
%let mean_cpi_1999_2000 = 1.05;

%let fyear = 1999;
%let lyear = 2000;

* Doesn't work if we just put one &, it interprets the second & as the end of the first macro variable
* and thinks CPI is a macro variable name;
%PUT &cpi&fyear;

* This does work however, because cpi1999 and cpi2000 are macro variable names;
%PUT &cpi1999&cpi2000;

* When we call two macro variables so we put two &s, note we don't need a period here;
%PUT &&cpi&fyear;

* Period also works though;
%PUT &&cpi&fyear.;

* When macros are embedded in text or code, we need the . to delimit the end;
%PUT &&mean_cpi_&fyear._&lyear.;