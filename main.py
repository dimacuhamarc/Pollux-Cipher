## Main Script File
from MorseConverter import MorseConverter
from PolluxCipher import PolluxCipher

def AssembleEncoder(plain_text):
  Morse = MorseConverter()
  Pollux = PolluxCipher()
  morse_value = Morse.text_to_morse(plain_text)
  pollux_value = Pollux.pollux_encode(morse_value)
  group_by_five = Pollux.group_by_five(pollux_value)
  print("input: " + plain_text)
  print("output: " + group_by_five)

def AssembleDecoder(pollux_value):
  Pollux = PolluxCipher()
  pollux_value = pollux_value.replace(' ', '')
  plain_text = Pollux.pollux_decode(pollux_value, Pollux.POLLUX_KEY_DICT)
  print("input: " + pollux_value)
  print("output: " + plain_text)

AssembleEncoder('He Who Must Not Be Named')
AssembleDecoder('27209 29108 81025 51884 61886 27412 20139 64264 44946 13022 95698 51581 34959 357')