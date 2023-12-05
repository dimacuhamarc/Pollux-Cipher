## Main Script File

from MorseConverter import MorseConverter

MorseDecoder = MorseConverter()
morse_value = '....x.x.-..x.-..x---xx.--x---x.-.x.-..x-..'
text_value = 'hello world'

print("input: " + morse_value)
print("\n")
result = MorseDecoder.morse_to_text(morse_value)
print(result)
deresult = MorseDecoder.text_to_morse(text_value.upper())
print("\n")
print("Decoded: " + deresult)
print("\n")
print("Original: " + morse_value)
print("\n")

print("IsSimilar?" + morse_value == deresult)