# Deleting Data

Since SAS operates on a row-by-row basis, we often have to make several intermediate datasets in the process of creating a clean dataset for analysis. To keep our project space clean we want to delete these files at the end of our scripts. To do this, we make use of the `DELETE` statement of `PROC DATASETS`. 

## Deleting Files with PROC DATASETS

The general syntax to delete a file or list of files is

```sas 
proc datasets lib = (noprint);
    delete /* list files here */;
quit;
run;
```

`lib` specifies the library where the files are located. `noprint` (optional) supresses printing to the log. After the `delete` we specify the files we want to delete. Here is an example to delete the files `clean_data_pre` and `clean_data_merge` located in the `out` library

```sas
proc datasets lib = out;
    delete clean_data_pre clean_data_merge;
quit;
run;
```

We can also make use of the SAS wildcard character `:` to delete many files with a common prefix
    
````{margin}
```{note}
The wildcard character `:` only works for objects with a common prefix. So `pre_:` works but `pre_:_suffix` will not work.
```
````

```sas
proc datasets lib = out;
    delete clean_data_:;
quit;
run;
```

## Deleting All Files in a Library with KILL

Often times we use certain folders in our project space to store intermediate files that are byproducts of the build process (sometimes called `dump`). These folders can be filled with many files during a build process and it can be annoying to list them all out in the `DELETE` statement. In SAS we can delete all the files in a library using the `KILL` option to `PROC DATASETS`. For instance, to delete all the files in the library `out` we would write

```sas
proc datasets lib = out kill;
quit;
run;
```

We recommend using this sparingly to avoid accidently deleting important files. 

