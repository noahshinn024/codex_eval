def format_str_impossible(str1, str2):
  """
  Reverses, and deletes every other letter from a combination of two strings and
  converts it to a string of all of the vowels in reverse order and returns a
  string of c's with length equal to the vowel count
  """
  

  # reverses the two strings
  str1 = str1[::-1]
  str2 = str2[::-1]

  # deletes every other letter from the two strings
  str1 = list(str1)
  str2 = list(str2)
  del str1[1::2]
  del str2[0::2]
  str1 = "".join(str1)
  str2 = "".join(str2)

  # combines the two strings
  str3 = str1 + str2

  # converts the combined string to a list of the vowels
  vowels = ['a', 'e', 'i', 'o', 'u']
  str4 = []
  for letter in list(str3):
    if letter in vowels:
      str4.append(letter)

  # reverses the list of vowels
  str4 = str4[::-1]

  # creates a string of c's with length equal to the vowel count
  str5 = ""
  for i in range(len(str4)):
    str5 += 'c
"""
input: ('', '')   --->   ERROR
input: ('hello', 'world')   --->   ERROR
input: ('abc', 'def')   --->   ERROR
input: ('hellohellohello', 'world')   --->   ERROR
input: ('123456789', 'world')   --->   ERROR
"""