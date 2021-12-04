def msf(str1):
  nsc = [ch for ch in str1 if ch!=' ']
  spaces_char = len(str1) - len(nsc)
  result = ' '*spaces_char
  result = '"'+result + ''.join(nsc)+'"'
  return(result)

print(msf("Spotify  "))