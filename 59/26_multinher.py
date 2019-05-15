# python is an object-oriented language with built in facilities for making multiple inheritance tractable, using
# functionalities like super, however its better to avoid using multiple inheritance altogether.

#if you find yourself desiring the convenience and encapsulation that comes with multiple inheritance, consider writing a mix-in instead
# a mix-in is a small class that only defines a set of additional methods that a class should provide. Mix in classes
# dont define their own instance attributes nor require their init constructor to be called

"""writing mix ins is easy because python makes it trivial to inspect the current state of any object regardless of its type.
 Dynamic inspection lets you write generic functionality a single time, in a mix-in, that can be applied to many other classes.
 Mixins can be composed and layered to minimize repetitive code and maximize reuse.

 For example, say you want the ability to convert a python object from its in-memory representation to a dictionary thats
 ready for serialisation. Why not write this functionality generically so you can use it with all of your classes?"""

#here i define an example mix-in that accomplishes this with a new public method thats added to any class that inherits from it

class ToDictMixin(object):
    def to_dict(self):
        return self._traverse_dict(self.__dict__)

#The implementation details are straightforward and rely on dynamic attribute access using hasattr, dynamic type inspection
#with isinstance, and accessing the instance directory __dict__.

#The hasattr() method returns true if an object has the given named attribute and false if it does not."""

    def _traverse_dict(self, instance_dict):
        output = {}
        for key, value in instance_dict.items():
            output[key] = self._traverse(key, value)
        return output

# The isinstance() function returns True if the specified object is of the specified type, otherwise False

    def _traverse(self, key, value):
        if isinstance(value, ToDictMixin):
            return value.to_dict()
        elif isinstance(value, dict):
            return self._traverse_dict(value)
        elif isinstance(value, list):
            return [self._traverse(key, i) for i in value]
        elif hasattr(value, '__dict__'):
            return self._traverse_dict(value.__dict__)
        else:
            return value

# here define an ex of a class that uses the mix in to make a dictionary representation of a binary tree

class BinaryTree(ToDictMixin):
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

#translating a large number of related python objects into a dictionary becomes easy

tree = BinaryTree(10, left=BinaryTree(7, right=BinaryTree(9)), right=BinaryTree(13, left=BinaryTree(11)))
print(tree.to_dict())

"""The best part about mix ins is that you can make their generic functionality pluggable so behaviours can be overridden
when required. For example, here I define a subclass of Binary Tree that holds a reference to its parent. This circular
reference would cause the default implementation of ToDictMixin.to_dict to loop forever."""

class BinaryTreeWithParent(BinaryTree):
    def __init__(self, value, left=None, right=None, parent=None):
        super().__init__(value, left=left, right=right)
        self.parent = parent

# the solution is to override the ToDictMixin._traverse method in the BinaryTreeWithParent  class to only process values that matter,
# preventing cycles encountered by the mixin. Here, i override the _traverse method to not traverse the parent and just insert its
# numerical value

    def _traverse(self, key, value):
        if (isinstance(value, BinaryTreeWithParent) and key == 'parent'):
            return value.value #prevent cycles
        else:
            return super()._traverse(key, value)

# calling BinaryTreeWithParent.to_dict will work without issue because the circular referencing properties arent followed.

root = BinaryTreeWithParent(10)
root.left = BinaryTreeWithParent(7, parent=root)
root.left.right = BinaryTreeWithParent(9, parent=root.left)
print(root.to_dict())

# By defining BinaryTreeWithparent._traverse. I've also enabled any class that has an attribut of type BinaryTreeWithParent
# to automatically work with ToDictMixin

class NamedSubTree(ToDictMixin):
    def __init__(self, name, tree_with_parent):
        self.name = name
        self.tree_with_parent = tree_with_parent
