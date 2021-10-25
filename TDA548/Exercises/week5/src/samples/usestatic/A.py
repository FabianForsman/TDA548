# package samples.usestatic

# A class using class variables and methods (static variables and methods)
# 
# This shows:
# - An instance method can use/call instance and class
# variables and methods.
# - A class method can only call class methods and use
# class variables (no "this" in static methods)
# Class method can't know which object!
class A:
    # This is a constant (use upper case)
    # Since it is defined outside of the constructor (__init__),
    # it belongs to the class itself, not the objects created from it
    CONST = 34
    # Same here, class attribute, not instance attribute
    class_attr = 1

    def __init__(self):
        self.instance_attr = 0  # This attribute can change between instances   

    def get_class_attr(self):  # Instance can access classVar
        return self.class_attr

    @staticmethod
    def get_class_attr_static():    # Class method also can - note no self parameter
        return A.class_attr         # Must find class_attr via class name A, not self.

    def get_instance_attr(self):    # Instance method, ok
        return self.instance_attr

    # @staticmethod
    # def get_instance_attr_static():  # No, class method can't access instance_attr
    #     return A.instance_attr       # Uncommenting and calling gives "AttributeError"

    @staticmethod
    def set_class_attr_static(class_attr):
        A.class_attr = class_attr

    def set_class_attr(self, class_attr):  # Instance can access attributes of its class
        type(self).class_attr = class_attr

    def set_instance_attr(self, instance_attr):
        self.instance_attr = instance_attr

    @staticmethod
    def set_instance_attr_static(instance_attr):    # Class can't access
        A.instance_attr = instance_attr             # This becomes a completely different attribute!
