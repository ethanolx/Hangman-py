# finish library for 4 to 8 letter words
# for dictionary (temporary usage only)


def string_wrapper(string, step):
    wrapped_string = ""
    num_of_sections = len(string) / step
    i = 0
    while i < num_of_sections:
        j = 0
        wrapped_string += '"'
        while j < step:
            wrapped_string += string[i * step + j]
            j += 1
        wrapped_string += '", '
        i += 1
    return wrapped_string


# 3-letter words
a3 = ["act", "add", "age", "ago", "aid", "air", "all", "and", "any", "app", "are", "arm", "art", "ask", "aim", "amp", "ass", "ate",
      "ace", "arc", "ash", "ave", "awe", "axe", "ado", "aft", "aha", "ail", "ale", "ani", "ant", "ape", "apt", "ark", "awl", "aye"]

b3 = ["bad", "bag", "bar", "bay", "bed", "big", "bit", "box", "boy", "bus", "but", "buy", "ban", "bet", "bid", "bug",
      "bah", "beg", "bib", "boa", "bog", "boo", "bop", "bot", "bro", "bub", "bud", "bum", "bun", "bye", "bat", "bee", "bow"]

c3 = ["can", "cap", "car", "cat", "cup", "cut", "caw", "cob", "cod", "cog", "coo",
      "cot", "cub", "cud", "cur", "cab", "cad", "cam", "con", "cop", "cow", "cry", "cue"]

d3 = ["dad", "day", "did", "die", "dog", "dry", "due", "dig", "dot", "dab", "dew", "dim",
      "din", "dit", "dub", "dud", "dam", "den", "dip", "doc", "don", "dug", "duo", "dye"]

e3 = ["eat", "egg", "end", "era", "eye", "ear", "ego", "eve", "ebb",
      "eel", "elf", "elk", "elm", "emu", "eon", "ere", "err", "ewe"]

f3 = ["fan", "far", "fat", "fee", "few", "fit", "fix", "fly", "for", "fun", "fed",
      "fax", "flu", "fog", "fox", "fad", "fib", "fig", "fin", "foe", "foo", "fro", "fry"]

g3 = ["gap", "gas", "get", "god", "got", "gun", "guy", "gym", "gal",
      "gel", "gem", "gen", "gig", "git", "gum", "gut", "gag", "gin", "goo"]

h3 = ["had", "has", "her", "hey", "him", "his", "hit", "hot", "how", "hat", "hip", "hub", "ham", "hay",
      "hid", "hue", "huh", "hag", "hap", "hem", "hen", "hew", "hex", "hoe", "hog", "hug", "hum", "hut"]

i3 = ["ice", "its", "ink", "inn", "icy",
      "ill", "imp", "ion", "ire", "irk", "ivy"]

j3 = ["job", "joy", "jar", "jet", "jam", "jaw",
      "jab", "jay", "jig", "jog", "jot", "jug"]

k3 = ["key", "kid", "kit", "keg", "kin", "kip"]

l3 = ["lab", "law", "lay", "led", "leg", "let", "log", "lot", "low", "lid",
      "lie", "lip", "lag", "lap", "lit", "lad", "lob", "loo", "lug", "lye"]

m3 = ["man", "map", "may", "men", "met", "mix", "mom", "mac", "mad", "max", "mid", "mod",
      "mag", "mat", "mob", "mud", "mug", "mum", "mar", "maw", "mew", "mic", "moo", "mop", "mow"]

n3 = ["net", "new", "nor", "not", "now", "nut", "nab",
      "nag", "nah", "nap", "nay", "nip", "nob", "nod", "nun"]

o3 = ["off""oil""old""one""our""out""own""oak""odd""opt""ops""ore""owe""owl""oaf""oar""oat""oft""orb"]

p3 = ["pay", "per", "pet", "pin", "pot", "pro", "put", "pad", "pan", "par", "pen", "pie", "pit", "pop", "pal", "pic", "pig",
      "pod", "pub", "pat", "paw", "pax", "pea", "pee", "peg", "pew", "ply", "poo", "pow", "pox", "pry", "pug", "pun", "pup", "pus"]

q3 = []

r3 = ["ran", "raw", "red", "rid", "row", "run", "ram", "rod", "rap", "rat", "rig", "rim", "rip",
      "rub", "rug", "rum", "rad", "rag", "ray", "rib", "rob", "roe", "rot", "rue", "rut", "rye"]

s3 = ["sad", "sat", "saw", "say", "sea", "see", "set", "she", "sit", "six", "sky", "son", "sun", "sin", "sir", "ski", "spa", "sum",
      "sap", "sew", "shy", "sip", "soy", "spy", "sub", "sac", "sag", "sic", "sis", "sly", "sob", "sod", "sow", "sty", "sue", "sup"]

t3 = ["tab", "tag", "tax", "tea", "ten", "the", "tip", "too", "top", "try", "two", "tap", "thy",
      "tie", "toy", "tad", "tan", "tee", "tin", "toe", "tow", "tub", "tar", "tit", "tot", "tug", "tum"]

u3 = ["use", "ups", "urn"]

v3 = ["via", "van", "vat", "vet", "vex", "vid", "vie", "vow"]

w3 = ["war", "was", "way", "web", "wet", "who", "why", "win", "won", "wow", "wed",
      "wan", "wax", "wit", "wad", "wag", "wee", "wig", "woe", "wok", "woo", "wry"]

x3 = []

y3 = ["yes", "yet", "you", "yea", "yep", "yak", "yam",
      "yap", "yaw", "yen", "yin", "yon", "yum", "yup"]

z3 = ["zoo", "zip", "zag", "zap", "zig", "zit"]

