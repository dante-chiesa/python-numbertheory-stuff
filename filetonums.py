from typing import NamedTuple, List

_BYTEORDER = "little"
#_BYTEORDER = "big"

class FileNums(NamedTuple):
    nums: List[int]
    padding: int

    def to_file(self, filename:str):
        return numstofile(self, filename)

def filetonums(filename: str, *, blocksize:int = 4) -> FileNums:
    nums: List[int] = []
    padding = 0
    with open(filename, "rb") as f:
        while True:
            data:bytes = f.read(blocksize);
            if data is None or len(data) == 0: # end of file
                break;
            #pad with zeros, should only happen to last block
            if len(data) < 4:
                if padding != 0:
                    raise Exception("Multiple short blocks somehow!")
                padding = 4 - len(data)
                data += bytes([0 for _ in range(padding)])
            num = int.from_bytes(data, _BYTEORDER);
            nums.append(num);
    
    return FileNums(nums, padding)

def numstofile(numsobj:FileNums, filename:str,*,blocksize:int = 4):
    with open(filename, "wb") as f:
        lenbutone = len(numsobj.nums) - 1
        for i in range(lenbutone):
            num = numsobj.nums[i]
            data:bytes = num.to_bytes(blocksize, _BYTEORDER)
            f.write(data)
        lastblock = numsobj.nums[lenbutone].to_bytes(blocksize, _BYTEORDER)
        bytecount = blocksize - numsobj.padding
        truncated = lastblock[0:bytecount]
        f.write(truncated)
