# SAS Macros

A SAS `%macro` is a discrete piece of code that can be accessed throughout the SAS script by keyword reference. A SAS `%macro` can take and use arguments. A SAS `%macro` is useful when you need to execute a similar set of tasks over and over again (for instance, over many years). This is similar to a `program` or `ado` in Stata or `functions` in R and Python. The general syntax is:

```sas
%macro name(/* Arguments go here */);

    /* SAS code goes here */
    
%mend name;
```

A SAS `%macro` is referenced elsewhere in a SAS script as `%name(...)`. You can think of a SAS `%macro` as inserting the contained text/statements into the SAS script whenever referenced.

## Arguments

A SAS `%macro` has two types of arguments (or none at all): positional and keyword. Keyword arguments are specified with a keyword, equals sign and a default value (which can be null) 

```sas
%macro name(keyward_arg = 1); 
%mend name;
```

or with a null default value 

```sas
%macro name(keyword_arg = );
%mend name;
````

To supply a custom value of `10` we we would would write 

```sas
%name(keyword_arg = 10);
```

Positional arguments are just listed and are assigned the value corresponding to their position in the argument list when the macro is defined: 

```sas
%macro name(a, b, c);
%mend name;
```

If I called `%name(1, 2, 3)` then `a = 1, b = 2, c = 3`. If no argument is specified in the corresponding position then the positional argument resolves to null. 

Arguments are referenced inside of a `%macro` as macro variables. These concepts are illustrated below. 

```sas
%macro hello_world;

    %PUT Hello World!;
    
%mend hello_world;
```

```sas
%macro hello_place(place);

    %PUT Hello &place.!;
    
%mend hello_place;
```

```sas
%macro hello_there(place, name = John);

    %PUT Hello &place., my name is &name.!;
    
%mend hello_there;
```

```sas
%hello_world;
%hello_place(USA);
%hello_there(USA);
%hello_there();
%hello_there(USA, name = Danny);
```

These macro calls output

```sas
324  %hello_world;
Hello World!
325  %hello_place(USA);
Hello USA!
326  %hello_there(USA);
Hello USA, my name is John!
327  %hello_there();
Hello , my name is John!
328  %hello_there(USA, name = Danny);
Hello USA, my name is Danny!
```



## Example

To motivate the use of `%macro` functions, suppose you needed to load in two years of data and generate a few variables. You could do something like:

```sas
data out.intergen_1999_clean;
    set in.intergen_1999;
        
        year = 1999;
        par_inc = mom_inc + dad_inc;
run;

data out.intergen_2000_clean;
    set in.intergen_2000;
        
        year = 2000;
        gen par_inc = mom_inc + dad_inc;
run;
```

However, you can also do this in a cleaner and more efficient way with a `%macro` function.

```sas
* Define our macro;
%macro clean_intergen(year);

    data intergen_&year._clean;
        set intergen_&year.;
        
            year = &year.;
            par_inc = mom_inc + dad+inc;
    run;
    
%mend clean_intergen;

* Call the macro on each year;
%clean_intergen(1999);
%clean_intergen(2000);
```

This style of coding is preferred as it keeps our scripts concise, generally reduces errors and makes debugging easier. 

