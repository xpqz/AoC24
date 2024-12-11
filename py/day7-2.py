def read_file(filename):
    with open(filename) as file:
        return zip(*[(int(p[0]), list(map(int, p[1].split())))  
                    for p in (line.split(':') for line in file)])

def reachable(curr, nums, target):        
    max_val = min_val = concat_val = curr    
    for n in nums:
        max_val = max(max_val * n, max_val + n)
        min_val = min(min_val * n, min_val + n)
        concat_val = int(str(concat_val) + str(n))
        
    return not ((target > max_val and target > concat_val) or 
                (target < min_val and target < concat_val))

def evaluate(nums, target):

    # def backtrack(pos, curr):
    #     if pos == len(nums):
    #         return curr == target
            
    #     if not reachable(curr, nums[pos:], target):
    #         return False
            
    #     if pos == 0:
    #         return backtrack(1, nums[0])
            
    #     ops = [
    #         lambda x, y: x + y,
    #         lambda x, y: x * y,
    #         lambda x, y: int(str(x) + str(y))
    #     ]
            
    #     for func in ops:
    #         if backtrack(pos + 1, func(curr, nums[pos])):
    #             return True
                
    #     return False

    # return backtrack(0, 0)

    def backtrack(pos, curr):
        print(f"Level {pos}: curr={curr}")  # Show where we are
        
        if pos == len(nums):
            print(f"Check: {curr} vs {target}")  # Show leaf comparison
            return curr == target
                
        if not reachable(curr, nums[pos:], target):
            print(f"Pruned: curr={curr}, remaining={nums[pos:]}")  # Show pruning
            return False
                
        if pos == 0:
            return backtrack(1, nums[0])
                
        ops = [
            lambda x, y: x + y,
            lambda x, y: x * y,
            lambda x, y: int(str(x) + str(y))
        ]
                
        for func in ops:
            new_val = func(curr, nums[pos])
            print(f"Try: {curr} -> {new_val}")  # Show each attempt
            if backtrack(pos + 1, new_val):
                print(f"Found through: {curr} -> {new_val}")  # Show successful path
                return True
                    
        return False

    return backtrack(0, 0)

if __name__ == '__main__':
    print(evaluate([6, 8, 6, 15], 7290))
    # print(sum(t for t, nums in zip(*read_file('../d/t')) if evaluate(nums, t)))
