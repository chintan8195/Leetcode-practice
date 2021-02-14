# https://forum.codebreakersacademy.com/t/amazon-oa2-count-k-distinct-substrings/992

from collections import defaultdict
def countKDistinctSubstrings(inputString, num):
    group_chars = []
    i = 0
    prev = None
    while i < len(inputString):
        c = inputString[i]
        if prev != c:
            group_chars.append((c,1))
        else:
            group_chars[-1] = (c, group_chars[-1][1] + 1)
        prev = c
        i += 1
    substrings = 0
    if num == 1:
        for c, count in group_chars:
            substrings += count * (count + 1) // 2
        return substrings
    for l in range(0, len(group_chars)):
        window_counts = defaultdict(int)
        for r in range(l, len(group_chars)):
            window_counts[group_chars[r][0]] += group_chars[r][1]
            if len(window_counts.keys()) == num:
                substrings += group_chars[r][1] * group_chars[l][1]
            elif len(window_counts.keys()) > num:
                break
    return substrings


#print(countKDistinctSubstrings("abc",2))
#print(countKDistinctSubstrings("abafg",2))
print(countKDistinctSubstrings("ppqpqss",2))


""" 
Q: Describe the problem statement in 2-3 sentences.
Ans: find maximum number of subbstrings exactly K distinct character.

Describe your solution in 2-3 sentences.


Practice walking through the code.

Do 5 stack traces for each problem and write out the intermediate variables. Send them here in Slack.

What is the runtime of this function? And write an explanation for why that is the case.

What is the space complexity of this function? And write an explanation for why that is the case.

 """