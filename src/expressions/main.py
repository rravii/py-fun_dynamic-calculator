from . import Expressions   # import from package (__init__.py)

def main():
    # 
    # create 'Expressions' instance using Expressions.numbers[] as default
    expressions = Expressions()
    expressions.print_results()
    # 
    # create 2nd 'Expressions' instance using numbers[] passed to constructor
    # expressions_2 = Expressions([3, 1, 2, 4, 2, 3])
    # expressions_2.print_results()
    #
    # create 3rd 'Expressions' instance using empty list[]
    expressions_3 = Expressions([1, 4, 6, 67, 6, 8, 23, 8, 34, 49, 67, 6, 8, 23, 37, 67, 6, 34, 19, 67,6, 8])
    expressions_3.print_results()
