def format_str_impossible(str1, str2):
  """
  Reverses, and deletes every other letter from a combination of two strings and
  converts it to a string of all of the vowels in reverse order and returns a
  string of c's with length equal to the vowel count
  """
  
  str1 = str1[::-1]
  str2 = str2[::-1]
  str1 = str1[1::2]
  str2 = str2[0::2]
  str1 = str1.replace("a", "")
  str2 = str2.replace("e", "")
  str1 = str1.replace("i", "")
  str2 = str2.replace("o", "")
  str1 = str1.replace("u", "")
  str2 = str2.replace("a", "")
  str2 = str2.replace("e", "")
  str2 = str2.replace("i", "")
  str2 = str2.replace("o", "")
  str2 = str2.replace("u", "")
  str1 = str1[::-1]
  str2 = str2[::-1]
  vowel_count = len(str1) + len(str2)
  str1 = ("c" * vowel_count)
  return str1


"""
input: ('', '')   --->   PASSED
input: ('hello', 'world')   --->   FAILED
input: ('abc', 'def')   --->   FAILED
input: ('hellohellohello', 'world')   --->   FAILED
input: ('123456789', 'world')   --->   FAILED
"""