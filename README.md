#	Pollux Cipher Decoder and Encoder
This repository contains a program that decodes **Pollux-Encrypted data**, and **encodes Plain-text Data**.

##	Author
- [Marc Dimacuha](https://github.com/dimacuhamarc)

## Background
  
The **Pollux Cipher** uses **Morse Code encryption technique**, where a plain-text is first transformed into Morse Code, and then, each Morse Code symbol is replaced with a numerical digit. 

These three Morse Code symbols ( **Dash** [--], **Dot** [•], and **Separator** [x] ) and **ten numerical digits** (1,2,3,4,5,6,7,8,9,0) may represent the same symbol.

##	Usage
**Default Key** used in the codebase:\
``POLLUX_KEY  =  'x.--.x.-x.'``\
using this mapping position\
``POLLUX_POS  = [1,2,3,4,5,6,7,8,9,0]``

**Mapped Key**
```
'x': [1, 6, 9], 
'.': [2, 5, 7, 0], 
'-': [3, 4, 8]
```

**The Codebase is written in Python3**
To use, compile and run ``main.py``

**Sample Output**\
Assembled Encoder
```
Plain-Text(input): He Who Must Not Be Named
Pollux-Encoded(result): 57751 76958 89557 29838 61841 77495 50949 93218 83986 64502 65918 59581 34671 305
```
Assembled Decoder
```
Pollux-Encoded(input): 27209 29108 81025 51884 61886 27412 20139 64264 44946 13022 95698 51581 34959 357
Plain-text(output): He Who Must Not Be Named
```
