Unlike STATA, SAS programs are organized in STEPS. When you run a Stata program, a dataset is loaded into memory (RAM) and the data remains in memory between statements. In SAS, data is not retained in memory between steps -- each step loads data from disk, transforms the state of the data, and re-writes the file to disk. 

The most basic SAS step (and one of the ones you will use the most) is the `DATA` step -- `DATA` steps are the building blocks of all SAS programs. SAS is especially useful when manipulating large datasets in `DATA` steps because it never loads an entire dataset into RAM. Instead, SAS loads a single row of data at a time into RAM, looping over all rows in the dataset serially to complete the set of commands you provide. In general, `DATA` steps are designed to read in an input file `SET` by the user and output a transformed file. Once a line is read into RAM, variables are created, deleted, and manipulated, and the resulting row is saved to the bottom of the new file. It is essential to understand how SAS data steps are executed to interpret how seemingly identical sets of SAS statements can produce drastically different results. 

You can read more about `DATA` steps [here](https://documentation.sas.com/?docsetId=basess&S).


```{toctree}
:hidden:
:titlesonly:


structure.ipynb
example.ipynb
options.ipynb
```
