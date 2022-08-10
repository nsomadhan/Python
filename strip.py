name = "       john         "
print( name.strip() ) # Striping all space

name =   "$$$john$$$$"  # no white space 
print( name.strip('$') )

name =   "$$$john$$$$  " # white space
print( name.strip('$') )

name =   "  $$$john$$$$"  # white space 
print( name.strip('$') )

name =   "  $$$john$$$$    " 
stripname = name.strip() # First removeing white space 
print(stripname.strip('$')) # the print with removing $

def namestrip():
   stripwhitespace = name.strip().strip('$')
   print(stripwhitespace)

print ('With function')
namestrip()


print ('variable pass With function')
name = '  $$variable$$ '
def varnamestrip(name):
   stripwhitespace = name.strip().strip('$')
   return stripwhitespace
print(varnamestrip(name))




#print("striping with for loop")

#for namestrip in name:
#    namestrip.strip()
#    namestrip.strip('$')
#    print(namestrip)

