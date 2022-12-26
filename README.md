# GoofyAhProgrammingLanguage
Goofy ahhhhhhhh <br>
Table of Contents:
> Users Guide
## Users Guide
### Basic
The data segment is reserved for declearing variables or pushing constants to the stack. <br>
The entry area is for the main exceution of the program. <br>
Each program must have the two following sections: 
* data
* entry 
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
* add
* sub
* out
* push 
* los
* cmp
* jcb
* goto 
#### Push
Pushes an item to the stack
#### Add/Sum
To add, push two ints to the stack and then run `add` or `sub`. The result will be pushed to the output stack.
#### Out
Prints the last item in the output stack
#### Los
Sets a var to the last item on the output stack. Ex:
```
let g 0
push 3
push 4
add
// g will be 7
los g
```
#### CMP
Compares last two items on the stack. If they are equal, the condition bit is set to 1. Otherwise it is set to 0.
#### JCB 
This will jump to the specified line if the condition bit is 1. Ex:
```
// jumps to line 15 is compare bit is 1
jcb 15
```
#### Goto
Goes to the specified line. Ex:
```
goto 15
```
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
