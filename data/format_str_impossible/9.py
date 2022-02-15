def format_str_impossible(str1, str2):
  """
  Reverses, and deletes every other letter from a combination of two strings and
  converts it to a string of all of the vowels in reverse order and returns a
  string of c's with length equal to the vowel count
  """
  
  new_str = ''
  vowels = ['a', 'e', 'i', 'o', 'u']
  for l1, l2 in zip(str1[::-1], str2[::-1]):
    if l1 in vowels and l2 in vowels:
      new_str = ''.join([new_str, l2])
    elif l1 in vowels:
      new_str = ''.join([new_str, l1])
    else:
      new_str = ''.join([new_str, l2])
  return ''.join(['c' for x in new_str])


"""
input: ('', '')   --->   PASSED
input: ('hello', 'world')   --->   FAILED
input: ('abc', 'def')   --->   FAILED
input: ('hellohellohello', 'world')   --->   FAILED
input: ('123456789', 'world')   --->   FAILED
"""