# Human Calculator

This program rewrites mathematical expressions to the corresponding language representation

The sample user story is `sample_usage.py`

```python
from HumanCalculator import HumanCalc
calc = HumanCalc()
print(calc.convert('342 - 340 = 2'))
# >>> three hundreds forty-two minus three hundreds forty equals two
```



# Testing

The tests provided in `tests` folder (*TestCalcUX* and *TestCalcComponents*) cover the majority of usecases. To test the entire application, including *UX* and *component* tests

    $ make test

Testing the application is quite convenient using the *makefile*. Alternatively, to test the entire package

    $ python -m unittest discover -v

Run *component* specific tests

    $ python -m unittest discover -s tests/component -v


# Features

* **unit testing**
* modern and scalable project layout


# Credits

https://realpython.com/python-testing/
