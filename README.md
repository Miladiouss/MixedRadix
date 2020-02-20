# MixedRadix
Modular arithmatic in Python. 
This is a Python package for handling mixed radix number system (non-constant base), their representation, and basic arithmetics.

The most commonly used example  of mixed radix numbers is representation of week day, hours, minutes, and seconds. The radix for this system is `[7, 24, 60, 60]`. Visit [this Wikipedia page](https://en.wikipedia.org/wiki/Mixed_radix) to learn more about mixed radix number systems.
## How to use?
1. Download this repository to your desired directory (`<MixedRadix_dir>`).
2. Add the following to your Python code to import it locally:
```Python
import sys
sys.path.append(<MixedRadix_dir>)
from MixedRadix import MixedRadix
```
No package dependencies. Written in Python 3.

## Why Mixed Radix?
Mixed radix numbers systems are specially useful in computing. A useful (not necessary the most common) application of mixed numbers in computer science is listing all the possible paths in a list of lists. Consider a list with the following lists as its elements:

```
A = [
        ['00', '01', '02'],
        ['10', '11'],
        ['20', '21', '22'],
        ['30'],
        ['40', '41']
    ]
```

Let's select an element from each row. `['01', '10', '22', '30', '40']` is one option (or path) out of 3x2x3x1x2 = 36 possible paths. A more systematic way of extracting paths is by using mixed radix number systems. The radix corresponding to the above is `[3, 2, 3, 1, 2]`. Now, in order to print all the possible paths, we first use a for loop to extract the length of each row and set that to the radix of a `MixedRadix` object initialized at 0. Looping over all the possible path indices by increasing its value by 1 will result in generating all the possible paths. The list of digits of this number are equivalent to the index representation of a path. A path can be used to extract all the elements of `A` corresponding to that path (see the example below). In my opinion this is a simple and elegant solution for walking over the space of all possible paths, especially if the number of rows and length of each one can vary from run to run and a tagging mechanism is needed. MixedRadix represents `digits` and `radix` in reverse over as well (`digitsR` and `radixR`); this could be useful if you want to vary the path from the base (root), rather than the tail (leaf) (see `MixedRadix` docstring).

```Python
# Construct a mixed radix number object
radix = []
for a in A:
    radix.append( len(a) )

tag = MixedRadix(value=0, radix=radix)
print('Radix:', tag.radix, '\n')
print('Tag Index |       Path Index      |                  Path             ')
# Loop over all possible path indecies
for i in range(tag.maxVal):
    print('   {:6} :   {}'.format(str(tag), tag.digits), end='     :     ')
    # Walk through the path in space of A
    path = []
    for row, clm in enumerate(tag.digits):
        path.append( A[row][clm] )
    print(path)
    # Go to the next path index
    tag += 1
```

Output:
```
Radix: [3, 2, 3, 1, 2] 

Tag Index |       Path Index      |                  Path             
    0     :   [0, 0, 0, 0, 0]     :     ['00', '10', '20', '30', '40']
   +1     :   [0, 0, 0, 0, 1]     :     ['00', '10', '20', '30', '41']
   +2     :   [0, 0, 1, 0, 0]     :     ['00', '10', '21', '30', '40']
   +3     :   [0, 0, 1, 0, 1]     :     ['00', '10', '21', '30', '41']
   +4     :   [0, 0, 2, 0, 0]     :     ['00', '10', '22', '30', '40']
   +5     :   [0, 0, 2, 0, 1]     :     ['00', '10', '22', '30', '41']
   +6     :   [0, 1, 0, 0, 0]     :     ['00', '11', '20', '30', '40']
   +7     :   [0, 1, 0, 0, 1]     :     ['00', '11', '20', '30', '41']
   +8     :   [0, 1, 1, 0, 0]     :     ['00', '11', '21', '30', '40']
   +9     :   [0, 1, 1, 0, 1]     :     ['00', '11', '21', '30', '41']
   +10    :   [0, 1, 2, 0, 0]     :     ['00', '11', '22', '30', '40']
   +11    :   [0, 1, 2, 0, 1]     :     ['00', '11', '22', '30', '41']
   +12    :   [1, 0, 0, 0, 0]     :     ['01', '10', '20', '30', '40']
   +13    :   [1, 0, 0, 0, 1]     :     ['01', '10', '20', '30', '41']
   +14    :   [1, 0, 1, 0, 0]     :     ['01', '10', '21', '30', '40']
   +15    :   [1, 0, 1, 0, 1]     :     ['01', '10', '21', '30', '41']
   +16    :   [1, 0, 2, 0, 0]     :     ['01', '10', '22', '30', '40']
   +17    :   [1, 0, 2, 0, 1]     :     ['01', '10', '22', '30', '41']
   +18    :   [1, 1, 0, 0, 0]     :     ['01', '11', '20', '30', '40']
   +19    :   [1, 1, 0, 0, 1]     :     ['01', '11', '20', '30', '41']
   +20    :   [1, 1, 1, 0, 0]     :     ['01', '11', '21', '30', '40']
   +21    :   [1, 1, 1, 0, 1]     :     ['01', '11', '21', '30', '41']
   +22    :   [1, 1, 2, 0, 0]     :     ['01', '11', '22', '30', '40']
   +23    :   [1, 1, 2, 0, 1]     :     ['01', '11', '22', '30', '41']
   +24    :   [2, 0, 0, 0, 0]     :     ['02', '10', '20', '30', '40']
   +25    :   [2, 0, 0, 0, 1]     :     ['02', '10', '20', '30', '41']
   +26    :   [2, 0, 1, 0, 0]     :     ['02', '10', '21', '30', '40']
   +27    :   [2, 0, 1, 0, 1]     :     ['02', '10', '21', '30', '41']
   +28    :   [2, 0, 2, 0, 0]     :     ['02', '10', '22', '30', '40']
   +29    :   [2, 0, 2, 0, 1]     :     ['02', '10', '22', '30', '41']
   +30    :   [2, 1, 0, 0, 0]     :     ['02', '11', '20', '30', '40']
   +31    :   [2, 1, 0, 0, 1]     :     ['02', '11', '20', '30', '41']
   +32    :   [2, 1, 1, 0, 0]     :     ['02', '11', '21', '30', '40']
   +33    :   [2, 1, 1, 0, 1]     :     ['02', '11', '21', '30', '41']
   +34    :   [2, 1, 2, 0, 0]     :     ['02', '11', '22', '30', '40']
   +35    :   [2, 1, 2, 0, 1]     :     ['02', '11', '22', '30', '41']
```
## Circular Numbers
Another useful feature of MixedRadix is its capability to behave modularly. By setting `overflowMethod` to `modular`, if the value of the number increases beyond what can be represented using the radix, it will loop around in a modular fashion. 

## Feedback and Contact
I would appreciate improvements, comments, and feedbacks ( my github username @ gmail.com). Thanks!
