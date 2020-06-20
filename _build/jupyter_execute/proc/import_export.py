# Importing and Exporting Data

In some cases we need to import external datasets, maybe a list of tracts or individual identifiers. We frequently export SAS datasets to Stata datasets since we mostly use SAS to clean and subset large datasets into more manageable datasets that we can analyze in Stata. 

## Importing Data with PROC IMPORT

To import datasets we use `PROC IMPORT`. The general syntax is below, optional arguments are placed in `()` 

```sas 
proc import 
    datafile = 
    out = 
    (dbms =)
    (delimiter = )
    (replace);
    getnames = ;
run;
```

### Description of Options

| :--- | :--- |
|   DATAFILE  | Specifies the complete path and filename    |
| OUT | Specifies the output SAS dataset in libname.filename format |
| DBMS | Specifies the type of data to import. One of csv (.csv, default delimiter is comma), dlm (.dat or .txt, default delimiter is blank), jmp (.jmp), or tab (.txt, default delimiter is tab) |
| DELIMITER | Specify the delimiter (i.e. ",", "&", "\|") |
| REPLACE | Replace output dataset if it already exists |
| GETNAMES | Generate variable names from first row |

### Example 

Below, we load in a comma-separated .txt file 

``` sas
libname out "/XX/output";

proc import datafile = "../data/proc_import_example.txt"
    out = out.proc_import_example
    dbms = csv
    replace;
    getnames = yes;
run;
```

Note that we can add SAS data step options to the `out` argument. For instance, if we only wanted to people over age 20 in our example

``` sas
libname out "/XX/output";

proc import datafile = "../data/proc_import_example.txt"
    out = out.proc_import_example (where = (age > 20))
    dbms = csv
    replace;
    getnames = yes;
run;
```
    

## Exporting Data with PROC EXPORT

To export SAS datasets to other formats we use `PROC EXPORT`. The general syntax is

```sas
proc export 
    data = 
    outfile = 
    (dbms = )
    (replace);
run;
```

### Description of Options

| :--- | :--- |
|   DATA  | The SAS dataset to export, specified as libname.filename |
| OUTFILE | Specifies the complete path and file name for the output file |
| DBMS | Specifies the type of data to export. |
| REPLACE | Replace output dataset if it already exists |

### Example

Below, we export a SAS dataset to a Stata dataset

```sas
libname raw "/XX/output";

proc export data = raw.clean_tax_records
    outfile = "/XX/clean/clean_tax_records.dta"
    replace;
run;
```

We can use SAS data step options in the `data` argument, like if we wanted to rename a variable

```sas
libname raw "/XX/output";

proc export data = raw.clean_tax_records(rename = (date_of_birth = dob))
    outfile = "/XX/clean/clean_tax_records.dta"
    replace;
run;
```



