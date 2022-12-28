# GoofyAhProgrammingLanguage
Goofy ahhhhhhhh <br>
Table of Contents:
> Users Guide
> Reccomended appplication structure 
## IMPORTANT LINKS:
Guide for the standard library: https://github.com/Electro-Corp/GoofyAhProgrammingLanguage/blob/main/stdlib/README.md#stdlib
## Users Guide
### Run a program
`python3 main.py [FILE].gapl` 
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
* lfile
* wfile
* lchar
* lspecInd
#### `push`
Pushes an item to the stack
#### `add`/`sum`
To add, push two ints to the stack and then run `add` or `sub`. The result will be pushed to the output stack.
#### `out`
Prints the last item in the output stack
#### `los`
Sets a var to the last item on the output stack. Ex:
```
let g 0
push 3
push 4
add
// g will be 7
los g
```
#### `cmp`
Compares last two items on the stack. If they are equal, the condition bit is set to 1. Otherwise it is set to 0.
#### `jcb`
This will jump to the specified line if the condition bit is 1. Ex:
```
// jumps to line 15 is compare bit is 1
jcb 15
```
#### `goto`
Goes to the specified line. Ex:
```
goto 15
```
#### `lchar`
Loads a char to the charstack. Ex:
```
lchar hello!
```
#### `lspecInd`
Pushes the char array at the specific index offset from the top provided (length - indexProvided) to the front of the char stack (note that the original is not removed) Ex:
```
lchar Hey
lchar WhoAsked?
lspecInd 2 
// Hey is now at the front at the back of the char stack
```
### NOTE: FOR FILES ITS RECOMMENDED TO USE THE STDLIB/FILEIO.GAPL for convenience
#### `lfile`
Loads a file based on the last item on the charstack, with the specified mode. Ex:
```
lchar helloworld.txt
lfile a
```
Modes:
* a = Append
* w = Write
* r = Read
#### `wfile`
Appends to the current loaded file with the last item on the charstack. Ex:
```
lchar helloworld.txt
lfile w
lchar Hey!
wfile
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
## Reccomended appplication structure 
It is recommended to make programs like so:
--- mainFile.gapl
   --- functionFile1.gapl
      --- subFunction1.gapl
   --- functionFile2.gapl
      --- subFunction2.gapl
      --- subFunction3.gapl
          --- subsubFunction1.gapl
Only one file may have the `data` and `entry` namespace. All other files must be a function file. Any imports the functions may have must be imported in the main file.
