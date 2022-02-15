def format_str_impossible(str1, str2):
  """
  Reverses, and deletes every other letter from a combination of two strings and
  converts it to a string of all of the vowels in reverse order and returns a
  string of c's with length equal to the vowel count
  """
  
  vowels = 'aeiou'
  index = 0
  reversed_str1 = ''
  reversed_str2 = ''
  while index < len(str1):
    if index % 2 == 0:
      reversed_str1 += str1[-index-1]
    else:
      reversed_str2 += str2[-index-1]
    index += 1
  vowels_str = ''
  for char in reversed_str1 + reversed_str2:
    if char in vowels:
      vowels_str += char
  return 'c' * len(vowels_str)


"""
input: ('', '')   --->   PASSED
input: ('hello', 'world')   --->   FAILED
input: ('abc', 'def')   --->   FAILED
input: ('hellohellohello', 'world')   --->   ERROR
input: ('123456789', 'world')   --->   ERROR
"""