# 20. Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        
        expected_closing_brackets = []
        
        open_to_close_bracket_map = {"(" : ")", "{" : "}", "[" : "]"}
        
        for bracket in s:
            if bracket in ["(", "{", "["]:
                closed_bracket = open_to_close_bracket_map.get(bracket)
                expected_closing_brackets.append(closed_bracket)

            else:
                if len(expected_closing_brackets) == 0:
                    return False
                expected_closing_bracket = expected_closing_brackets.pop()
                if bracket != expected_closing_bracket:
                    return False
                
        if len(expected_closing_brackets) > 0:
            return False
        
        return True
