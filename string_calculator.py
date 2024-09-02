import re

class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        # Handle custom delimiters
        delimiters = [',', '\n']
        if numbers.startswith("//"):
            parts = numbers.split('\n', 1)
            custom_delimiter = parts[0][2:]
            delimiters.append(custom_delimiter)
            numbers = parts[1]

        # Create a regex pattern for splitting by multiple delimiters
        pattern = '|'.join(map(re.escape, delimiters))
        num_list = re.split(pattern, numbers)

        # Convert to integers and check for negatives
        result = 0
        negatives = []
        for num in num_list:
            if num:
                n = int(num)
                if n < 0:
                    negatives.append(n)
                result += n

        if negatives:
            raise ValueError(f"Negative numbers not allowed: {', '.join(map(str, negatives))}")

        return result
