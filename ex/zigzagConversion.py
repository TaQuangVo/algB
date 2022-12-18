def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    result = ""
    wave_len = numRows + (numRows - 2)

    if numRows == 1:
        return s

    for i in range(numRows):
        current_index = i
        while(current_index < len(s)):
            result = result + s[current_index]

            next_index = current_index + wave_len - i - i

            if(i == 0 or i == numRows-1 or  next_index >= len(s)):
                current_index = current_index + wave_len
                continue

            result = result + s[next_index]
            current_index = current_index + wave_len
    
    return result

r = convert("PAYPALISHIRING", 3)
print(r)
