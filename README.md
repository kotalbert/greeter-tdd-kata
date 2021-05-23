# Greeter

All tests should always pass, regardless of environment conditions.

1. Write a `Greeter` class with `greet` function that receives a `name` as input and outputs `Hello <name>`. The signature of `greet` should not change throughout the kata. You are allowed to construct `Greeter` object as you please.
2. `greet` trims the input
3. `greet` capitalizes the first letter of the name
4. `greet` returns `Good morning <name>` when the time is 06:00-12:00
5. `greet` returns `Good evening <name>` when the time is 18:00-22:00
6. `greet` returns `Good night <name>` when the time is 22:00-06:00
7. `greet` logs into console each time it is called

source: https://github.com/wix/tdd-katas

# Lessons Learned:

1. You should write more than minimal test in RED phase.
2. Comprehensive tests, covering more than trivial example should be written in early phase. 
3. Specification can be inferred from well-defined tests.
4. Test should cover edge cases.
