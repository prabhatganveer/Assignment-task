{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "1--->Explain Exception handling? What is an Error in Python?\n",
    "ans->Exception handling is an important concept in python to run your code smoothly without \n",
    "     interruption of errors. In this article we will see how the try-except block works to avoid \n",
    "     exceptions/errors and run code smoothly. We will also see how to raise an error/exception and \n",
    "     how to handle it.\n",
    "     \n",
    "error->In Python, exceptions can be handled using a try statement. The critical operation which can \n",
    "     raise an exception is placed inside the try clause. The code that handles the exceptions is \n",
    "     written in the except clause. We can thus choose what operations to perform once we have caught \n",
    "     the exception.\n",
    "\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "2--->How many except statements can a try-except blockhave?\n",
    "     Name Some built-in exception classes:\n",
    "ans->1.There has to be at least one except statement. \n",
    "     2.When will the else part of try-except-else be executed? \n",
    "     3.The else part is executed when no exception occurs.\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "3--->When will the else part of try-except-else be executed?\n",
    "ans->The else part is executed when no exception occurs.\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "4--->Can one block of except statements handle multiple exception?\n",
    "ans->Each type of exception can be specified directly. There is no need to put it in a list.\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "5-->When is the finally block executed?\n",
    "ans->The finally block always executes when the try block exits. This ensures that the \n",
    "     finally block is executed even if an unexpected exception occurs.\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "6--->What happens when „1‟ == 1 is executed?\n",
    "ans->we get a false.\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "7--->How Do You Handle Exceptions With Try/Except/Finally In Python? exaplin with coding snippets\n",
    "ans->If the Python program contains suspicious code that may throw the exception, we must place that \n",
    "     code in the try block. The try block must be followed with the except statement, which contains \n",
    "     a block of code that will be executed if there is some exception in the try block.\n",
    "     \n",
    "---->Snippet is a programming term for a small region of re-usable source code, machine code, or text.\n",
    "     Ordinarily, these are formally defined operative units to incorporate into larger programming \n",
    "     modules.\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the no: 2\n"
     ]
    },
    {
     "ename": "EvenNumberError",
     "evalue": "enter no is even",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mEvenNumberError\u001b[0m                           Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-23-c19413990c18>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     10\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"no is odd\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     11\u001b[0m \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 12\u001b[1;33m     \u001b[1;32mraise\u001b[0m \u001b[0mEvenNumberError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"enter no is even\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mEvenNumberError\u001b[0m: enter no is even"
     ]
    }
   ],
   "source": [
    "'''\n",
    "8--->write python program that user to enter only odd numbers, else will raise an exception.\n",
    "ans->\n",
    "'''\n",
    "class EvenNumberError(Exception):\n",
    "    pass\n",
    "\n",
    "no=int(input(\"enter the no: \"))\n",
    "if no%2!=0:\n",
    "    print(\"no is odd\")\n",
    "else:\n",
    "    raise EvenNumberError(\"enter no is even\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "0\n",
      "Exception\n",
      "bye\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "9--->write program for Catching Specific Exceptions in Python\n",
    "ans->\n",
    "'''\n",
    "try:\n",
    "    a=int(input())\n",
    "    b=int(input())\n",
    "    c=a/b\n",
    "    print(c)\n",
    "except ZeroDivisionError:\n",
    "    print(\"Exception\")\n",
    "print('bye')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Exception cought: not readable\n",
      "finally block\n",
      "bye\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "10--->write python program for file operations to makes sure the file is closed\n",
    "      even if an exception occurs.\n",
    "ans->\n",
    "'''\n",
    "\n",
    "try:\n",
    "    file=open(\"album.txt\",'a')\n",
    "    a=\"prabhat\"\n",
    "    file.read()\n",
    "    print('data append')\n",
    "except Exception as e:\n",
    "    print('Exception cought:',e)\n",
    "    file.close()\n",
    "finally:\n",
    "    print('finally block')\n",
    "print('bye')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "11--->Explain Python Errors and Built-in Exceptions with coding snippets\n",
    "ans->Errors are the problems in a program due to which the program will stop the execution.\n",
    "     On the other hand, exceptions are raised when the some internal events occur which changes \n",
    "     the normal flow of the program.\n",
    "   ->We can handle these built-in and user-defined exceptions in Python using try , \n",
    "     except and finally statements.\n",
    "   ->Snippet is a programming term for a small region of re-usable source code, machine code, or text.\n",
    "     Snippet management is a feature of some text editors, program source code editors, IDEs, and \n",
    "     related software. It allows the user to avoid repetitive typing in the course of routine edit \n",
    "     operations.\n",
    "'''\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A New Exception occured:  6\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "12--->Explain User-Defined Exception in Python\n",
    "ans->Programmers may name their own exceptions by creating a new exception class. Exceptions need \n",
    "     to be derived from the Exception class, either directly or indirectly. Although not mandatory, \n",
    "     most of the exceptions are named as names that end in “Error” similar to naming of the standard \n",
    "     exceptions in python\n",
    "'''\n",
    "# A python program to create user-defined exception \n",
    "  \n",
    "# class MyError is derived from super class Exception \n",
    "class MyError(Exception): \n",
    "  \n",
    "    # Constructor or Initializer \n",
    "    def __init__(self, value): \n",
    "        self.value = value \n",
    "  \n",
    "    # __str__ is to print() the value \n",
    "    def __str__(self): \n",
    "        return(repr(self.value))   \n",
    "try: \n",
    "    raise(MyError(3*2)) \n",
    "  # Value of Exception is stored in error \n",
    "except MyError as error: \n",
    "    print('A New Exception occured: ',error.value)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the no:2\n",
      "no is incorrect\n",
      "enter the no:55\n",
      "your guess is correct\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "13--->write program that will ask the user to enter a number until they guess a stored number correctly.\n",
    "ans->\n",
    "'''\n",
    "a = ['11','22','55','44','33','66','77']\n",
    "while True:\n",
    "    no=input(\"enter the no:\")\n",
    "    if no in a:\n",
    "        print(\"your guess is correct\")\n",
    "        break\n",
    "    else:\n",
    "        print(\"no is incorrect\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter a value in kelvin5\n",
      "-450.67\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "14--->What is Assertions in Python? Write function that converts a temperature from degrees \n",
    "       Kelvin to degrees Fahrenheit.\n",
    "ans->\n",
    "'''\n",
    "a=int(input('enter a value in kelvin'))\n",
    "print(((a*9)/5)-459.67)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "error\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "15--->Write program that except Clause with No Exceptions\n",
    "ans->\n",
    "'''\n",
    "try:\n",
    "    print('k'+7)\n",
    "except:\n",
    "    print('error')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "16--->What is Argument of an Exception?Explain with coding snippets\n",
    "ans->If you write the code to handle a single exception, you can have a variable follow the  \n",
    "    name of the exception in the except statement. ... The variable can receive a single value or \n",
    "    multiple values in the form of a tuple.\n",
    "'''"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
