class RestrictedList(list):
    def __init__(self, allowed_type, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.allowed_type = allowed_type
        # Initial check for elements passed during initialization
        for item in self:
            if not isinstance(item, self.allowed_type):
                raise TypeError(
                    f"All elements must be of type {self.allowed_type.__name__}"
                )

    def append(self, item):
        if not isinstance(item, self.allowed_type):
            raise TypeError(
                f"Only elements of type {self.allowed_type.__name__} can be added."
            )
        super().append(item)

    def extend(self, iterable):
        for item in iterable:
            if not isinstance(item, self.allowed_type):
                raise TypeError(
                    f"Only elements of type {self.allowed_type.__name__} can be added."
                )
        super().extend(iterable)

    def __setitem__(self, key, value):
        if not isinstance(value, self.allowed_type):
            raise TypeError(
                f"Only elements of type {self.allowed_type.__name__} can be assigned."
            )
        super().__setitem__(key, value)


# Example usage:
my_int_list = RestrictedList(int)
my_int_list.append(10)
# my_int_list.append("hello") # This would raise a TypeError
