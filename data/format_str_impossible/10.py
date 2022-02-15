def format_str_impossible(str1, str2):
  """
  Reverses, and deletes every other letter from a combination of two strings and
  converts it to a string of all of the vowels in reverse order and returns a
  string of c's with length equal to the vowel count
  """
  
  str1 = str1[::-1]
  str2 = str2[::-1]
  str3 = ""
  str4 = ""
  for i in range(len(str1)):
    if i % 2 == 1:
      str3 += str1[i]
  for i in range(len(str2)):
    if i % 2 == 0:
      str4 += str2[i]
  return str3 + str4


"""
input: ('', '')   --->   PASSED
input: ('hello', 'world')   --->   FAILED
input: ('abc', 'def')   --->   FAILED
input: ('hellohellohello', 'world')   --->   FAILED
input: ('123456789', 'world')   --->   FAILED
"""