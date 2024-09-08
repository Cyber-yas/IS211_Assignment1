
def list_divide(numbers, divide):
    return sum(1 for number in numbers if number % divide ==0

class ListDivideException(Exception):
    pass

def test_list_divide():
    try:
        assert listDivide([1,2,3,4,5]) == 2
        assert listDivide([2,4,6,8,10]) == 5
        assert listDivide([30, 54, 63,98, 100], divide=10) == 2
        assert listDivide([]) == 0
        assert listDivide([1,2,3,4,5], 1) == 5
    except AssertionError as e:
        raise ListDivideExeption(f"Test failed: {e}")
        
if __name__ == "__main__":

    test_list_divide()
    print("All tests passed,")
