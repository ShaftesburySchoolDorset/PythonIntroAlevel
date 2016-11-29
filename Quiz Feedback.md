# Feedback - Real World Problems: Quiz

## Anne

- Don't forget to include comments in your code explaining what certain sections, like methods, do.
- Keep your code segmented; so classes should be at the top, followed by any other functions, and then any other code, like initialising your methods, at the bottom. This makes it easier to read.
- Line 4: move your score variable to inside the `__init__` method.
- Line 17: You can't have predfined quiz questions, I would like your program to generate the questions 'on the fly' (while it's running).

## Ben

- Lines 8, 9: Don't use name 'func' for variables. It is a 'reserved' word and does something else in python. Try and think of a different name for this variable.
- Lines 4, 5, 6: As you're using a class you don't need global variables. Re-write them in the `__init__` method as below. They will still be available throughout the class.
```python
self.score = 0 # already done
self.answer = ""
self.func = func # already done
```
- Lines 21-39: Your answer function is not very efficient as it has quite a lot of repeated code. Is there any way you can make this better with less lines of code?
- Line 18: You are already using the name `question` for the method name. Either rename the method or the variable.

## Isaac

- Line 10: method names should be lower case, this is to differentiate them from classes.
- Good code at the moment, the only thing to bear in mind is that your `Quiz` class will only work for 1 question, you need to ask several questions. Consider renaming your classes and moving some of the logic to other classes.

## Leo

- Line 5, 6, 13 I guess `name` and `classname` are variables you want to use throughout your class? Consider prefixing them with `self.` so `self.name` instead.
- Line 16: method names should be lower case, this is to differentiate them from classes.

## Simon

- Line 3, 30: Class names should use CamelCase
- Line 33: Add a space before the method to make the code easier to read
- Line 39: Variables should be in lower case
- Line 39: If you are trying to create a new instance of the `generator` class then you should end it with '()' so `quiz = generator()`

##  Zach

No comments