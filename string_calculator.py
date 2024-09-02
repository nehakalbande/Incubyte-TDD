import re

class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        # Default delimiters are comma and newline
        delimiters = [',', '\n']
        
        # Check if there is a custom delimiter
        if numbers.startswith("//"):
            parts = numbers.split('\n', 1)
            delimiter_part = parts[0][2:]
            numbers = parts[1]

            # Check for multiple delimiters with custom length
            if delimiter_part.startswith('[') and delimiter_part.endswith(']'):
                # Extract all delimiters within square brackets
                delimiters = re.findall(r'\[(.*?)\]', delimiter_part)
            else:
                # Single custom delimiter
                delimiters = [delimiter_part]

        # Create a regex pattern to split by multiple delimiters
        pattern = '|'.join(map(re.escape, delimiters))
        num_list = re.split(pattern, numbers)

        # Convert to integers, ignore numbers bigger than 1000, and check for negatives
        result = 0
        negatives = []
        for num in num_list:
            if num:
                n = int(num)
                if n < 0:
                    negatives.append(n)
                elif n <= 1000:
                    result += n

        if negatives:
            raise ValueError(f"Negative numbers not allowed: {', '.join(map(str, negatives))}")

        return result
