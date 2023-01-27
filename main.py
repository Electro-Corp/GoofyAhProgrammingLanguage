import sys
import traceback
stack = []
outstack = []
charstack = []
vars = []
data = []
funcs = []
fprog = [[""]*50 for _ in range(50)] 
cmp = 0
debug = False
g = -1
z = 0
p = None
def getVar(name):
  if(name in vars):
    return data[vars.index(name)]
  else:
    return None
def setVar(name, val):
  if(name in vars):
    data[vars.index(name)] = val 
def pFunc(file):
  #print("called (real)")
  global funcs
  global fprog
  global z
  global g
  with open(file, "r") as f:
    g+=1
    fdata = f.readlines()
  
  for i in range(len(fdata) - 1):
    #print(str(g)+","+str(z))
    #print(fprog)
    if(fdata[i]):
      z+=1
    if("{" in fdata[i]):
      #z = 0
      #g += 1
      funcs.append(fdata[i].strip('{').strip("\n").strip("func").strip('').strip('{').strip(' '))
    elif("}" in fdata[i]):
     # z = 0 
      g+=1
    elif ("//" not in fdata[i]):
      try:
        fprog[g][z] =  fdata[i].strip('\n')
      except:
        print("ERROR AT: ("+str(g)+","+str(z)+")")
  #print("Done")
  #print(funcs)
  #print(fprog)
def parse(fileName):
  global stack
  global outstack
  global cmp
  locX = 0
  locY = 0
  pnt = ''
  lines = []
  with open(fileName, "r") as f:
    # read data segment
    #print(locY)
    lines = f.readlines()
    
    while(lines[locY][locX] != '}'):
      if("include" in lines[locY]):
        pFunc((lines[locY].strip(' ').split(" ")[1].strip('\n')))
        locY += 1
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
      elif("lchar" in lines[locY]):
        charstack.append((lines[locY].strip(' ').split(" ")[1].strip('\n')))
        locY += 1
    # exceute the program (lamo)
    locY += 1
    while(lines[locY][locX] != '}'):
      #print(str(locY)+"| "+lines[locY])
      if("//" in lines[locY] or "entry" in lines[locY] or lines[locY] == '\n'):
        locY += 1
      elif("push" in lines[locY]):
        stack.append(getVar(lines[locY].strip(' ').split(" ")[1].strip('\n')))
        locY += 1
      elif("lchar" in lines[locY]):
        charstack.append((lines[locY].strip(' ').split(" ")[1].strip('\n')))
        locY += 1
      elif("lspecInd" in lines[locY]):
        charstack.append(charstack[len(charstack) - int(lines[locY].strip(' ').split(" ")[1].strip('\n'))])
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
       # print("Los got a request for var: "+(lines[locY].strip(' ').split(" ")
       #         [1].strip('\n'))+", which will be set to: "+str(outstack[len(outstack)-1]))
        setVar((lines[locY].strip(' ').split(" ")
                [1].strip('\n')),outstack[len(outstack)-1])
        locY += 1
      elif(lines[locY].strip(' ').strip('\n').split(" ")[0] in funcs):
        exc(funcs.index(lines[locY].strip(' ').split(" ")[0].strip('\n')))
        locY += 1
       
        # do the function idk lamo
      elif("let" in lines[locY]):
        v = lines[locY].strip(' ').split(" ")
        vars.append(v[1].strip('\n'))
        data.append(int(v[2].strip('\n')))
        locY += 1
      #
      # COMPARE BIT SECTION
      #
      elif ("cmp" in lines[locY]):
        if(stack[len(stack) -1 ] == stack[len(stack) -2]):
          cmp = 1
        else:
          cmp = 0
        locY += 1
      elif ("lmp" in lines[locY]):
        stack.append(cmp)
        locY += 1
      elif ("jcb" in lines[locY]):
        if(cmp == 1):
          locY = int(lines[locY].strip(' ').split(" ")[1].strip('\n'))
        else:
          locY += 1
      # GOOFY AHH
      elif ("goto" in lines[locY]):
        locY = int(lines[locY].strip(' ').split(" ")[1].strip('\n'))
      #
      # File features
      #
      elif ("lfile" in lines[locY]):
        p = open(charstack[len(charstack)-1], lines[locY].strip(' ').split(" ")[1].strip('\n'))
        locY += 1
      elif ("wfile" in lines[locY]):
        p.write(charstack[len(charstack)-1])
        locY += 1 
      elif ("rfile" in lines[locY]):
        charstack.append(p.readlines())
        locY += 1 
      #
      # Print
      #
      elif("print" in lines[locY]):
        print(charstack[len(charstack)-1])
        locY+=1
      elif("trchar" in lines[locY]):
        charstack.append(str(stack[len(stack)-1]))
        locY+=1
      #
      # Stack access
      #
      elif("sload" in lines[locY]):
        outstack.append(int(lines[locY].strip(' ').split(" ")[1].strip('\n')))
        locY += 1
      else:
        print("ERROR, "+lines[locY] +" is not a command.")
        print(lines[locY].strip(' ').split(" "))
        break
      #print(stack)
def exc(ind):
  global fprog
  s = -3
  #print("IND: "+str(ind))
  d = open("tmp.gapl","w")
  with open("tmp.gapl","a") as g:
    g.write("data{\n")
    g.write("}\n")
    g.write("entry{\n")
    while(True):
      try:
        if(fprog[ind][s] != ""):
          g.write(str(fprog[ind][s]).strip(''))
          g.write('\n');
        s+= 1;
        if(s == 50):
          break
      except Exception as e:
        #print("EEEE: "+str(s)+str(e))
        break
    g.write("}\n")
  parse("tmp.gapl")
try:
  print("parsing file: "+sys.argv[1])
except:
  print("Error, file may not exist")
  exit()
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
print("// Char stack")
print(charstack)
print("// Compare Bit")
print(str(cmp))
print("// Loaded functions ")
print(funcs)
print("? Would you like to see loaded function data ? (y/n)")
if(input("") == 'y'):
  print(fprog)