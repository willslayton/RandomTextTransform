# RandomTextTransform
A python script to apply transformations to bodies of text using randomness.

## Suffixer
Chooses a random suffix and adds it the the end of words in a body of text. Takes input text, an array of suffixes, and a float between 0.0 and 1.0 to determine the rate of suffix application.

#### Example:
This will add the suffixes -ghetti and -oli () to words randomly theoretically 20% of the time for the text file `text.txt`.
```
import randomtexttransform as rtt
with open('text.txt', "r") as f:
  text = f.read()
  rtt.suffixer(text, ['ghetti', 'oli'], 0.20)
```

## Shuffler
Randomly shuffles the lines of text and then iterates through them to shuffle the order of words in that text. Only need the text to shuffle as an argument.

#### Example:
This will randomly shuffle the lines and words within them for the text file `text.txt`.
```
import randomtexttransform as rtt
with open('text.txt', "r") as f:
  text = f.read()
  rtt.shuffler(text)
```
