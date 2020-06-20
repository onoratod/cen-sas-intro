# Putting It All Together

Adding together the components we discussed in this section, here is an example of a SAS program header. It's helpful to add a comment at the very top with a quick description (at the very least) of what the file does. 

```sas
/***
intergen_start.sas
Build intergenerational data
Created By: Census Predoc #1 (2017-02-02)
***/

options debug='CONNECT=00200000' mlogic mprint replace errorabend obs=max threads cpucount=actual;

* Filepaths;
libname databank "/XX/databank/dropoff";
libname dump "/XX/intergen/dump";
libname out "/XX/intergen/micro";

* Useful SAS macros;
%include "/XX/leap_macros.sas";

/*---------------------------------------------------------------
Useful macros
---------------------------------------------------------------*/

%let fcohort = 1978;
%let lcohort = 1991;

*CPI factors; 
%include "/XX/intergen/code/modules/cpi.sas";
```

