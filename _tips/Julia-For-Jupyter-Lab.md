---
layout: post
date: 2020-06-08
---

# Julia For Jupyter Lab

## Julia Installation

Julia can be easily installed on Windows/Linux by downloading the necessary package from the Julia website at [this link.](https://julialang.org/downloads/)

Once installed Julia we then need to make sure it is correctly added to the system PATH. If that's not the case, we just need to go to the directory where Julia is installed and then in the bin folder. Once copied this path, we just need to add it to the system environment variables.

In order to check if Julia has been added correctly to the PATH, we can then open a terminal and just type `julia`, this should then open the Julia shell.

## Jupyter Set-up

At this point we are ready to connect Julia to Jupyter Lab and Jupyter Notebook. This can be easily done by going to the terminal and typing the following lines:

```
using Pkg
Pkg.add("IJulia")
```

Now if we launch our Jupyter Lab as usual, we should automatically find between the different kernel options the possibility to start a Julia Kernel.

## Conclusion

Julia can alternatively also be installed on IDEs such as Atom or Visual Studio Code. On Atom this can be easily done by installing the [Juno extension.](http://docs.junolab.org/stable/man/installation/)
