# Exercise 

If you're up for it, test what we discussed about control flow in SAS to write a `%macro` that takes a `start_year`, an `end_year`, and a macro `name` and calls the specified macro for each year in between `start_year` and `end_year`. 

````{admonition} Solution
:class: dropdown, success

``` sas
    %macro exercise(start_year, end_year, name);
        
        %do year = &start_year %to &end_year;
            %&name.(&year.);
        %end;
        
    %mend exercise;
```
````

