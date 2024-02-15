from pydantic import BaseModel

from mypackage.mymodule import MyClass


class TestMyClass:
    """
    A class with pytest unit tests.
    """

    def test_something(self):
        my_class = MyClass()
        assert my_class.do_something() == "abc"

    def test_bo4e_importable(self):
        from mypackage.bo4e import Bankverbindung

        assert issubclass(Bankverbindung, BaseModel)
