import sys
import traceback
stack = []
outstack = []
vars = []
data = []
funcs = []
fprog = [[""]*50]*50
debug = False
g = -1
z = -3
def getVar(name):
  if(name in vars):
    return data[vars.index(name)]
  else:
    return None
def setVar(name, val):
  if(name in vars):
    data[vars.index(name)] = val 
def pFunc(file):
  global funcs
  global fprog
  global z
  global g
  with open(file, "r") as f:
    fdata = f.readlines()
  
  for i in range(len(fdata) - 1):
    #print(str(g)+","+str(z))
    #print(fprog)
    if('\n' in fdata[i]):
      z+= 1;
    if("{" in fdata[i]):
      z = 0;
      g += 1
      funcs.append(fdata[i].strip('{').strip("\n").strip("func").strip('').strip('{').strip(' '))
    #elif("}" in fdata[i]):
      
    elif ("//" not in fdata[i]):
      print(str(g)+","+str(z))
      try:
        fprog[g][z] = str(fprog[g][z]) + fdata[i].strip('\n')
      except:
        print("ERROR AT: ("+str(g)+","+str(z)+")")
  #print(funcs)
  #print(fprog)
def parse(fileName):
  global stack
  global outstack
  locX = 0
  locY = 0
  pnt = ''
  lines = []
  with open(fileName, "r") as f:
    # read data segment
    lines = f.readlines()
    if("include" in lines[locY]):
      pFunc((lines[locY].strip(' ').split(" ")[1].strip('\n')))
      locY += 1
    while(lines[locY][locX] != '}'):
      #print(lines[locY])
      if("//" in lines[locY]):    # ignore comments
        locY += 1
        if(debug):
            print("comment")
      elif "data{" in lines[locY]:
        locY += 1
      elif("push" in lines[locY]):
        if(debug):
          print("push command")
        stack.append(int(lines[locY].strip(' ').split(" ")[1].strip('\n')))
        locY+=1
      elif("let" in lines[locY]):
        v = lines[locY].strip(' ').split(" ")
        vars.append(v[1].strip('\n'))
        data.append(int(v[2].strip('\n')))
        locY += 1
    # exceute the program (lamo)
    locY += 1
    while(lines[locY][locX] != '}'):
      if("//" in lines[locY] or "entry" in lines[locY] or lines[locY] == '\n'):
        locY += 1
      elif("push" in lines[locY]):
        stack.append(getVar(lines[locY].strip(' ').split(" ")[1].strip('\n')))
        locY += 1
      elif("add" in lines[locY]):
        outstack.append(int((stack[len(stack) -1 ])+  int(stack[len(stack)-2])))
        locY += 1
      elif("sub" in lines[locY]):
        outstack.append(int((stack[len(stack) -1 ]) - int(stack[len(stack)-2])))
        locY += 1
      elif("out" in lines[locY]):
        print(outstack[len(outstack)-1])
        locY += 1
      elif("los" in lines[locY]):
        setVar((lines[locY].strip(' ').split(" ")
                [1].strip('\n')),outstack[len(outstack)-1])
      elif(lines[locY].strip(' ').strip('\n').split(" ")[0] in funcs):
        exc(funcs.index(lines[locY].strip(' ').split(" ")[0].strip('\n')))
        locY += 1
        # do the function idk lamo
      elif("let" in lines[locY]):
        v = lines[locY].strip(' ').split(" ")
        vars.append(v[1].strip('\n'))
        data.append(int(v[2].strip('\n')))
        locY += 1
      else:
        print("ERROR, "+lines[locY] +" is not a command.")
        print(lines[locY].strip(' ').split(" "))
        break
def exc(ind):
  s = 0
  #print("IND: "+str(ind))
  d = open("tmp.gapl","w")
  with open("tmp.gapl","a") as g:
    
    g.write("data{\n")
    g.write("}\n")
    g.write("entry{\n")
    while(True):
      try:
        g.write(str(fprog[ind][ind][s]).strip(''))
        g.write('\n');
        s+= 1;
      except Exception as e:
        #print("EEEE: "+str(s)+str(e))
        break
    g.write("}\n")
  parse("tmp.gapl")
print("parsing file: "+sys.argv[1])
try:
  parse(sys.argv[1])
except Exception as e :
  print("Error: "+str(e))
  print(traceback.format_exc())
  print("Stack dump:")
  print(stack)
  print(outstack)
  #print(fprog)
print("===== Program finished.  Details: =====")
print("// Stack")
print(stack)
print("// Output stack")
print(outstack)
print("// Loaded functions ")
print(funcs)
print("? Would you like to see loaded function data ? (y/n)")
if(input("") == 'y'):
  print(fprog)