# GoofyAhProgrammingLanguage
Goofy ahhhhhhhh <br>
Table of Contents:
> Users Guide
## Users Guide
### Basic
Each program must have the two following sections: 
* data
* entry
The data segment is reserved for declearing variables or pushing constants to the stack. <br>
The entry area is for the main exceution of the program. <br>
Example: <br>
```
data{
  // define two vars
  let x 1
  let y 1
  // push to the staack
  push x
  push y
}
entry{
  // add the two last items pushed to the stack
  add
}
```
### Supported Built In functions
As of now, there are four built in functions:
* add
* sub
* out
* push 
### Creating your own functions
To create your own function, create a seperate source file. Here it will be `stdlib.gapl`, a file part of the standard library.
To create a function, use the `func` syntax, like so: <br>
```
func puts{
  // code
}
```
To import the file in the main source, use `include`. Example:
```
include stdlib.gapl
```
