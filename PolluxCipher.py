import random
from MorseConverter import MorseConverter

class PolluxCipher:
  POLLUX_KEY = 'x.--.x.-x.'
  POLLUX_POS = [1,2,3,4,5,6,7,8,9,0]

  POLLUX_KEY_DICT = {}
  for char, pos in zip(POLLUX_KEY, POLLUX_POS):
    if char not in POLLUX_KEY_DICT:
        POLLUX_KEY_DICT[char] = []
    POLLUX_KEY_DICT[char].append(pos)
  
  @staticmethod
  def pollux_encode(morse_value):
    result = ''
    for code in morse_value:
      for key, value in PolluxCipher.POLLUX_KEY_DICT.items():
        if code == key:
          result += random.choice(value).__str__() + ''
    return result
  
  @staticmethod 
  def pollux_decode(pollux_value, pollux_key_dict):
      morse_value = ''
      for num in pollux_value:
          for key, value in pollux_key_dict.items():
              if int(num) in value:
                  morse_value += key
      return MorseConverter.morse_to_text(morse_value)

  @staticmethod
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
