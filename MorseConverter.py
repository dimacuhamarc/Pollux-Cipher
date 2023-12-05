## Morse Code Converter and Translator

class MorseConverter: 
  MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                  'C': '-.-.', 'D': '-..', 'E': '.',
                  'F': '..-.', 'G': '--.', 'H': '....',
                  'I': '..', 'J': '.---', 'K': '-.-',
                  'L': '.-..', 'M': '--', 'N': '-.',
                  'O': '---', 'P': '.--.', 'Q': '--.-',
                  'R': '.-.', 'S': '...', 'T': '-',
                  'U': '..-', 'V': '...-', 'W': '.--',
                  'X': '-..-', 'Y': '-.--', 'Z': '--..',
                  '1': '.----', '2': '..---', '3': '...--',
                  '4': '....-', '5': '.....', '6': '-....',
                  '7': '--...', '8': '---..', '9': '----.',
                  '0': '-----', ' ': 'xx', '': 'x'}

  @staticmethod
  def morse_to_text(morse_code):
    morse_code = morse_code.split('x')
    text = ''
    for code in morse_code:
        for key, value in MorseConverter.MORSE_CODE_DICT.items():
            if code == value:
                text += key + ''
            elif code == 'xx':
                text += ' '
    return text
  
  # @staticmethod
  # def text_to_morse(text):
  #     morse_code = ''
  #     for char in text.upper():
  #         if char in MorseConverter.MORSE_CODE_DICT.keys():
  #             morse_code += MorseConverter.MORSE_CODE_DICT[char]
  #         elif char :
  #             morse_code += 'x'
  #         else:
  #             morse_code += 'xx'
  #     return morse_code[:-1]  # Remove the trailing 'x'
  
  @staticmethod
  def text_to_morse(text):
      morse_code = ''
      for char in text.upper():
          if char in MorseConverter.MORSE_CODE_DICT.keys():
              morse_code += MorseConverter.MORSE_CODE_DICT[char] + 'x'
          elif char == ' ':
              morse_code += 'xx'
      return morse_code[:-1].rstrip('x')