class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        prev = collections.defaultdict(int)
        arr = []
        
        for name in names:
            if name not in prev:
                arr.append(name)
                prev[name] = 0
            else:
                prev[name] += 1
                counter = prev[name]
                
                while True:
                    new_name = name + "(" + str(counter) + ")"
                    if new_name not in prev:
                        arr.append(new_name)
                        prev[new_name] = 0
                        break
                    else:
                        counter += 1
        return arr