# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nested_list):
        def flatten(my_list):
            result = []
            for item in my_list:
                if isinstance(item, list):
                    flat_list = flatten(item)
                    result += flat_list
                else:
                    result.append(item)
            return result
        self.flat_list = flatten(nested_list)

    def next(self) -> int:
        return self.flat_list.pop(0)

    def has_next(self) -> bool:
        if len(self.flat_list) > 0:
            return True
        return False


check1 = NestedIterator([1, [4, [6]]])

print(check1.flat_list)

print(check1.next())
print(check1.next())
print(check1.next())


#
# print(check1)
#
# print(check1.next())

# Your NestedIterator object will be instantiated and called as such:
# nested_list1 = [1, [4, [6]]]
# i, v = NestedIterator(nested_list1), []
# while i.has_next():
#   v.append(i.next())
#
# print(v)
