def get_max_occuring_char(str1):
  ASCII_SIZE = 256
  ctr = [0] * ASCII_SIZE
  m = -1
  ch = ''
  for i in str1:
    ctr[ord(i)]+=1;
 
  for i in str1:
    if m < ctr[ord(i)]:
      m = ctr[ord(i)]
      ch = i
  return ch

print(get_max_occuring_char("Python: Get file creation and modification date/times"))