# Setting Variable Lengths

In SAS, variables have different lengths. Numeric variables have lengths between 3 and 8 (depending on the size of the number). A character variables length is equivelent to the length of the string (i.e. `"Philadelphia"` would have length 12). SAS automatically sets the length of numeric and character variables to 8. This can sometimes be wasteful and we can save space by carefully setting the lengths of our variables. However, we need to be careful not to set the lengths too short so that we lose information. The SAS guide also warns against shortening variables with fraction values which may result in a loss of precision. You can find a chart of variable lengths and their corresponding numeric ranges [here](https://documentation.sas.com/?docsetId=hostunx&docsetTarget=p12zsdbylnn6c2n1i48z7djr6uzo.htm&docsetVersion=9.4&locale=en). 

You can set the length of a variable with a `LENGTH` statement in the `DATA` step. For numeric variables

```sas
data out.outfile;
    set in.infile;
    
    length married 3;
    
    married = 1;
    
run;
```

For character variables the length is preceded by `$`

```sas
data out.outfile;
    set in.infile;
    
    length tract $6;
    
    tract = "123456";
    
run;
```

You can set the lengths for a list of variables by listing the variable names and then listing the length. This sets the length of `wages`, `income`, and `dividends` to 8

```sas
data out.outfile;
    set in.infile;
    
    length wages income dividends 8 tract $6;
run;
```


