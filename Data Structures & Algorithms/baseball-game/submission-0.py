class Solution: 
    def calPoints(self, operations: List[str]) -> int:
        records = [] # stack for score

        for operation in operations:
            # case of +
            if operation == "+":
                records.append(records[-1] + records[-2])                
            # case of D
            elif operation == "D":                
                records.append(records[-1] * 2)
            # case of C
            elif operation == "C":
                records.pop()
            # case of int
            else:
                records.append(int(operation))
        
        return sum(records)

        