# Semicolons and Comments

## Semicolons

SAS uses `;` to delimit the end of a line of code (this is similar to Java and C languages). This means you need to include a `;` at the end of every line of code. This also means lines of code can span several lines (unlike Stata which requires a line break character `///`).

## Comments

SAS has two ways to create comments. You can start a comment with `*` and end it with `;` 

``` sas 
* This is a comment;
x = 10;
```

You can also create block comments with `/* */` 

``` sas
/* This is a 
   block comment */
x = 10;
```

Block comments can also be used inline

```sas 
data out.outfile(drop = x /* This is an inline comment */);
    set in.infile;
run;
```