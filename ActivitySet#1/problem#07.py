str = "X-DSPAM-Confidence: 0.8475"

text = str.find(':')
piece = str[text+2:]

value = float(piece)
print(value)