{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the no :- 5\n",
      "factorial isv :- 120\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "1--->Write a Python function to calculate the factorial of a number (a non-negative integer)\n",
    "ans->\n",
    "\n",
    "'''\n",
    "n=int(input(\"enter the no :- \"))\n",
    "def fac(no):\n",
    "    fac=1\n",
    "    while no>0:\n",
    "        fac=fac * no\n",
    "        no=no - 1\n",
    "    print(\"factorial isv :-\",fac)\n",
    "fac(no)"
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
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the no: 5\n",
      "5 is in the range\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "2--->Write a Python function to check whether a number is in a given range\n",
    "ans->\n",
    "\n",
    "'''\n",
    "n=int(input(\"enter the no: \"))\n",
    "def test_range(n):\n",
    "    if n in range(3,9):\n",
    "        print(\"%s is in the range\"%str(n))\n",
    "    else :\n",
    "        print(\"The number is outside the given range.\")\n",
    "test_range(n)\n"
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
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "3--->Write a Python function to check whether a number is perfect or not.\n",
    "ans->\n",
    "\n",
    "'''\n",
    "def perfect_number(n):\n",
    "    sum = 0\n",
    "    for x in range(1, n):\n",
    "        if n % x == 0:\n",
    "            sum += x\n",
    "            print(sum)\n",
    "    return sum == n\n",
    "print(perfect_number(2))\n"
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
      "True\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "4--->Write a Python function that checks whether a passed string is palindrome or not\n",
    "ans->\n",
    "\n",
    "'''\n",
    "def isPalindrome(string):\n",
    "    left_pos = 0\n",
    "    right_pos = len(string) - 1\n",
    "    \n",
    "    while right_pos >= left_pos:\n",
    "        if not string[left_pos] == string[right_pos]:\n",
    "            return False\n",
    "        left_pos += 1\n",
    "        right_pos -= 1\n",
    "    return True\n",
    "print(isPalindrome('aza')) \n"
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
    "5--->How do you perform pattern matching in Python? Explain.\n",
    "ans->Steps of Regular Expression Matching\n",
    "---->Import the regex module with import re.\n",
    "---->Create a Regex object with the re. compile() function. ...\n",
    "---->Pass the string you want to search into the Regex object's search() method. ...\n",
    "---->Call the Match object's group() method to return a string of the actual matched text.\n",
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
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "15\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "6--->What is lambda function in python?What we call a function which is incomplete version of a function?\n",
    "ans->A lambda function is a small anonymous function.\n",
    "     A lambda function can take any number of arguments, but can only have one expression.\n",
    "     The power of lambda is better shown when you use them as an anonymous function inside another function.\n",
    "---->Stub() is a simple but incomplete version of a function.\n",
    "'''\n",
    "#exammple\n",
    "x = lambda a : a + 10\n",
    "print(x(5))"
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
    "7--->How Many Basic Types Of Functions Are Available In Python?\n",
    "ans->There are three types of functions in Python: Built-in functions, \n",
    "     such as \n",
    "     help() to ask for help, \n",
    "     min() to get the minimum value, \n",
    "     print() to print an object to the terminal,… You can find an overview with more of these functions here.\n",
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
   "execution_count": 80,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "addition of a and b is: 10\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "8--->Write a Python program to access a function inside a function.\n",
    "ans->\n",
    "\n",
    "'''\n",
    "def add(a,b):\n",
    "    def sum():\n",
    "        c=a+b\n",
    "        print(\"addition of a and b is:\",c)\n",
    "    sum()\n",
    "add(5,5)\n",
    "        "
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
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "9--->Write a Python program to detect the number of local variables declared in a function.\n",
    "ans->We can use the co_nlocals() function which returns the number of local variables used by the\n",
    "     function to get the desired result.\n",
    "\n",
    "'''\n",
    "def fun(): \n",
    "    a = 2\n",
    "    str = 'GeeksForGeeks'\n",
    "print(fun.__code__.co_nlocals) "
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
    "10--->What is map function in Python?\n",
    "ans-->Python's map() is a built-in function that allows you to process and transform all the items in an iterable \n",
    "      without using an explicit for loop, a technique commonly known as mapping. map() is useful when you need to \n",
    "      apply a transformation function to each item in an iterable and transform them into a new iterable.\n",
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
    "11--->Does Python Have A Main() Method?\n",
    "ans-->Some programming languages have a special function called main() which is the execution point for a program file. \n",
    "      Python interpreter, however, runs each line serially from the top of the file and has no explicit main() function. \n",
    "      Python offers other conventions to define the execution point.\n",
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
   "execution_count": 81,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sum: 8\n",
      "Sum: 22\n",
      "Sum: 17\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "12--->What Does The *Args Do In Python?What Does The **Kwargs Do In Python?\n",
    "ans-->*args passes variable number of non-keyworded arguments list and on which operation of the list can be performed. \n",
    "      **kwargs passes variable number of keyword arguments dictionary to function on which operation of a dictionary can \n",
    "      be performed.\n",
    "\n",
    "'''\n",
    "def adder(*num):\n",
    "    sum = 0\n",
    "    \n",
    "    for n in num:\n",
    "        sum = sum + n\n",
    "\n",
    "    print(\"Sum:\",sum)\n",
    "\n",
    "adder(3,5)\n",
    "adder(4,5,6,7)\n",
    "adder(1,2,3,5,6)"
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
    "13--->What Does The Name Do In Python? What Is The Purpose Of “End” In Python?\n",
    "ans-->Python print end keyword\n",
    "      The end key of print function will set the string that needs to be appended when printing is done.\n",
    "      By default the end key is set by newline character. So after finishing printing all the variables, a newline \n",
    "      character is appended.\n",
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
    "14--->What Does The Len() Function Do In Python? What Does The Ord() Function Do In Python?\n",
    "ans-->\n",
    "Len() :-Python len() Function\n",
    "      The len() function returns the number of items in an object. When the object is a string, the len() function \n",
    "      returns the number of characters in the string.\n",
    "  \n",
    "ord() :-ord() function in Python\n",
    "      In Python, the ord() function accepts a string of unit length as an argument and returns the Unicode equivalence \n",
    "      of the passed argument.\n",
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
    "15--->Name few methods that are used to implement Functionally Oriented Programming in Python?\n",
    "ans-->'__init__' is used to initialize objects, '__str__' to format object for printing,\n",
    "      '__eq__' for equality operator,\n",
    "      '__len__' for len function, and many many others.\n",
    "      Suggest using the dir() function to explore how the builtin data types are put together. \n",
    "\n",
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
     "data": {
      "text/plain": [
       "'tahbarp'"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'''\n",
    "16--->Write a program in Python to reverse a string without using inbuilt function reverse string?\n",
    "ans-->\n",
    "\n",
    "'''\n",
    "def rev(str):\n",
    "    str=str[::-1]\n",
    "    return str\n",
    "rev('prabhat')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n"
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
   "version": "3.7.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
