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
       "'\\n1--->What isDictionaries?\\nans->\\n\\n'"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'''\n",
    "1--->What is Dictionaries?\n",
    "ans->Dictionaries are sometimes found in other languages as “associative memories” or “associative arrays”.\n",
    "   ->Dictionaries are used to store data values in key:value pairs.\n",
    "   ->A dictionary is a collection which is ordered*, changeable and does not allow duplicates.\n",
    "   ->Dictionaries are written with curly brackets, and have keys and values:\n",
    "   ->syntex:-\n",
    "    \n",
    "    Example\n",
    "            Create and print a dictionary:\n",
    "\n",
    "            thisdict = {\n",
    "              \"brand\": \"Ford\",\n",
    "              \"model\": \"Mustang\",\n",
    "              \"year\": 1964\n",
    "            }\n",
    "            print(thisdict)\n",
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
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "key is 2\n",
      "value is 12\n",
      "dict_keys([2, 1])\n",
      "dict_values([12, 24])\n",
      "key is 1\n",
      "value is 24\n",
      "dict_keys([2, 1])\n",
      "dict_values([12, 24])\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "2--->How will you create a dictionary in python?How will you get all the keys from the dictionary?\n",
    "     How will you get all the values from the dictionary?\n",
    "ans->\n",
    "\n",
    "'''\n",
    "b={2:12,1:24}\n",
    "for k,v in b.items():\n",
    "    print('key is',k)\n",
    "    print('value is',v)\n",
    "    print(b.keys())\n",
    "    print(b.values())"
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
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'tuple'>\n",
      "{'A': 1, 'B': 2, 'C': 3}\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "3--->How will you create a dictionary using tuples in python?\n",
    "ans->\n",
    "\n",
    "'''\n",
    "t = (('A', 1), ('B', 2), ('C', 3))\n",
    "print(type(t))\n",
    "d = { i:j for i,j in t }\n",
    "print(d)"
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
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original dictionary :  {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}\n",
      "Dictionary in ascending order by value :  [(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]\n",
      "Dictionary in descending order by value :  {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "4--->Write a Python script to sort (ascending and descending) a dictionary by value.\n",
    "ans->\n",
    "\n",
    "'''\n",
    "import operator\n",
    "d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}\n",
    "print('Original dictionary : ',d)\n",
    "sorted_d = sorted(d.items(), key=operator.itemgetter(1))\n",
    "print('Dictionary in ascending order by value : ',sorted_d)\n",
    "sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))\n",
    "print('Dictionary in descending order by value : ',sorted_d)"
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
      "{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "5--->Write a Python script to concatenate following dictionaries to create a newone\n",
    "ans->\n",
    "\n",
    "'''\n",
    "dic1={1:10, 2:20}\n",
    "dic2={3:30, 4:40}\n",
    "dic3={5:50,6:60}\n",
    "dic4 = {}\n",
    "for d in (dic1, dic2, dic3):\n",
    "    dic4.update(d)\n",
    "print(dic4)"
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
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Key is present in the dictionary\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "6--->Write a Python script to check if a given key already exists in a dictionary\n",
    "ans->\n",
    "\n",
    "'''\n",
    "x={'a':5,'b':4,'c':1,'d':8}\n",
    "if 'a' in x.keys():\n",
    "    print('Key is present in the dictionary')\n",
    "else:\n",
    "    print('Key is not present in the dictionary')"
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
    "7--->How Do You Traverse Through A Dictionary Object In Python?\n",
    "ans->There are two ways of iterating through a Python dictionary object. One is to fetch associated value \n",
    "     for each key in keys() list. There is also items() method of dictionary object which returns list of tuples,\n",
    "     each tuple having key and value.\n",
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
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The key is present.\n",
      "\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "8--->How Do You Check The Presence Of A Key In A Dictionary?\n",
    "ans->\n",
    "\n",
    "'''\n",
    "inp_dict = {'Python': \"A\", 'Java':\"B\", 'Ruby':\"C\", 'Kotlin':\"D\"} \n",
    " \n",
    "search_key = 'Ruby'\n",
    " \n",
    "if search_key in inp_dict: \n",
    "        print(\"The key is present.\\n\") \n",
    "          \n",
    "else: \n",
    "        print(\"The key does not exist in the dictionary.\") "
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
   "execution_count": 68,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "9--->Write a Python script to print a dictionary where the keys are numbers between 1 and 15(both Sample Dictionary)\n",
    "      {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, \n",
    "       9: 81, 10: 100,11: 121, 12: 144, 13:169,14: 196, 15:225}\n",
    "Example: 1, 4, 9, 16, ?\n",
    "Answer: they are Squares (12=1, 22=4, 32=9, 42=16, ...) \n",
    "Sequence: 1, 4, 9, 16, 25, 36, 49, ...\n",
    "ans->\n",
    "\n",
    "'''\n",
    "\n",
    "d={}\n",
    "s=1\n",
    "for i in range(1,16):\n",
    "    d[i]=i**2\n",
    "print(d) "
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
      "keys are more\n",
      "True\n",
      "False\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "10--->Write a Python program to check multiple keys exists in a dictionary\n",
    "ans->\n",
    "\n",
    "'''\n",
    "x={'a':5,'b':4,'c':1,'d':8}\n",
    "x1=len(x.keys())\n",
    "if x1>1:\n",
    "    print(\"keys are more\")\n",
    "else:\n",
    "    print(\"keys are less\")\n",
    "    \n",
    "student = {\n",
    "  'name': 'Alex',\n",
    "  'class': 'V',\n",
    "  'roll_id': '2'\n",
    "}\n",
    "print(student.keys() >= {'class', 'name'})\n",
    "print(student.keys() >= {'name', 'Alex'})\n",
    "print(student.keys() >= {'roll_id', 'name'})\n"
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
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'a': 5, 'b': 10, 'c': 15, 'd': 20, 'e': 25, 'f': 30, 'g': 35, 'h': 40}\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "11--->Write a Python script to merge two Python dictionaries\n",
    "ans->\n",
    "\n",
    "'''\n",
    "\n",
    "x={'a':5,'b':10,'c':15,'d':20}\n",
    "y={'e':25,'f':30,'g':35,'h':40}\n",
    "x.update(y)\n",
    "print(x)"
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
      "{'red': '#FF0000', 'green': '#008000', 'blue': '#0000FF'}\n",
      "{'red': ['#FF0000'], 'green': ['#008000'], 'blue': ['#0000FF']}\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "12--->Write a Python program to map two lists into a dictionary\n",
    "ans->\n",
    "\n",
    "'''\n",
    "#using zip function()\n",
    "keys = ['red', 'green', 'blue']\n",
    "values = ['#FF0000','#008000', '#0000FF']\n",
    "color_dictionary = dict(zip(keys, values))\n",
    "print(color_dictionary)\n",
    "\n",
    "#without zip()\n",
    "keys = ['red', 'green', 'blue']\n",
    "values = ['#FF0000','#008000', '#0000FF']\n",
    "k={}\n",
    "for i in range(3):\n",
    "    k[keys[i]]=[]\n",
    "    k[keys[i]].append(values[i])\n",
    "print(k)   "
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
   "execution_count": 99,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "13--->Write a Python program to combine two dictionary adding values for common keys.\n",
    "      d1 = {'a': 100, 'b': 200,'c':300}\n",
    "      d2 = {'a': 300, 'b': 200,'d':400}\n",
    "      Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c':300})\n",
    "ans->\n",
    "\n",
    "'''\n",
    "from collections import Counter\n",
    "d1 = {'a': 100, 'b': 200, 'c':300}\n",
    "d2 = {'a': 300, 'b': 200, 'd':400}\n",
    "d = Counter(d1) + Counter(d2)\n",
    "print(d)\n"
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
      "Original List:  {'a': 100, 'b': 200, 'c': 300, 'e': 100, 'f': 200, 'g': 300}\n",
      "Unique Values:  {200, 100, 300}\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "14--->Write a Python program to print all unique values in a dictionary.\n",
    "ans->\n",
    "\n",
    "'''\n",
    "x={'a': 100, 'b': 200, 'c':300, 'e':100, 'f':200, 'g':300}\n",
    "print(\"Original List: \",x)\n",
    "u_value = set( val for dic in x for val in x.values())\n",
    "print(\"Unique Values: \",u_value)"
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
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica'))\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "15--->Why Do You Use The Zip() Method In Python?\n",
    "ans->Python's zip() function creates an iterator that will aggregate elements from two or more iterables. \n",
    "     You can use the resulting iterator to quickly and consistently solve common programming problems, like creating \n",
    "     dictionaries.\n",
    "\n",
    "'''\n",
    "a = (\"John\", \"Charles\", \"Mike\")\n",
    "b = (\"Jenny\", \"Christy\", \"Monica\")\n",
    "\n",
    "x = zip(a, b)\n",
    "\n",
    "#use the tuple() function to display a readable version of the result:\n",
    "\n",
    "print(tuple(x))\n"
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
      "ac\n",
      "ad\n",
      "bc\n",
      "bd\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "16--->Write a Python program to create and display all combinations of letters, selecting each letter \n",
    "      from a different key in adictionary.\n",
    "      Sample data   : {'1':['a','b'], '2':['c','d']} \n",
    "      ExpectedOutput:\n",
    "        ac\n",
    "        ad\n",
    "        bc\n",
    "        bd\n",
    "ans->\n",
    "\n",
    "'''\n",
    "\n",
    "import itertools      \n",
    "d ={'1':['a','b'], '2':['c','d']}\n",
    "for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):\n",
    "    print(''.join(combo))"
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
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['b', 'e', 'c']\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "17--->Write a Python program to find the highest 3 values in a dictionary.\n",
    "ans-->\n",
    "\n",
    "'''\n",
    "from heapq import nlargest\n",
    "my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}  \n",
    "three_largest = nlargest(3, my_dict, key=my_dict.get)\n",
    "print(three_largest)"
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
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Counter({'item1': 1150, 'item2': 300})\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "18--->Write a Python program to combine values in python list of dictionaries. \n",
    "      Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':300},{'item': 'item1', 'amount':750}]\n",
    "      Expected Output:\n",
    "      Counter({'item1': 1150, 'item2':300})\n",
    "ans-->\n",
    "\n",
    "'''\n",
    "from collections import Counter\n",
    "item_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]\n",
    "result = Counter()\n",
    "for d in item_list:\n",
    "    result[d['item']] += d['amount']\n",
    "print(result) "
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
      "{'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "19--->Write a Python program to create a dictionary from a string. Note: Track the count of the letters from thestring.\n",
    "      Sample string :'w3resource'\n",
    "      Expected output: \n",
    "      {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o':1}\n",
    "ans-->\n",
    "\n",
    "'''\n",
    "from collections import defaultdict, Counter\n",
    "str1 = 'w3resource' \n",
    "my_dict = {}\n",
    "for letter in str1:\n",
    "    my_dict[letter] = my_dict.get(letter, 0) + 1\n",
    "print(my_dict)"
   ]
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
