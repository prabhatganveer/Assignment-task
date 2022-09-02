{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'\\n1--->What is tuple?Difference between list and tuple\\nans->given below\\n\\n'"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'''\n",
    "1--->What is tuple?Difference between list and tuple\n",
    "ans->gilistel ow\n",
    " \n",
    "tuple()->\n",
    "- In the tuple definition, we used parenthesis ()\n",
    "- tuples are immutable\n",
    "-we cannot change/modify the values of a tuple.\n",
    "-we can use tuples as dictionary keys if needed.\n",
    "-syntex :- names = (\"Nicholas\", \"Michelle\", \"Alex\")\n",
    "\n",
    "list() ->\n",
    "-while in the list definition, we used square brackets [].\n",
    "-Lists are mutable \n",
    "-we can change/modify the values of a list\n",
    "-we can't use a list as a key in a dictionary\n",
    "-syntex :- names = [\"Nicholas\", \"Michelle\", \"Alex\"]\n",
    "\n",
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
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('tuple', False, 3.2, 1)\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "2--->Write a Python program to create a tuple with different datatypes\n",
    "ans->given below\n",
    "\n",
    "'''\n",
    "tuplex = (\"tuple\", False, 3.2, 1)\n",
    "print(tuplex)"
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
      "(5, 10, 15, 20, 25)\n",
      "(5,)\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "3--->Write a Python program to create a tuple with numbers\n",
    "ans->given below\n",
    "\n",
    "'''\n",
    "#Create a tuple with numbers\n",
    "tuplex =( 5, 10, 15, 20, 25)\n",
    "print(tuplex)\n",
    "#Create a tuple of one item\n",
    "tuplex =( 5,)\n",
    "print(tuplex)\n"
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
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "abcxyzpqr11.1\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "4--->Write a Python program to convert a tuple to a string\n",
    "ans->given below\n",
    "\n",
    "'''\n",
    "\n",
    "tuplex=('abc','xyz','pqr','1','1.1')\n",
    "str =  ''.join(tuplex)\n",
    "print(str)"
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
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "yes\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "5--->Write a Python program to check whether an element exists within a tuple\n",
    "ans->given below\n",
    "\n",
    "'''\n",
    "tuplex=(10,20,30)\n",
    "\n",
    "if 10 in tuplex:\n",
    "    print(\"yes\")"
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
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "6--->Write a Python program to find the length of a tuple.\n",
    "ans->given below\n",
    "\n",
    "'''\n",
    "tuplex=(10,20,30,'kkk')\n",
    "print(len(tuplex))"
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
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[10, 20, 30]\n",
      "(10, 20, 30)\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "7--->Write a Python program to convert a list to a tuple\n",
    "ans->given below\n",
    "\n",
    "'''\n",
    "a=[10,20,30]\n",
    "print(a)\n",
    "b=tuple(list(a))\n",
    "print(b)"
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
   "execution_count": 78,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('e', 'c', 'r', 'u', 'o', 's', 'e', 'r', '3', 'w')\n",
      "(20, 15, 10, 5)\n",
      "(30, 20, 10)\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "8--->Write a Python program to reverse a tuple\n",
    "ans->given below\n",
    "\n",
    "'''\n",
    "#create a tuple\n",
    "x = (\"w3resource\")\n",
    "# Reversed the tuple\n",
    "y = reversed(x)\n",
    "print(tuple(y))\n",
    "\n",
    "tuplex=(10,20,30)\n",
    "tuplex[::-1]#using slicing\n",
    "z=reversed(tuplex)\n",
    "print(tuple(z))"
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
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(10, 20, 55)\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "9--->Write a Python program to replace last value of tuples in a list\n",
    "ans->given below\n",
    "\n",
    "'''\n",
    "tuplex=(10,20,30)\n",
    "\n",
    "a=list(tuplex)\n",
    "\n",
    "a[-1]=55\n",
    "\n",
    "b=tuple(a)\n",
    "print(b)\n"
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
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "10--->Write a Python program to find the repeated items of a tuple\n",
    "'''\n",
    "tuplex=(10,20,30,40,50,50,50)\n",
    "print(tuplex.count(50))"
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
   "execution_count": 83,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[('',), ('a', 'b'), ('a', 'b', 'c'), 'd']\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "11--->Write a Python program to remove an empty tuple(s) from a list of tuples\n",
    "ans->given below\n",
    "\n",
    "'''\n",
    "L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]\n",
    "L = [i for i in L if i]\n",
    "print(L)     "
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
   "execution_count": 75,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[(1, 3, 8), (2, 4, 9)]\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "12--->Write a Python program to unzip a list of tuples into individual lists\n",
    "ans->given below\n",
    "\n",
    "'''\n",
    "l = [(1,2), (3,4), (8,9)]\n",
    "print(list(zip(*l)))"
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
   "execution_count": 115,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'A': 1, 'B': 2, 'C': 3}\n",
      "{'x': [1, 2, 3], 'y': [1, 2], 'z': [1]}\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "13--->Write a Python program to convert a list of tuples into a dictionary\n",
    "ans->given below\n",
    "\n",
    "'''\n",
    "#simple\n",
    "t = (('A', 1), ('B', 2), ('C', 3))\n",
    "d = { i:j for i,j in t }\n",
    "print(d)\n",
    "\n",
    "#using for loop\n",
    "l = [(\"x\", 1), (\"x\", 2), (\"x\", 3), (\"y\", 1), (\"y\", 2), (\"z\", 1)]\n",
    "d={}\n",
    "for k,v in l:\n",
    "    d.setdefault(k,[]).append(v)\n",
    "print(d)\n"
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
