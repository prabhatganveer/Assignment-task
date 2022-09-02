{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "1--->How can you pick a random item from a list or tuple?\n",
    "ans->\n",
    "\n",
    "'''\n",
    "import random\n",
    "m=[1,2,3,4,5,6,7,8,9,10]\n",
    "x=random.choice(m)\n",
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
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "2--->How can you pick a random item from a range?\n",
    "ans->\n",
    "\n",
    "'''\n",
    "import random\n",
    "m=range(10)\n",
    "x=random.choice(m)\n",
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
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "3--->How can you get a random number in python?\n",
    "ans->Random integer values can be generated with the randint() function. This function takes \n",
    "     two arguments: the start and the end of the range for the generated integer values. \n",
    "     Random integers are generated within and including the start and end of range values,\n",
    "     specifically in the interval [start, end].\n",
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
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.46300735781502145\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "4--->How will you set the starting value in generating random numbers?\n",
    "ans->\n",
    "\n",
    "'''\n",
    "import random\n",
    "\n",
    "random.seed(9)\n",
    "print(random.random())"
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
      "[16, 20, 40, 55]\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "5--->How will you randomizes the items of a list in place?\n",
    "ans->\n",
    "\n",
    "'''\n",
    "import random\n",
    "l = [16,20,55,40]\n",
    "random.shuffle(l)\n",
    "print(l)"
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
      "prabhas\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "6--->Write a Python program to read a random line from a file.\n",
    "ans->\n",
    "\n",
    "'''\n",
    "import random\n",
    "lines = open('tony.txt').read().splitlines()\n",
    "myline =random.choice(lines)\n",
    "print(myline)"
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
    "7--->Write a Python program to convert degree to radian\n",
    "ans->\n",
    "\n",
    "'''\n",
    "pi=22/7\n",
    "degree = float(input(\"Input degrees: \"))\n",
    "radian = degree*(pi/180)\n",
    "print(radian)\n"
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
      "Input degrees: 5\n",
      "0.0873015873015873\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "8--->Write a Python program to calculate the area of at trapezoid\n",
    "ans->\n",
    "\n",
    "'''\n",
    "base_1 = 5\n",
    "base_2 = 6\n",
    "height = float(input(\"Height of trapezoid: \"))\n",
    "base_1 = float(input('Base one value: '))\n",
    "base_2 = float(input('Base two value: '))\n",
    "area = ((base_1 + base_2) / 2) * height\n",
    "print(\"Area is:\", area)\n"
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
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Length of base: 5\n",
      "Measurement of height: 5\n",
      "Area is:  25.0\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "9--->Write a Python program to calculate the area of aparallelogram\n",
    "ans->\n",
    "\n",
    "'''\n",
    "base = float(input('Length of base: '))\n",
    "height = float(input('Measurement of height: '))\n",
    "area = base * height\n",
    "print(\"Area is: \", area)\n",
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
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Height of cylinder: 2\n",
      "Radius of cylinder: 2\n",
      "Volume is:  25.142857142857142\n",
      "Surface Area is:  50.285714285714285\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "10--->Write a Python program to calculate surface volume and area of a cylinder\n",
    "ans->\n",
    "\n",
    "'''\n",
    "pi=22/7\n",
    "height = float(input('Height of cylinder: '))\n",
    "radian = float(input('Radius of cylinder: '))\n",
    "volume = pi * radian * radian * height\n",
    "sur_area = ((2*pi*radian) * height) + ((pi*radian**2)*2)\n",
    "print(\"Volume is: \", volume)\n",
    "print(\"Surface Area is: \", sur_area)\n"
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
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "sum of all divisors : 90\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "11--->Write a Python program to returns sum of all divisors of a number\n",
    "ans->\n",
    "\n",
    "'''\n",
    "d = []\n",
    "for i in range(2,20):\n",
    "    if i%2==0:\n",
    "        d.append(i)\n",
    "print(\"sum of all divisors :\",sum(d))"
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
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10.1\n",
      "1.0\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "12--->Write a Python program to find the maximum and minimum numbers from the specified decimal numbers.\n",
    "ans->\n",
    "\n",
    "'''\n",
    "x = [1.00,5.1,6.8,9.1,10.10]\n",
    "print(max(x))\n",
    "print(min(x))"
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
      "20.33\n",
      "['Decimal({2.45})', 'Decimal({2.69})', 'Decimal({2.45})', 'Decimal({3.45})', 'Decimal({2.0})', 'Decimal({0.04})', 'Decimal({7.25})']\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "13--->A1. Write a Python program to find the sum of the following decimal numbers and display the numbers in sorted order\n",
    "Decimal numbers : 2.45, 2.69, 2.45, 3.45, 2.00, 0.04,7.25\n",
    "Expected Output:\n",
    "Sum:20.33\n",
    "Sorted order: [Decimal('0.04'), Decimal('2.00'), Decimal('2.45'),Decimal('2.45'), Decimal('2.69'), Decimal('3.45'),Decimal('7.25')]\n",
    "ans->\n",
    "'Decimal(\"{}\")'.format(i)\n",
    "'''\n",
    "d = [2.45, 2.69, 2.45, 3.45, 2.00, 0.04,7.25]\n",
    "print(sum(d))\n",
    "x = sorted(d)\n",
    "q = []\n",
    "for i in d:\n",
    "    d='Decimal('+'{' + str(i) +'})'   \n",
    "    q.append(d)\n",
    "print(q)\n",
    "#print([f'Decimal(\"{i}\")' for i in d])   "
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
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Square root of  1.44  is : 1.2\n",
      "exponential of  1.44  is : 4.220695816996552825673328929\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "14--->Write a Python program to get the square root and exponential of a given decimal number\n",
    "ans->\n",
    "\n",
    "'''\n",
    "from decimal import *\n",
    "x = Decimal('1.44')\n",
    "print(\"Square root of \",x, \" is :\", x.sqrt())\n",
    "print(\"exponential of \",x, \" is :\", x.exp())\n"
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
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2/3 + 3/7 = 23/21\n",
      "2/3 - 3/7 = 5/21\n",
      "2/3 * 3/7 = 2/7\n",
      "2/3 / 3/7 = 14/9\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "15--->Write a Python program to add, subtract, multiply and divide two fractions.\n",
    "Expected Output: 2/3 + 3/7 =23/21\n",
    "2/3 -3/7 =5/21\n",
    "2/3 * 3/7 =2/7\n",
    "2/3 / 3/7 =14/9\n",
    "ans->\n",
    "\n",
    "'''\n",
    "import fractions\n",
    "\n",
    "f1 = fractions.Fraction(2, 3)\n",
    "f2 = fractions.Fraction(3, 7)\n",
    "\n",
    "print('{} + {} = {}'.format(f1, f2, f1 + f2))\n",
    "print('{} - {} = {}'.format(f1, f2, f1 - f2))\n",
    "print('{} * {} = {}'.format(f1, f2, f1 * f2))\n",
    "print('{} / {} = {}'.format(f1, f2, f1 / f2))\n"
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
