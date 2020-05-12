import random
def suffixer(text, suffixes, rate):
    lines = text.split("\n")
    new = []
    for line in lines:
        if line:
            words = line.split(" ")
            for i in range(len(words)):
                if (random.random() <= rate):
                    suffix = random.choice(suffixes)
                    if any(j in words[i] for j in ['!', '?', ',', '.', ':', ';']):
                        words[i] = words[i][:-1] + suffix + words[i][-1:]
                    else:
                        words[i] = words[i] + suffix
                else:
                    pass
            line = " ".join(words)
            new.append(line)
        else:
            pass
    return("\n".join(new))
def shuffler(text):
    lines = text.split("\n")
    random.shuffle(lines)
    new = []
    for line in lines:
        if line:
            words = line.split(" ")
            random.shuffle(words)
            line = " ".join(words).lower().capitalize()
            new.append(line)
        else:
            pass
    return("\n".join(new))
