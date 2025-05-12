def validate_input(N: int) -> bool:
    """
    Validate the input to ensure it is a positive integer greater than 1.
    Args:
        N (int): The input number to validate
    Returns:
        bool: True if N is a positive integer greater than 1, False otherwise
    """
    return isinstance(N, int) and N > 1
