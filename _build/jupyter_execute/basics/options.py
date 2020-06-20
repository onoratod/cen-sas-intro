# The OPTIONS Statement

The first line of each SAS program should be the `OPTIONS` statement. This tells SAS how to run the processing of your program (i.e. how statements are printed to the log, how the program utilizes server resources, etc.)

```sas
options debug='CONNECT=00200000' mlogic mprint replace errorabend obs=max threads cpucount=actual;
```

This line, among other things, tells SAS that it is OK to replace existing datasets (`replace`), that macro code (discussed below) should be printed to the log (`mlogic` and `mprint`), that SAS should use multi-threaded processing if available (`threads`), that it should use as many CPU cores
as are made available to the process (`cpucount`), and that SAS should terminate and set `OBS=0` when it hits an error (`errorabend`).

You can find a list of SAS options [here](https://documentation.sas.com/?docsetId=lesysoptsref&docsetTarget=p1tmgku1vq7pwqn1iqioeflxgec1.htm&docsetVersion=9.4&locale=en).

```{tip}
Given that our code can take several hours or days to run, we often want to be sure that our code will work and produce what we want. To do this we can set `OBS=0` or `OBS=N` to read in the first `N` observations of each dataset. This allows the code to run incredibly fast, which allows us to address syntax errors and confirm the final data includes everything we want among other things. If you are merging datasets in your code, the final dataset may appear empty because it is unlikely that the first `N` observations have the same merge keys between the two datasets. 
```

