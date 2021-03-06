## Javascript - Objects, Scopes and Closures

> Learning Objectives
 - At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
 - Why Javascript programming is amazing (don’t forget to tweet today, with the hashtag #javascriptisamazing :))
 - How to create an object in Javascript
 - What this means
 - What undefined means
 - Why the variable type and scope is important
 - What is a closure
 - What is a prototype
 - How to inherit an object from another

 > Tasks

- Write an empty class Rectangle that defines a rectangle: You must use the class notation for defining your class
- The constructor must take 2 arguments w and h, Initialize the instance attribute width with the value of w, Initialize the instance attribute height with the value of h
- If w or h is equal to 0 or not a positive integer, create an empty object
- Create an instance method called print() that prints the rectangle using the character X
- Create an instance method called rotate() that exchanges the width and the height of the rectangle, Create an instance method called double() that multiples the width and the height of the rectangle by 2
- Write a class Square that defines a square and inherits from Rectangle of 4-rectangle.js: You must use the class notation for defining your class and extends, The constructor must take 1 argument: size, The constructor of Rectangle must be called (by using super())
- Create an instance method called charPrint(c) that prints the rectangle using the character c, If c is undefined, use the character X
- Write a function that returns the number of occurrences in a list: Prototype: exports.nbOccurences = function (list, searchElement)
- Write a function that returns the reversed version of a list: Prototype: exports.esrever = function (list), You are not allow to use the built-in method reverse
- Write a function that prints the number of arguments already printed and the new argument value. (see example below), Prototype: exports.logMe
- Write a function that converts a number from base 10 to another base passed as argument: Prototype: exports.converter = function (base), You are not allowed to import any file, You are not allowed to declare any new variable (var, let, etc..)
