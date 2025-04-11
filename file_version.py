def findMaxVersion(cls,input1,input2):
    import re
    if input2==0:
        return -1
    maxVersion=-1
    pattern=r"File_(\d+)"
    for file in input1:
        match=re.match(pattern,file.strip())
        if match:
            Version=int(match.group(1))
            maxVersion=max(maxVersion,Version)
    return maxVersion