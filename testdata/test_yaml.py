import pytest
import yaml

class TestData:
    @pytest.mark.parametrize("a,b",yaml.safe_load(open("./testdata/data.yml")))
    def test_foo(self,a,b):
        print(f"a + b = {a + b}")
