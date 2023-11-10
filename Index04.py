def main(s):
    """
    The s string variable is given. Return three characters from the beginning.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    s1= s[0]
    s2= s[1]
    s3= s[2]
    return s1+s2+s3
print(main("number"))
print(main("codeschool"))