name = "       john         "
print( name.strip() ) # Striping all space

name =   "$$$john$$$$"  # no white space 
print( name.strip('$') )

name =   "$$$john$$$$  " # white space
print( name.strip('$') )

name =   "  $$$john$$$$"  # white space 
print( name.strip('$') )
