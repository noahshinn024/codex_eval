def format_str_impossible(str1, str2):
  """
  Reverses, and deletes every other letter from a combination of two strings and
  converts it to a string of all of the vowels in reverse order and returns a
  string of c's with length equal to the vowel count
  """
  
  str1 = str1[::-1]
  str2 = str2[::-1]
  str1 = str1[::2]
  str2 = str2[::2]
  str1 = str1[::-1]
  str2 = str2[::-1]
  vowels = 'aeiou'
  vowels = vowels[::-1]
  str1 = list(str1)
  str2 = list(str2)
  str1.reverse()
  str2.reverse()
  str1 = ''.join(str1)
  str2 = ''.join(str2)
  str3 = ''
  for i in range(len(str1)):
    if str1[i] in vowels:
      str3 += 'c'
    else:
      str3 += str1[i]
  for i in range(len(str2)):
    if str2[i] in vowels:
      str3 += 'c'
    else:
      str3 += str2[i]
  return str3
"""
input: ('', '')   --->   PASSED
input: ('hello', 'world')   --->   FAILED
input: ('abc', 'def')   --->   FAILED
input: ('hellohellohello', 'world')   --->   FAILED
input: ('123456789', 'world')   --->   FAILED
"""