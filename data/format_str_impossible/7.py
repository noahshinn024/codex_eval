def format_str_impossible(str1, str2):
  """
  Reverses, and deletes every other letter from a combination of two strings and
  converts it to a string of all of the vowels in reverse order and returns a
  string of c's with length equal to the vowel count
  """
  
  # reverse the strings
  str1 = str1[::-1]
  str2 = str2[::-1]

  # slice the strings
  str1 = str1[0:len(str1):2]
  str2 = str2[1:len(str2):2]

  # convert to vowel string
  str1 = "".join(vowel_list(str1))
  str2 = "".join(vowel_list(str2))

  # concatenate both strings
  str1 = str2 + str1

  # return c string with length of vowel string
  return "c" * len(str1)



"""
input: ('', '')   --->   ERROR
input: ('hello', 'world')   --->   ERROR
input: ('abc', 'def')   --->   ERROR
input: ('hellohellohello', 'world')   --->   ERROR
input: ('123456789', 'world')   --->   ERROR
"""