import os
import re
import pandas as pd
import openai
from io import StringIO
from contextlib import redirect_stdout

from tests import inputs, outputs

openai.api_key = os.getenv("OPENAI_API_KEY")

NUM_COMPLETIONS = 20

def read_prompt():
  with open('py_func.py', 'r') as f:
    return f.read()

def read_func_name():
  with open('py_func.py', 'r') as f:
    string = f.read()
    func_name = re.findall(r"\s*def\s+(\w+)\s*", string)
    func_name = [x.replace("def ", "") for x in func_name][0]
    return func_name

def completion(prompt):
  return openai.Completion.create(
    engine="code-davinci-001",
    prompt=prompt,
    temperature=0.6,
    max_tokens=128,
    top_p=1,
    n=NUM_COMPLETIONS,
    frequency_penalty=0,
    presence_penalty=0,
    stop=["print", "def", "if __name__"]
)

def test_results(prompt, completions, func_name):
  passed = 0
  failed = 0
  errors = 0
  log_dir = os.path.join('data', func_name)
  results_file = os.path.join('data', func_name, 'results.py')
  log_file = os.path.join('data', 'log.csv')
  os.mkdir(log_dir)
  for i in range(NUM_COMPLETIONS):
    print(f"\n##### Testing completion #{i} #####\n")
    completion = '  ' + completions.choices[i].text
    py_file = os.path.join(log_dir, f"{i}.py")
    performance_str = '"""\n'
    for j in range(len(inputs)):
      input1 = inputs[j][0]
      input2 = inputs[j][1]
      output = outputs[j]
      try:
        print(f"Test #{j}:")
        f = StringIO()
        with redirect_stdout(f):
          exec(f"{prompt}\n{completion}\nprint({func_name}({input1}, {input2}) == {output})")
          res = f.getvalue().replace('\n', '')
          if 'True' in res:
            print('PASSED')
            performance_str += f"input: ({input1}, {input2})   --->   PASSED\n"
            passed += 1
          else:
            print('FAILED')
            performance_str += f"input: ({input1}, {input2})   --->   FAILED\n"
            failed += 1
        print('\n')
      except Exception as e:
        print(e)
        performance_str += f"input: ({input1}, {input2})   --->   ERROR\n"
        errors += 1
    performance_str += '"""'
    with open(py_file, 'w') as f:
      f.write(f"{prompt}\n{completion}\n{performance_str}")
    performance_str = ''
  accuracy = round(passed / (NUM_COMPLETIONS * len(inputs)) * 100, 2)
  with open(results_file, 'w') as f:
    f.write(f'"""\nTESTS PASSED: {passed}\nTESTS FAILED: {failed}\nERRORS: {errors}\nACCURACY: {accuracy}\n"""')
  log_to_csv(log_file, [func_name, accuracy, passed, failed, errors, prompt])

  print(f"\n\nTESTS PASSED: {passed}\nTESTS FAILED: {failed}\nERRORS: {errors}\nACCURACY: {accuracy}%\n\n\n")

def log_to_csv(log_file, lst):
  df = pd.DataFrame([lst], columns=['FUNC_NAME', 'ACCURACY', 'PASSED', 'FAILED', 'ERRORS', 'PROMPT'])
  df.to_csv(log_file, index=False, mode='a', header=None)


def evaluate_codex():
  prompt = read_prompt()
  completions = completion(prompt)
  func_name = read_func_name()
  test_results(prompt, completions, func_name)

if __name__ == '__main__':
  evaluate_codex()
  