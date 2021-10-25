# package samples.override

# Possible to make mistakes when overriding
def override_mistake_program():
    a = B()
    print(f"Ten times as much is {a.long_and_hard_to_spell_name(5.0)}")


class A:
    # Possible to override
    def long_and_hard_to_spell_name(self, f: float):
        return f


class B(A):
    # No override! Instead inherited method from A.
    def long_and_hard_to_spel_name(self, f: float):
        return 10 * f


if __name__ == "__main__":
    override_mistake_program()
