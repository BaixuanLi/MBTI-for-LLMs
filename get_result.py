result = [
    {"A": "J", "B": "P"},
    {"A": "E", "B": "I"},
    {"A": "P", "B": "J"},
    {"A": "S", "B": "N"},
    {"A": "P", "B": "J"},
    {"A": "F", "B": "T"},
    {"A": "J", "B": "P"},
    {"A": "J", "B": "P"},
    {"A": "F", "B": "T"},
    {"A": "E", "B": "I"},
    {"A": "J", "B": "P"},
    {"A": "P", "B": "J"},
    {"A": "E", "B": "I"},
    {"A": "N", "B": "S"},
    {"A": "I", "B": "E"},
    {"A": "E", "B": "I"},
    {"A": "T", "B": "F"},
    {"A": "I", "B": "E"},
    {"A": "N", "B": "S"},
    {"A": "S", "B": "N"},
    {"A": "F", "B": "T"},
    {"A": "N", "B": "S"},
    {"A": "T", "B": "F"},
    {"A": "S", "B": "N"},
    {"A": "I", "B": "E"},
    {"A": "T", "B": "F"},
    {"A": "N", "B": "S"},
    {"A": "F", "B": "T"},
]

statistics = {
    "I": 0,
    "N": 0,
    "F": 0,
    "J": 0,
    "E": 0,
    "S": 0,
    "T": 0,
    "P": 0,
}

print("Please enter the 28-answers for the test:")
answer = input()  # "AABBBAAAB..."
assert len(answer) == 28

for i in range(len(answer)):
    statistics[result[i][answer[i]]] += 1

mbti = []
if statistics["I"] > statistics["E"]:
    mbti.append("I")
else:
    mbti.append("E")

if statistics["N"] > statistics["S"]:
    mbti.append("N")
else:
    mbti.append("S")

if statistics["F"] > statistics["T"]:
    mbti.append("F")
else:
    mbti.append("T")

if statistics["J"] > statistics["P"]:
    mbti.append("J")
else:
    mbti.append("P")

print("The statistical result is {}".format(statistics))
print("Consequently, the MBTI result is {}".format(''.join(mbti)))