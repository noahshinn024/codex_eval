def format_str_impossible(str1, str2):
  """
  Reverses, and deletes every other letter from a combination of two strings and
  converts it to a string of all of the vowels in reverse order and returns a
  string of c's with length equal to the vowel count
  """
  
  # Reverse strings
  str1 = str1[::-1]
  str2 = str2[::-1]

  # Concatenate strings
  str_comb = str1 + str2
  vowel_list = []
  for char in str_comb:
    # If current char is a vowel,
    if char in vowels:
      # Append vowel to list
      vowel_list.append(char)
      # Remove vowel from string
      str_comb = str_comb.replace(char, '')

  # Convert list to string
  str_vowels = ''.join(vowel_list)
  # Reverse string
  str_vowels = str_vowels[::-1]
  # Create a string of c's equal to the length of vowel_list
  str_c = 'c' * len(vowel_list)
  # Format string and return
  return format_str(str_vowels, str_c)


"""
input: ('', '')   --->   ERROR
input: ('hello', 'world')   --->   ERROR
input: ('abc', 'def')   --->   ERROR
input: ('hellohellohello', 'world')   --->   ERROR
input: ('123456789', 'world')   --->   ERROR
"""