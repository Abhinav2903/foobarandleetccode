def canBeEqual(target: [int], arr: [int]) -> bool:
    for f,d in enumerate(target):
        if(target.count(d)!=arr.count(d)):
            return False
        print(f)    
    return True

print(canBeEqual([3,7,9],[3,7,11]))    