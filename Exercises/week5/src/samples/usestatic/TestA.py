# package samples.usestatic

from A import A


def test_a():
    a1 = A()
    a2 = A()

    print(a1.get_instance_attr() == 0)
    # print(A.get_instance_attr())   # No, not a class method, can't call without an instance

    print(a1.get_class_attr())
    print(a2.get_class_attr())
    print(a1.get_class_attr_static())  # Bad style, don't use object when calling static method
    print(A.get_class_attr_static())    # Use class when calling static method

    a1.set_instance_attr(0)
    a2.set_instance_attr(1)
    a1.set_class_attr(5)

    print(a1.get_instance_attr() != a2.get_instance_attr())
    # Changed of one object affects all objects
    print(a2.get_class_attr() == 5)

    # print(A.get_instance_attr_static())  # Also uncomment method declaration in A.py


if __name__ == "__main__":
    test_a()
