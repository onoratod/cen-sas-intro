# DATA Step Structure 

`DATA` steps are declared by the keyword `data` followed by an output dataset that SAS will write to. The output dataset may be a temporary file (no `libname`). In most applications, you will specify an input dataset using the `set` statement. This is the data SAS will read in, manipulate, and save to the output file. The `set` and `data` file can be the same file. You can also append multiple datasets together by listing multiple inputs to the `set` statement. To conclude the `data` step you use a `run` statement.

```sas
data library.out_filename;
    set library.in_filename;
        /* data step statements go here */
run;
```

