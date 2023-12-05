## Main Script File
import string
import random
from MorseConverter import MorseConverter

# MorseDecoder = MorseConverter()
# morse_value = '....x.x.-..x.-..x---xx.--x---x.-.x.-..x-..'
# text_value = 'hello world'

# print("input: " + morse_value)
# print("\n")
# result = MorseDecoder.morse_to_text(morse_value)
# print("output: " + result)
# print("\n")
# deresult = MorseDecoder.text_to_morse(text_value)
# print("reverse: " + deresult)
# print("\n")

# isSimilar = deresult == morse_value
# print("isSimilar: " + isSimilar.__str__())

POLLUX_KEY = 'x.--.x.-x.'

POLLUX_KEY_DICT = {
  'x': [1,6,9],
  '.': [2,5,7,0],
  '-': [3,4,8],
}

print(POLLUX_KEY)
print("\n")
print(POLLUX_KEY_DICT)

MorseLib = MorseConverter()
plain_text = 'hello world'
sample_text = 'when one teaches two learn'
morse_value = MorseLib.text_to_morse(sample_text)

def pollux_encode(morse_value):
  result = ''
  for code in morse_value:
    for key, value in POLLUX_KEY_DICT.items():
      if code == key:
        result += random.choice(value).__str__() + ''
  return result

def group_by_five(pollux_value):
  result = ''
  count = 0
  for code in pollux_value:
    if count == 5:
      result += ' '
      count = 0
    result += code + ''
    count += 1
  return result

print("\n")
print("input: " + morse_value)
print("\n")
result = pollux_encode(morse_value)
print("output: " + morse_value)
print("output: " + group_by_five(result))

