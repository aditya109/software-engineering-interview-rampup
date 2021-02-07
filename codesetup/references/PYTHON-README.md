# Steps to run example codebase in <img src="https://cdn.svgporn.com/logos/python.svg" height="50"/> 

> The Python implementation of a particular problem is written such that the code can be freely tested amongst numerous test cases.

To run a particular code implementation in `.NET` for a particular problem set, navigate to the specific problem set.  

Let's say the problem set is `max_sum_of_contingous_subarray_of_size_n` under `sliding-window`.

So we navigate to `grokking-the-coding-interview` > `sliding-window` > `max_sum_of_contingous_subarray_of_size_n` > `python` > `MainApp`.

For `C#`, you could either use `Visual Studio` or any text editor of your choice. I am using `VS Code` for demonstration.

## Repository Explanation

1. The directory structure visible would be something like this:

   ```powershell
   MainApp
   ├───app
   │   ├───__init__.py
   │   └───mainApp.py
   └───testMainApp.py
   ```

2. `mainApp.py` is the program where actual code resides. The main code resides within `run()`.

   ```c#
   class MainApp:
       def __init__(self):
           pass
   
       ''' Problem Statement goes here...
       '''
   
       def run(self, arr, k):
           ''' 
           code goes here
           '''
           return 0
   ```

3. `testMainApp.py` is the program where unit tests reside.

   ```c#
   from unittest.case import expectedFailure
   from mainApp import MainApp
   import unittest
   
   class TestMainApp(unittest.TestCase):
   
       def setUp(self):
           self._arguments = [
               {
                   'arr': [4, 2, 1, 7, 8, 1, 2, 8, 1, 0],
                   'k': 3,
                   'expectedResult': 16
               },
               {
                   'arr': [4, 2, 1, 7, 8, 1, 2, 8, 1, 0],
                   'k': 4,
                   'expectedResult': 19
               },
               {
                   'arr': [4, 2, 1, 7, 8, 1, 2, 8, 1, 0],
                   'k': 5,
                   'expectedResult': 26
               },
               {
                   'arr': [4, 2, 1, 7, 8, 8, 1, 0],
                   'k': 3,
                   'expectedResult': 23
               },
           ]
           self._mainAppInstance = MainApp()
   
       def test_run(self):
           for argument in self._arguments:
               actualResult = self._mainAppInstance.run(argument['arr'], argument['k'])
               self.assertEqual(actualResult, argument['expectedResult'])
   ```

## Steps for `VS Code` users:

1. Open the `MainApp` in `VS Code`.

2. Open `Powershell Terminal`.

   ```powershell
   🐳 :: MainApp » python -m unittest testMainApp
   .
   ----------------------------------------------------------------------
   Ran 1 test in 0.000s
   
   OK
   ```

