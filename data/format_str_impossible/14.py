def format_str_impossible(str1, str2):
  """
  Reverses, and deletes every other letter from a combination of two strings and
  converts it to a string of all of the vowels in reverse order and returns a
  string of c's with length equal to the vowel count
  """
  
  str1 = str1[::-1]
  str2 = str2[::-1]
  str1 = str1[1::2]
  str2 = str2[::2]
  vowels = "aeiou"
  str_impossible = "c" * len([letter for letter in str1 + str2 if letter in vowels])
  return str_impossible


"""
input: ('', '')   --->   PASSED
input: ('hello', 'world')   --->   PASSED
input: ('abc', 'def')   --->   PASSED
input: ('hellohellohello', 'world')   --->   PASSED
input: ('123456789', 'world')   --->   PASSED
"""