# Example SAS Script

Below we created a sample SAS script to illustrate some of the topics we covered so you can see how you might end up using them in a SAS script of your own. This creates a macro to clean some raw data, merge on some geographic variables, export the data as a `.dta`, and clean the working directory. It calls this macro for a set of years using a loop macro that loops over years using a do loop.

````{margin}
```{tip}
We use the `in` operator to check whether `yob` is between 1978 and 1983 inclusive.
```
````

```{code-block} sas
---
lineno-start: 1
---
/***
Prepare raw tax records for analysis
Created By: Census Predoc #2 (2017-02-02)
***/

options debug='CONNECT=00200000' mlogic mprint replace errorabend obs=max threads cpucount=actual;

* Filepaths;
libname raw "/XX/raw";
libname dump "/XX/analysis/dump";
libname geo "/XX/geos";

* Useful SAS macros;
%include "/XX/leap_macros.sas";

* Macro to clean data;
%macro prep_raw_data(year);
    
    * Clean the raw data, restrict to 1978 to 1983 cohorts;
    data dump.pre_&year.(keep = pik yob income geoid where = (yob in(1978:1983)));
        set raw.tax_records_&year.;
        
        length  yob 3
                wages 
                dividends
                agi
                income 8;
         
        income = sum(wages, dividends, agi);
    run;
    
    * Merge on geography;
    proc sql;
        create table dump.clean_&year. as
            select A.*, B.state,
                        B.county,
                        B.tract
                from dump.pre_&year. as A
                left join geo.geos_2010 as B
                    on A.geoid = B.geoid and A.geoid is not null;
    quit;
    
    * Convert to Stata dataset;
    proc export 
        data = dump.clean_&year. 
        outfile = "/XX/analysis/clean/clean_&year..dta" 
        replace;
    run;
    
    * Delete intermediate data;
    proc datasets lib = dump;
        delete clean_&year. pre_&year.;
    quit;
    
%mend prep_raw_data;

* Macro to loop over years;
%macro loop(start, end, name);
    %do i = &start. %to &end.;
        %&name.(&i.);
    %end;
%mend loop;

* Loop over years;
%loop(2000, 2015, prep_raw_data);
```
