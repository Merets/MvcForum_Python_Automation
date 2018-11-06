class TypeValidator(object):
    @classmethod
    def validate_type(cls, variable, class_type):
        expected_type_name = class_type.__name__
        actual_type_name = type(variable).__name__
        if not isinstance(variable, class_type):
            raise TypeError(f"Passing argument should be of type '{expected_type_name}', but actually is"
                            f" '{actual_type_name}'")