three_letter_words = a3 + b3 + c3 + d3 + e3 + f3 + g3 + h3 + i3 + j3 + k3 + \
    l3 + m3 + n3 + o3 + p3 + q3 + r3 + s3 + t3 + u3 + v3 + w3 + x3 + y3 + z3

# 4-letter words
a4 = ["able", "acid", "aged", "also", "area", "army", "away"]

b4 = ["baby", "back", "ball", "band", "bank", "base", "bath", "bear", "beat", "been", "beer", "bell", "belt", "best", "bill", "bird", "blow", "blue", "boat", "body", "bomb", "bond", "bone", "book", "boom", "born", "boss", "both", "bowl", "bulk", "burn", "bush", "busy"]

c4 = ["call", "calm", "came", "camp", "card", "care", "case", "cash", "cast", "cell", "chat", "chip", "city", "club", "coal", "coat", "code", "cold", "come", "cook", "cool", "cope", "copy", "core", "cost", "crew", "crop"]

d4 = ["dark", "data", "date", "dawn", "days", "dead", "deal", "dean", "dear", "debt", "deep", "deny", "desk", "dial", "diet", "disc", "disk", "does", "done", "door", "dose", "down", "draw", "drew", "drop", "drug", "dual", "duke", "dust", "duty"]

e4 = ["each", "earn", "ease", "east", "easy", "edge", "else", "even", "ever", "evil", "exit"]

f4 = ["face", "fact", "fail", "fair", "fall", "farm", "fast", "fate", "fear", "feed", "feel", "feet", "fell", "felt", "file", "fill", "film", "find", "fine", "fire", "firm", "fish", "five", "flat", "flow", "food", "foot", "ford", "form", "fort", "four", "free", "from", "fuel", "full", "fund"]

g4 = ["gain", "game", "gate", "gave", "gear", "gene", "gift", "girl", "give", "glad", "goal", "goes", "gold", "golf", "gone", "good", "gray", "grew", "grey", "grow", "gulf"]

h4 = ["hair", "half", "hall", "hand", "hang", "hard", "harm", "hate", "have", "head", "hear", "heat", "held", "hell", "help", "here", "hero", "high", "hill", "hire", "hold", "hole", "holy", "home", "hope", "host", "hour", "huge", "hung", "hunt", "hurt"]

i4 = ["idea", "inch", "into", "iron", "item"]

j4 = ["jack", "jane", "jean", "john", "join", "jump", "jury", "just"]

k4 = ["keen", "keep", "kent", "kept", "kick", "kill", "kind", "king", "knee", "knew", "know"]

l4 = ["lack", "lady", "laid", "lake", "land", "lane", "last", "late", "lead", "left", "less", "life", "lift", "like", "line", "link", "list", "live", "load", "loan", "lock", "logo", "long", "look", "lord", "lose", "loss", "lost", "love", "luck"]

m4 = ["made", "mail", "main", "make", "male", "many", "mark", "mass", "matt", "meal", "mean", "meat", "meet", "menu", "mere", "mice", "mile", "milk", "mill", "mind", "mine", "miss", "mode", "mood", "moon", "more", "most", "move", "much", "must"]

n4 = ["name", "navy", "near", "neck", "need", "news", "next", "nice", "nick", "nine", "none", "nose", "note"]

o4 = ["okay", "once", "only", "onto", "open", "oral", "over", "owls"]

p4 = ["pace", "pack", "page", "paid", "pain", "pair", "palm", "park", "part", "pass", "past", "path", "peak", "pick", "pink", "pipe", "plan", "play", "plot", "plug", "plus", "poll", "pool", "poor", "port", "post", "pull", "pure", "push"]

q4 = []

r4 = ["race", "rail", "rain", "rank", "rare", "rate", "read", "real", "rear", "rely", "rent", "rest", "rice", "rich", "ride", "ring", "rise", "risk", "road", "rock", "role", "roll", "roof", "room", "root", "rose", "rule", "rush"]

s4 = ["safe", "said", "sake", "sale", "salt", "same", "sand", "save", "seat", "seed", "seek", "seem", "seen", "self", "sell", "send", "sent", "sept", "ship", "shop", "shot", "show", "shut", "sick", "side", "sign", "site", "size", "skin", "slip", "slow", "snow", "soft", "soil", "sold", "sole", "some", "song", "soon", "sort", "soul", "spot", "star", "stay", "step", "stop", "such", "suit", "sure"]

t4 = ["take", "tale", "talk", "tall", "tank", "tape", "task", "team", "tech", "tell", "tend", "term", "test", "text", "than", "that", "them", "then", "they", "thin", "this", "thus", "till", "time", "tiny", "told", "toll", "tone", "tony", "took", "tool", "tour", "town", "tree", "trip", "true", "tune", "turn", "twin", "type"]

u4 = ["unit", "upon", "used", "user"]

v4 = ["vary", "vast", "very", "vice", "view", "vote"]

w4 = ["wage", "wait", "wake", "walk", "wall", "want", "ward", "warm", "wash", "wave", "ways", "weak", "wear", "week", "well", "went", "were", "west", "what", "when", "whom", "wide", "wife", "wild", "will", "wind", "wine", "wing", "wire", "wise", "wish", "with", "wood", "word", "wore", "work"]

x4 = []

y4 = ["yard", "yeah", "year", "your"]

z4 = ["zero", "zone"]

four_letter_words = a4 + b4 + c4 + d4 + e4 + f4 + g4 + h4 + i4 + j4 + k4 + l4 + m4 + n4 + o4 + p4 + q4 + r4 + s4 + t4 + u4 + v4 + w4 + x4 + y4 + z4

# 5-letter words
five_letter_words = []
# 6-letter words
six_letter_words = []
# 7-letter words
seven_letter_words = []
# 8-letter words
eight_letter_words = []

