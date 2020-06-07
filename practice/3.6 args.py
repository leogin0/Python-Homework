def printinfo(*args,**vardict ):
   print ('first：',list(args))
   print('second:',vardict)

printinfo(11,12,a=1,b=3)