def format_str_impossible(str1, str2):
  """
  Reverses, and deletes every other letter from a combination of two strings and
  converts it to a string of all of the vowels in reverse order and returns a
  string of c's with length equal to the vowel count
  """
  
  str1 = str1[::-1]
  str2 = str2[::-1]
  str3 = ''
  vowels = 'aeiou'
  for i in range(len(str1)):
    if i % 2 == 0:
      str3 += str1[i]
  for j in range(len(str2)):
    if j % 2 != 0:
      str3 += str2[j]
  str3 = str3[::-1]
  str4 = ''
  for k in range(len(str3)):
    if str3[k] in vowels:
      str4 += 'c'
    else:
      str4 += str3[k]
  return str4


"""
input: ('', '')   --->   PASSED
input: ('hello', 'world')   --->   FAILED
input: ('abc', 'def')   --->   FAILED
input: ('hellohellohello', 'world')   --->   FAILED
input: ('123456789', 'world')   --->   FAILED
"""