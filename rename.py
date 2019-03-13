import glob, os

allfiles = glob.glob('*.jpg')

title = input("Title:")
count = input("Start number:")
count = int(count)

for afile in allfiles:
  new_filename = title +'_' + str(count) + '.jpg'
  print (new_filename)
  os.rename(afile, new_filename)
  count += 1
print("Done, last filename:", new_filename)
os.system("pause")