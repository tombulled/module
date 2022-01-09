# module
Module utility library

## Usage

### `override`
Override a module with an object

```python
# lib.py

import module

@module.override
def foo():
    print('foo!')
```

```python
>>> import lib
>>> lib
<function foo at 0x7f330a053b50>
```

### `call`
Make a module callable

```python
# lib.py

import module

@module.call
def foo():
    print('foo!')
```

```python
>>> import lib
>>> callable(lib)
True
>>> lib()
'foo!'
```