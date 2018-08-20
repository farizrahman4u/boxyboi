# boxyboi
Boxing primitives in python

------


Boxyboi lets you bind (not really) attributes to primitives like strings and integers while preserving their natural behaviour.


## Example

```python
from boxyboi import box

dude = box('Abin Simon')
dude.age = 22
dude.github = 'github.com/meain'

print(dude)  # >>> 'Abin Simon'

# `dude` behaves like a `str`:
print(dude.lower())  # >>> `abin simon`
print(len(dude))  # >>> 10
print(dude.split(' '))  # >>> ['Abin', 'Simon']

```
