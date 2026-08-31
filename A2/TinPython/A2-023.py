

from types import SimpleNamespace

def main():
        
        
    _STRING = input().strip()
    _STRING_LOWER = _STRING.lower()
    _STRING_LEN = len(_STRING_LOWER)


    _pureblood = True
    _first_impurity_index = -1
    
    _a = SimpleNamespace(safe_index=0, streak_best=0, streak_new=0)
    
    
    def impure(index):
        nonlocal _pureblood, _first_impurity_index
        _pureblood = False
        _first_impurity_index = index if _first_impurity_index == -1 else _first_impurity_index
    

    _unknown = True
    for i in range(_STRING_LEN):
        
        _a.safe_index >>= 1
        
        char = _STRING_LOWER[i]
        ipp_in_string = True if i + 1 <= _STRING_LEN - 1 else False
        charpp = _STRING_LOWER[i + 1] if ipp_in_string else ""
        
        
        if char != "i" and char != "t":
            _unknown = False
        
        if char == "r":
            _a.streak_new = 0
            
            if ipp_in_string:
                _a.safe_index |= ( 1 << 1 )
                if charpp != "a":
                    impure(i + 1)
            else:
                impure(i)
            
        elif char == "a":
            
            _a.streak_new += 1
            if _a.streak_new > _a.streak_best:
                _a.streak_best = _a.streak_new
            
            if i == 0 or not _a.safe_index & 1:
                impure(i)
                
            elif ipp_in_string: 
                _a.safe_index |= ( 1 << 1 )
        
        elif char == "b":
            _a.streak_new = 0
            
            if ipp_in_string:
                if not charpp in ["i", "t"]:
                    impure(i + 1)
            else:
                impure(i)
        
        else: 
            _a.streak_new = 0
                

    if _unknown:
        print(f"unknown {_STRING_LEN}")
        return
    
    elif not _pureblood:
        print(f"no {_first_impurity_index}")
        return
    
    else:
        print(f"yes {_a.streak_best}")
        return
            
    
if __name__ == "__main__":
    main()