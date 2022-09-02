{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    " \"\"\"\n",
    " \n",
    "1--->What is Python ,Name some of the features of Python.\n",
    "ans->Python is an interpreted, object-oriented, high-level programming language with\n",
    "     dynamic semantics.\n",
    "fetures:-\n",
    "->Its high-level built in data structures, combined with dynamic typing and dynamic\n",
    "  binding, make it very attractive for Rapid Application Development.\n",
    "->Python supports modules and packages, which encourages program modularity and\n",
    "  code reuse.\n",
    "->The Python interpreter and the extensive standard library are available in source or\n",
    "  binary form without charge for all major platforms, and can be freely distributed.\n",
    "  \n",
    " \"\"\""
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
      "what type Python version you are using?\n",
      "version 3.7.9\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "2--->Write a Python program to get the Python version you are using?\n",
    "ans->v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32\n",
    "exapmle->\n",
    "\n",
    "\"\"\"\n",
    "print(\"what type Python version you are using?\")\n",
    "print(\"version 3.7.9\")"
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
    "\"\"\"\n",
    "3--->Is python the right choice for Web based Programming?\n",
    "ans->Web development using Python has been very popular for years – and for all the right reasons. \n",
    "     Not only is it a perfect language for beginners but it can also serve you as stepping stone for \n",
    "     learning more complicated languages. Python web development is something every developer should give a try.\n",
    "\n",
    "\"\"\""
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
    "\"\"\"\n",
    "4--->Why was the language called as Python?\n",
    "ans->Why is it called Python? ¶ When he began implementing Python, Guido van Rossum was also \n",
    "     reading the published scripts from “Monty Python's Flying Circus”, a BBC comedy series from the 1970s. \n",
    "     Van Rossum thought he needed a name that was short, unique, and slightly mysterious, \n",
    "     so he decided to call the language Python.\n",
    "\n",
    "\"\"\""
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
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the no :- 5\n",
      "no is positive\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "5--->Write a Python program to check if a number is positive, negative or zero.\n",
    "ans->example given below.\n",
    "\n",
    "\"\"\"\n",
    "no=int(input(\"enter the no :- \"))\n",
    "\n",
    "if no>0:\n",
    "    print(\"no is positive\")\n",
    "else:\n",
    "    if no==0:\n",
    "        print(\"no is zero\")\n",
    "    else:\n",
    "        print(\"no is negative\")"
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
    "\"\"\"\n",
    "6--->What is the language from which Python has got its features or derived its features?\n",
    "ans->Python is derived from programming languages such as ABC, Modula 3, small talk, Algol-68. \n",
    "     Van Rossum picked the name Python for the new language from a TV show, Monty Python's Flying Circus.\n",
    "     Language paradigms: Object-oriented program...\n",
    "     Language designers: Guido van Rossum\n",
    "\n",
    "\n",
    "\"\"\""
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
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'str'>\n",
      "<class 'int'>\n",
      "True\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "7--->Write a Python program to check if variable is of integer or string.\n",
    "ans->given below\n",
    "\n",
    "\"\"\"\n",
    "#print(isinstance(25,int) or isinstance(25,str))\n",
    "#print(isinstance(25,int) or isinstance(25,str))\n",
    "#print(isinstance(\"25\",int) or isinstance(\"25\",str))\n",
    "\n",
    "name=\"prabhat\"\n",
    "age=12\n",
    "print(type(name))\n",
    "print(type(age))\n",
    "print(isinstance(name,str))\n",
    "print(isinstance(age,int))"
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
    "\"\"\"\n",
    "8--->Does python support switch or case statement in Python?If not what is the reason for the same?\n",
    "ans->Python does not have a simple switch case construct. Coming from a Java or C++ background,\n",
    "     you may find this to be a bit odd. But Python does not have this. So, to get around this, \n",
    "     we use Python's built-in dictionary construct to implement cases and decided what to do when a case is met.\n",
    "---->Python doesn't have a switch/case statement because of Unsatisfactory Proposals . ... \n",
    "     Most programming languages have switch/case because they don't have proper mapping \n",
    "     constructs. You cannot map a value to a function, that's why they have it.\n",
    "\"\"\""
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
    "\"\"\"\n",
    "9--->How Python is interpreted?\n",
    "ans->Python is an “interpreted” language. This means it uses an interpreter. \n",
    "     An interpreter is very different from the compiler. An interpreter executes the statements of \n",
    "     code “one-by-one” whereas the compiler executes the code entirely and lists all possible errors at a time.\n",
    "\"\"\""
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
      "Enter a number: 5\n",
      "Factorial of 5 is 120\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "10-->Write a Python program to get the Factorial number of given number\n",
    "ans->\n",
    "\"\"\"\n",
    " \n",
    "num = int(input(\"Enter a number: \"))\n",
    "if num < 0: \n",
    "    print(0)\n",
    "elif num == 0 or num == 1:\n",
    "    print(1)\n",
    "else: \n",
    "    fac=1\n",
    "    for i in range(1,num+1):\n",
    "        fac = fac * i    \n",
    "    print(\"Factorial of\",num,\"is\",fac)"
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
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the value of 'n': 10\n",
      "Fibonacci Series:  0 1 1 2 3 5 8 13 21 34 "
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "11-->Write a Python program to get the Fibonacci series of given range\n",
    "ans->given below.\n",
    "\n",
    "\"\"\"\n",
    "n = int(input(\"Enter the value of 'n': \"))\n",
    "a = 0\n",
    "b = 1\n",
    "sum = 0\n",
    "count = 1\n",
    "print(\"Fibonacci Series: \", end = \" \")\n",
    "while(count <= n):\n",
    "    print(sum, end = \" \")\n",
    "    count += 1\n",
    "    a = b\n",
    "    b = sum\n",
    "    sum = a + b"
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
    "\"\"\"\n",
    "12-->How memory is managed in Python?\n",
    "ans->Instead of storing values in the memory space reserved by the variable, Python has the variable \n",
    "     refer to the value. Similar to pointers in C, variables in Python refer to values (or objects) stored \n",
    "     somewhere in memory.\n",
    "    \n",
    "---->The Python memory manager manages chunks of memory called “Blocks”. A collection of blocks of the same\n",
    "     size makes up the “Pool”. Pools are created on Arenas, chunks of 256kB memory allocated on heap=64 pools.\n",
    "     If the objects get destroyed, the memory manager fills this space with a new object of the same size.\n",
    "\n",
    "\"\"\""
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
    "\"\"\"\n",
    "13-->13.What is namespace in Python?\n",
    "ans->A namespace in Python is a collection of underlying keywords and objects that Python has within memory.\n",
    "     It's a very common concept in Object-Oriented Programming. In Python, a namespace is\n",
    "     a key-value pair implemented as a Dictionary.\n",
    "\n",
    "\"\"\""
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
    "\"\"\"\n",
    "14-->What is the purpose continue statement in python?\n",
    "ans->The continue keyword is used to end the current iteration in a for loop (or a while loop), \n",
    "     and continues to the next iteration.\n",
    "\"\"\""
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
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1)..without using temp variable\n",
      "enter the value of a:- 10\n",
      "enter the value of b:- 20\n",
      "B:- 10\n",
      "A:- 20 \n",
      "\n",
      "2)..with using temp variable\n",
      "enter the value of a:- 5\n",
      "enter the value of b:- 6\n",
      "A:- 6 \n",
      "B:- 5\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "15-->Write python program that swap two number with temp variable and\n",
    "without temp variable\n",
    "ans->given below.\n",
    "\n",
    "\"\"\"\n",
    "#without temp variable\n",
    "print(\"1)..without using temp variable\")\n",
    "a=int(input(\"enter the value of a:- \"))\n",
    "b=int(input(\"enter the value of b:- \"))\n",
    "\n",
    "a=a+b \n",
    "\n",
    "b=a-b\n",
    "print(\"B:-\",b)\n",
    "\n",
    "a=a-b\n",
    "print(\"A:-\",a,\"\\n\")\n",
    "\n",
    "#with temp variable\n",
    "print(\"2)..with using temp variable\")\n",
    "a=int(input(\"enter the value of a:- \"))\n",
    "b=int(input(\"enter the value of b:- \"))\n",
    "\n",
    "temp=a\n",
    "a=b\n",
    "b=temp\n",
    "\n",
    "print(\"A:-\",a,\"\\nB:-\",b)\n"
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
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the no :- 2\n",
      "even\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "16-->Write a Python program to find whether a given number is even or odd,print out an appropriate message to the user.\n",
    "ans->given below.\n",
    "\n",
    "\"\"\"\n",
    "no=int(input(\"enter the no :- \"))\n",
    "if no%2==0:\n",
    "    print(\"even\")\n",
    "else:\n",
    "    print(\"odd\")"
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
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the value h :- 5\n",
      "enter the value b :- 6\n",
      "area of circle    :- 15\n",
      "\n",
      "\n",
      "enter the value r :- 5\n",
      "area of circle :-  78.5\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "17-->Write a Python program that compute the area of following 1)Triangle (accepts base and height) 2)Circle (accept radius)\n",
    "ans->given below.\n",
    "\n",
    "\"\"\"\n",
    "#1)...area of tringle\n",
    "\n",
    "h=int(input(\"enter the value h :- \"))\n",
    "b=int(input(\"enter the value b :- \"))\n",
    "x=1/2\n",
    "ans=x*h*b\n",
    "print(\"area of circle    :-\",int(ans))\n",
    "print(\"\\n\")\n",
    "\n",
    "#2)...area of circle\n",
    "pi=float(3.14)\n",
    "\n",
    "r=int(input(\"enter the value r :- \"))\n",
    "ans=pi*r*r\n",
    "print(\"area of circle :- \",ans)"
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
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please Enter Your Own Character : x\n",
      "The Given Character x is a Consonant\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "18-->Write a Python program to test whether a passed letter is a vowel or not\n",
    "ans->given beow.\n",
    "\n",
    "\"\"\"\n",
    "# Python Program to check character is Vowel or Consonant\n",
    "ch = input(\"Please Enter Your Own Character : \")\n",
    "\n",
    "if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A'\n",
    "       or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):\n",
    "    print(\"The Given Character\", ch, \"is a Vowel\")\n",
    "else:\n",
    "    print(\"The Given Character\", ch, \"is a Consonant\")"
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
      "enter the value p :- 5\n",
      "enter the value r :- 15\n",
      "enter the value t :- 1\n",
      "intrest :-  0.75\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "19-->Write a Python program to compute the value of a specified principal amount, rate of interest, and a number of years\n",
    "ans->given below.\n",
    "\n",
    "\"\"\"\n",
    "p=int(input(\"enter the value p :- \"))\n",
    "r=int(input(\"enter the value r :- \"))\n",
    "t=int(input(\"enter the value t :- \"))\n",
    "ans=p*r*t/100\n",
    "print(\"simple intrest :- \",ans)\n",
    "\n"
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
    "\"\"\"\n",
    "20-->What are the tools that help to find bugs or perform static analysis?\n",
    "ans->Pychecker and Pylint are the static analysis tools that help to find bugs in python. \n",
    "     Pychecker is an opensource tool for static analysis that detects the bugs from source code and warns \n",
    "     about the style and complexity of the bug.\n",
    "\n",
    "\"\"\""
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
    "\"\"\"\n",
    "21-->What are Python decorators?\n",
    "ans->A decorator is a design pattern in Python that allows a user to add new functionality to an existing \n",
    "     object without modifying its structure. Decorators are usually called before the definition of a \n",
    "     function you want to decorate.\n",
    "\n",
    "\"\"\""
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
    "\"\"\"\n",
    "22-->What is PEP 8?\n",
    "ans->PEP 8, sometimes spelled PEP8 or PEP-8, is a document that provides guidelines and best practices\n",
    "     on how to write Python code. ... The primary focus of PEP 8 is to improve the readability and consistency \n",
    "     of Python code. PEP stands for Python Enhancement Proposal, and there are several of them.\n",
    "\n",
    "\"\"\""
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
      "Input first number: 55\n",
      "Input second number: 12\n",
      "Input third number: 69\n",
      "Numbers in sorted order:  12 55 69\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "23-->Write a Python program to sort three integers withoutusing conditional statements andloops.\n",
    "ans->given below.\n",
    "\"\"\"\n",
    "x = int(input(\"Input first number: \"))\n",
    "y = int(input(\"Input second number: \"))\n",
    "z = int(input(\"Input third number: \"))\n",
    "a1 = min(x, y, z)\n",
    "a3 = max(x, y, z)\n",
    "a2 = (x + y + z) - a1 - a3\n",
    "print(\"Numbers in sorted order: \", a1, a2, a3)"
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
    "\"\"\"\n",
    "24-->Write a Python program that accepts an integer (n) and computes the valueof n+nn+nnn.\n",
    "ans->given below.\n",
    "\"\"\"\n",
    "a = int(input(\"Input an integer : \"))\n",
    "n1 = int( \"%s\" % a )\n",
    "n2 = int( \"%s%s\" % (a,a) )\n",
    "n3 = int( \"%s%s%s\" % (a,a,a) )\n",
    "print (n1+n2+n3)"
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
      "enter the 1st value:- 5\n",
      "enter the 2nd value:- 6\n",
      "enter the 3rd value:- 5\n",
      "zero\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "25-->Write a Python program to sum of three givenintegers.However, if two values are equal sum will bezero.\n",
    "ans->given below.\n",
    "\"\"\"\n",
    "a=int(input(\"enter the 1st value:- \"))\n",
    "b=int(input(\"enter the 2nd value:- \"))\n",
    "c=int(input(\"enter the 3rd value:- \"))\n",
    "\n",
    "if a==b==c:\n",
    "    print(a+b+c) \n",
    "elif a==b or b==c or c==a:\n",
    "    print('zero')\n",
    "else:\n",
    "    print(a+b+c)    "
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
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the 1st value:- 3\n",
      "enter the 2nd value:- 2\n",
      "true\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "26-->Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.\n",
    "ans->given below.\n",
    "\"\"\"\n",
    "n1=int(input(\"enter the 1st value:- \"))\n",
    "n2=int(input(\"enter the 2nd value:- \"))\n",
    "if n1==n2 or n1+n2==5 or n1-n2==5:\n",
    "    print(\"true\")\n",
    "else:\n",
    "    print(\"false\")"
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
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Input a number: 8\n",
      "36.0\n",
      "8\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "27-->Write a python program to sum of the first n positive integers\n",
    "ans->given below.\n",
    "\"\"\"\n",
    "n = int(input(\"Input a number: \"))\n",
    "sum_num = (n * (n + 1)) / 2\n",
    "print(sum_num)"
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
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
