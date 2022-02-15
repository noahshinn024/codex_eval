def format_str_complex(str1, str2):
  """
  Reverses, and deletes every other letter from a combination of two strings and
  returns a string of all of the vowels in reverse order
  """
  
  str1_list = list(str1)
  str2_list = list(str2)
  str1_list.reverse()
  str2_list.reverse()
  str1_list.pop(1)
  str1_list.pop(3)
  str2_list.pop(1)
  str2_list.pop(3)
  str1_list.extend(str2_list)
  str_vowel = ""
  for i in str1_list:
    if i in "aeiou":
      str_vowel += i
  return str_vowel


"""
input: ('', '')   --->   ERROR
input: ('hello', 'world')   --->   FAILED
input: ('abc', 'def')   --->   ERROR
input: ('hellohellohello', 'world')   --->   FAILED
input: ('123456789', 'world')   --->   FAILED
"""