# The LIBNAME Statement

SAS requires that you specify the directories where SAS datasets should be saved and accessed from as LIBRARIES before you can use these directories. Every program you write will have at least one declared library. These should be listed at the top of you code beneath the `OPTIONS` statement. These are similar to filepath globals you might store at the top of your Stata `.do` files. 

Each `LIBNAME` statement assigns a short (1-8 characters) name to a directory, after which SAS datasets are accessed as `libname.file_name` in procedure and `DATA` steps. Libraries are **only** used for accessing data in SAS format (i.e. `.sas7bdat`).

```sas
libname databank "XX/databank/dropoff";
libname dump "XX/intergen/dump";
libname out "XX/intergen/micro";
```

