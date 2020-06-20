# Why SAS?

Writing code in SAS can be frustrating. It is likely not the type of statistical programming language you are accustomed to using. Programs like Stata and R store data in random access memory (RAM) — SAS operates on a single row of data at a time. This is what makes SAS useful for working with large datasets — you do not have to read the full file into memory. 

In Stata, you can use other parts of the data to inform "row-level" operations. For example, if you have a variable $x$ and you want to generate 

$$
z = x − \overline{x}
$$ 

you can use the `egen` function to attach $\overline{x}$ as a wide variable or simply summarize $x$ and difference out the mean using the stored macro. Conversely, SAS cannot compute the sample mean, $\overline{x}$, in a standard `DATA` step operation (more on this later) because it only has a single line of the data held in memory. A simple way to think about SAS is as a for-loop executing commands on each row of the data:

```stata
forval i = 1/_N {
    replace x = x + 1 if _n == `i'
}
```

The SAS programmer is required to write linear and purposeful code because of this "row-by-row functionality." This forces you to think through every operation you are asking SAS to perform. That is why SAS is like spinach. 

>It might not taste good, but “SAS is good for you” - Angrist.

