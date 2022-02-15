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
  vowels = "aeiou"
  num_of_vowels = 0
  for i in range(len(str1)):
    if str1[i] in vowels:
      num_of_vowels += 1
  for i in range(len(str2)):
    if str2[i] in vowels:
      num_of_vowels += 1
  return "c" * num_of_vowels



"""
input: ('', '')   --->   PASSED
input: ('hello', 'world')   --->   PASSED
input: ('abc', 'def')   --->   FAILED
input: ('hellohellohello', 'world')   --->   PASSED
input: ('123456789', 'world')   --->   PASSED
"""