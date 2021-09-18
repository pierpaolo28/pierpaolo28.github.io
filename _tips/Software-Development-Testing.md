---
layout: post
date: 2021-09-18
---

# Software Development Testing

## Introduction
When writing simple programs, it can be quite straightforward to understand how the code works and what should be the expected outputs. Although, as the complexity of a program increases it then becomes much more difficult to understand if the program is actually doing what we expect it to do or if for some particular cases it misbehaves and returns a wrong result (bugs).

> Software Testing is the process of evaluating computer code to determine whether or not it does what you expect it to do.

## Testing Techniques

Testing techniques can typically be divided into 2 main key categories:
- **Manual Testing:** we create a piece of code and we manually run it multiple times using different input parameters to test different possible scenarios and the resulting outputs.
- **Automated Testing:** the goal of automated testing is to automate the process of checking if the results returned by a programme, can match or not our expectations (we write code to test the code we had previously written). In order to check if our programme is correctly working, different **test cases** needs to be designed (input scenarios covering all the different combinations our programme logic should be able to handle). Using automated testing we can then test our code anytime we make any change in the codebase and just wait to see if our updated programme passed all the tests or not (and if not, quickly identify what went wrong to finally design a solution). When creating test cases it is important to try to consider and cover all the possible **edge cases** (inputs to our code that produce unexpected results and are found at the extreme ends of the ranges of input we imagine our programs should be able to work with).

Some examples of automated testing techniques are:
- **Unit Tests:** are used to verify that small, isolated parts of a programme are correct (e.g. functions, classes). It is important to make sure that the portion of code we are testing is really isolated by the rest of the programme so that to avoid having any problem of consistency of the output. Unittest is one of the most common libraries available for Python in order to design this kind of tests.
- **Integration Tests:** verify that the interaction between different pieces of code are working the way we expect them to (we check if when combining different parts of a system, everything still works). When running these kind of tests it might then be necessary to execute them in a separate environment (a testing environment rather than the actual production environment) in order to avoid any possibly disruption in our customer/consumer facing service.
- **Test Driven Development:** this methodology focuses on trying to fist create a series of tests we want our program to be able to pass and then actually start on creating the program itself (we code first the tests and then the program).

Additional examples of testing techniques are: Regression Testing (checking if a bug has been correctly fixed), Smoke Tests (checking essential things about our program, e.g. is our program even able to run at all?), Load Tests (checking if our program is able to scale as more people uses it), etc..

Finally, when deciding how to create our test cases (used in any testing technique) to check if our code is working as expected, there are 2 main approaches we can take:
- **White-box testing:** relies on the test creator's knowledge of the software being tested to construct the test cases (e.g. a developer creates some code and then knowing what the code should be able to do or not, creates some tests to check).
- **Black-box testing:** written with an awareness of what the program is supposed to do (such as its planned requirements/specifications) but the tests creator has no inside knowledge of how the program works behind the scenes (e.g. someone else writes a programme, tells you what you can do with it and asks you to check if you are able to do everything you need with it).

In order to create good software developments habits, testing is typically used in conjunction with Version Control tools (e.g. git) and continuous integration techniques.

## Resources and References
- [Testing Python for Beginners](https://www.youtube.com/watch?v=x_N4qAFsCrs)
