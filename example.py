import randomtexttransform as rtt
with open('Iron_Man_1_Script.txt', "r") as f:
    text = f.read()
    print(rtt.suffixer(text, ['ghetti', 'oli'], 0.20))
    print(rtt.shuffler(text))
