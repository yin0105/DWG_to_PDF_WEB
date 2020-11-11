file_in = 'f:\\Operations\\masterbills\\text\\A72262000000.txt'

f = open(file_in, 'r')
in_file = ''
for line in f.readlines():
  in_file = in_file + line
f.close()

#####################################################################################################

#search_for = '--------------------------------------------------------------------------------'
#replace_with = '--------------------------------------------------------------------------------\n'
#print in_file.replace(search_for, replace_with)



#if iCnt == 55:
search_for   = '--------------------------------------------------------------------------------'
if in_file.find(search_for) > 0:
  replace_with = '--------------------------------------------------------------------------------\n'
  in_file      = in_file.replace(search_for, replace_with)

print(in_file)
