# combine_str
# inputs = [["''", "''"], ["'hello'", "'world'"], ["'abc'", "'def'"], ["'hellohellohello'", "'world'"], ["'123456789'", "'world'"]]
# outputs = ["''", "'helloworld'", "'abcdef'", "'hellohellohelloworld'", "'123456789world'"]

# format_str
# inputs = [["''", "''"], ["'hello'", "'world'"], ["'abc'", "'def'"], ["'hellohellohello'", "'world'"], ["'123456789'", "'world'"]]
# outputs = ["''", "'drwle'", "'fdb'", "'drwleolhle'", "'drw8642'"]

# format_str_complex
# inputs = [["''", "''"], ["'hello'", "'world'"], ["'abc'", "'def'"], ["'hellohellohello'", "'world'"], ["'123456789'", "'world'"]]
# outputs = ["''", "'e'", "''", "'eoe'", "''"]

# format_str_impossible
# inputs = [["''", "''"], ["'hello'", "'world'"], ["'abc'", "'def'"], ["'hellohellohello'", "'world'"], ["'123456789'", "'world'"]]
# outputs = ["''", "'c'", "''", "'ccc'", "''"]

# remove_prime_nums
# inputs = [["[]", "[]"], ["[1, 2, 3]", "[4, 5, 6]"], ["[4, 6, 8]", "[10, 12, 14]"], ["[1, 1, 1]", "[37, 39, 13]"], ["[]", "[1, 2, 3]"]]
# outputs = ["[]", "[4, 6]", "[4, 6, 8, 10, 12, 14]", "[]", "[1, 2, 3]"]

# interweave_lsts
# inputs = [["[]", "[]"], ["[1, 2, 3]", "[]"], ["[]", "[10, 12, 14]"], ["['hello']", "[37, 39, 13]"], ["['hello', 5, '6']", "[1, 2, 3]"]]
# outputs = ["[]", "[1, 2, 3]", "[10, 12, 14]", "['hello', 37, 39, 13]", "['hello', 1, 5, 2, '6', 3]"]

# sort_lsts
inputs = [["[]", "[]"], ["[1, 2, 3]", "[]"], ["[]", "[1, 9, 3]"], ["['a', 1]", "['b', 'c', 'a']"], ["['z', '?', '6']", "[1, 2, 3]"]]
outputs = ["[]", "[1, 2, 3]", "[1, 3, 9]", "[1, 'a', 'a', 'b', 'c']", "['?', '6', 'z', 1, 2, 3]"]