symbols = '$¢£¥€¤'

generator_expresion = tuple(ord(symbol) for symbol in symbols)

import array 

generator_expresion = array.array('I', (ord(symbol) for symbol in symbols))

