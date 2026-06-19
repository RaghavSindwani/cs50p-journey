import sys
if len(sys.argv) == 1:
    print("No Font Specified")

elif len(sys.argv) == 3:
    print("Font: "+ sys.argv[2])

else:
    print("Invalid")
