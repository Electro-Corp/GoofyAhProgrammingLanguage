# GoofyAhProgrammingLanguage
Goofy ahhhhhhhh <br>
Table of Contents:
> Users Guide


## Users Guide

### Basic
Each program must have the two following sections: <br>
* data
* entry
<br>
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
<br>
### Supported Built In functions
<br>
As of now, there are four built in functions:
* add
* sub
* out
* push
<br>
