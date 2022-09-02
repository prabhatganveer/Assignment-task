{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[30, 20, 10]\n",
      "['d', 'c', 'b']\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "1--->What is List?How will you reverse a list?\n",
    "ans->Lists are used to store multiple items in a single variable.\n",
    "\n",
    "'''\n",
    "thislist=[10,20,30]#int\n",
    "thislist.reverse()\n",
    "a.reverse()\n",
    "a=['b','c','d']#str\n",
    "print(thislist)\n",
    "print(a)"
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
      "[10, 20]\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "2--->How will you remove last object from a list?\n",
    "ans->using remove() method\n",
    "\n",
    "'''\n",
    "thislist=[10,20,30]\n",
    "thislist.remove(30)\n",
    "print(thislist)\n"
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
     "data": {
      "text/plain": [
       "25"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'''\n",
    "3--->Suppose list1 is [2, 33, 222, 14, 25], What is list1[-1]?\n",
    "ans->list1[-1]=? ans is -> 25\n",
    "\n",
    "'''\n",
    "thislist=[2, 33, 222, 14, 25]\n",
    "thislist[-1]"
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
      "[10, 20, 30, 5]\n",
      "[10, 20, 30, 6, 5, 7]\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "4--->Differentiate between append() and extend()methods.?\n",
    "ans->\n",
    "append():-\n",
    "        ->Adds its argument as a single element to the end of a list. The length of the list increases by one.\n",
    "        ->A list is an object. If you append another list onto a list, the parameter list will be a single object \n",
    "          at the end of the list.\n",
    "        ->append() adds a single element to the end of the list while .\n",
    "        ->append() takes a single element as argument while . \n",
    "extend():-   \n",
    "        ->Iterates over its argument and adding each element to the list and extending the list. The length of the \n",
    "          list increases by number of elements in it’s argument.\n",
    "        ->A string is an iterable, so if you extend a list with a string, you’ll append each character as you iterate \n",
    "          over the string.\n",
    "        ->extend() can add multiple individual elements to the end of the list.\n",
    "        ->extend() takes an iterable as argument (list, tuple, dictionaries, sets, strings).\n",
    "\n",
    "\n",
    "'''\n",
    "#append()\n",
    "a=[10,20,30]\n",
    "a.append(5)\n",
    "print(a)\n",
    "#extend\n",
    "b=[10,20,30]\n",
    "b.extend([6,5,7])\n",
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
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "largest no :-  30\n",
      "minimum no :-  30\n",
      "sum of list:-  60\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "5--->Write a Python function to get the largest number,smallest num and sum of all from a list\n",
    "ans->\n",
    "\n",
    "''' \n",
    "a=[10,20,30]\n",
    "print(\"largest no :- \",max(a))\n",
    "print(\"minimum no :- \",max(a))\n",
    "print(\"sum of list:- \",sum(a))\n",
    "    "
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
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'''\n",
    "6--->How will you compare two lists?\n",
    "ans->given below\n",
    "\n",
    "'''\n",
    "a=[1,2,3]\n",
    "b=[1,2,3]\n",
    "a==b\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
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
    "7--->Write a Python program to count the number of strings where the string length is 2 or more and the \n",
    "     first and last character are same froma given list of strings.\n",
    "ans->given below\n",
    "\n",
    "'''\n",
    "#1st and last word are same so count + 1\n",
    "words =['aba', 'xyx', 'aba', '1221'] #for time 1st and last are same.\n",
    "ctr = 0\n",
    "for word in words:\n",
    "    if len(word) > 1 and word[0] == word[-1]:\n",
    "        ctr = ctr + 1\n",
    "print(ctr)"
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
   "execution_count": 98,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{40, 10, 50, 20, 60}\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "8--->Write a Python program to remove duplicates from alist\n",
    "ans->given below\n",
    "\n",
    "'''\n",
    "a=[10,20,20,10,10,50,40,60]\n",
    "c=set(a)\n",
    "print(c)"
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
      "not empty\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "9--->Write a Python program to check a list is empty or not.\n",
    "ans->given below\n",
    "\n",
    "'''\n",
    "a=[10]\n",
    "if 10 in a:\n",
    "    print('not empty')\n",
    "else:\n",
    "    print('empty')\n"
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
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "10--->Write a Python function that takes two lists and returns True if the y have at least one common member\n",
    "ans->given below\n",
    "\n",
    "'''\n",
    "x=[10,20,30]\n",
    "y=[10,50,40]\n",
    "\n",
    "if x not in y:\n",
    "    True"
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
   "execution_count": 91,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 4, 9, 16, 25]\n",
      "[256, 289, 324, 361, 400]\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "11--->Write a Python program to generate and print a list of first and last 5 elements where the values \n",
    "      are square of numbers between 1 and 30\n",
    "ans->given below\n",
    "\n",
    "'''\n",
    "l = list()\n",
    "for i in range(1,21):\n",
    "    l.append(i**2)\n",
    "print(l[:5])\n",
    "print(l[-5:])\n"
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
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3]\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "12--->Write a Python function that takes a list and returns a new list with unique elements of the first list\n",
    "ans->given below\n",
    "\n",
    "'''\n",
    "a = [1, 2, 2, 3]\n",
    "b = []\n",
    "for i in a:\n",
    "    if i not in b:\n",
    "        b.append(i)\n",
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
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "snnsnxnsn\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "13--->Write a Python program to convert a list of characters into a string\n",
    "ans->given below\n",
    "\n",
    "'''\n",
    "\n",
    "a=['snns','nxnsn']\n",
    "b=''.join(a)\n",
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
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "'''\n",
    "14--->Write a Python program to select an item randomly from a list.\n",
    "ans->given below\n",
    "\n",
    "'''\n",
    "import random\n",
    "color_list = ['Red', 'Blue', 'Green', 'White', 'Black']\n",
    "print(random.choice(color_list))"
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
   "execution_count": 91,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 40, 60, 70, 90]\n",
      "2nd smallest is -> 40\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "15--->Write a Python program to find the second smallest number in a list.\n",
    "ans->given below\n",
    "\n",
    "'''\n",
    "a=[40,60,70,90,2]\n",
    "b=len(a)\n",
    "a.sort()\n",
    "print(a)\n",
    "print('2nd smallest is ->',a[1])"
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
   "execution_count": 96,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{10, 20, 30}\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "16--->Write a Python program to get unique values from a list\n",
    "ans->given below\n",
    "\n",
    "'''\n",
    "a=[10,20,30,30]\n",
    "c=set(a)\n",
    "print(c)"
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
   "execution_count": 106,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "yes in list\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "17--->Write a Python program to check whether a list contains a sub list\n",
    "ans->given below\n",
    "\n",
    "'''\n",
    "a=[10,20,30,[40,50,60]]\n",
    "if 40 in a[3]:\n",
    "    print('yes in list')"
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
   "execution_count": 112,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[10, 20]\n",
      "[40, 50, 60]\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "18--->Write a Python program to split a list into different variables.\n",
    "ans->given below\n",
    "\n",
    "'''\n",
    "\n",
    "\"\"\"\n",
    "listobj = ['love', 'yes', 'no']\n",
    "var1, var2, var3 = listobj\n",
    "print(var1)\n",
    "print(var2)\n",
    "print(var3)\n",
    "\"\"\"\n",
    "\n",
    "a=[10,20,30,40,50,60]\n",
    "b=a[0:2]\n",
    "c=a[3:]\n",
    "print(b)\n",
    "print(c)\n",
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
