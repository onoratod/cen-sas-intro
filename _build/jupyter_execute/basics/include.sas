A usefule SAS functionality that we use in many of our programs is the `%include` statement. Generally, we include the `leap_macros.sas` program containing a TON of SAS macro programs written over the years (from back when the group was called LEAP, hence the name). This works very similar to the `include` statement in Stata.

```sas
%include "/XX/leap_macros.sas";
```