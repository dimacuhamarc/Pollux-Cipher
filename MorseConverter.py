## Morse Code Module
# MorseConverter Class File

class MorseConverter: 
  
  ##  Morse Code Dictionary, Basis for Translation
  MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...',
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
    '0': '-----', ' ': 'xx', '': 'x'
  }



  ##  Translates Morse Code to Plain Text
  @staticmethod # Converts Function to a Static Method
  def morse_to_text(morse_code):
    morse_code = morse_code.split('x')
    text = ''
    for code in morse_code:
        for key, value in MorseConverter.MORSE_CODE_DICT.items():
            if code == value:
                text += key + ''
            elif code == key:
                text += ' '
    return text
  
  ##  Translates Plain Text to Morse Code
  @staticmethod # Converts Function to a Static Method
  def text_to_morse(text):
      morse_code = ''
      for char in text.upper():
          if char in MorseConverter.MORSE_CODE_DICT.keys():
              if char != ' ':
                  morse_code += MorseConverter.MORSE_CODE_DICT[char] + 'x'
              else:
                  morse_code += 'x'
      return morse_code[:-1].rstrip('x')