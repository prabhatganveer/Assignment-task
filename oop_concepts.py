{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "1--->what are oops concepts?is multiple inheritance supported in java\n",
    "ans->Major Python OOPs concept-\n",
    "     Class.\n",
    "     Object.\n",
    "     Method.\n",
    "     Inheritance.\n",
    "     Encapsulation.\n",
    "     Polymorphism.\n",
    "     Data Abstraction.\n",
    "java in->The Java programming language supports multiple inheritance of type, which is the ability \n",
    "        of a class to implement more than one interface. ... As with multiple inheritance of \n",
    "        implementation, a class can inherit different implementations of a method defined \n",
    "        (as default or static) in the interfaces that it extends.\n",
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
    "2--->How To Define a Class in Python?What Is Self?Give An Example Of A Python Class\n",
    "ans->Create a class named Person, use the __init__() function to assign values for name and age: \n",
    "     class Person: def __init__(self, name, age): self.name = name.\n",
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
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "120\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "3--->Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle\n",
    "ans->\n",
    "'''\n",
    "class Rectangle():\n",
    "    def __init__(self, l, w):\n",
    "        self.length = l\n",
    "        self.width  = w\n",
    "\n",
    "    def rectangle_area(self):\n",
    "        return self.length*self.width\n",
    "\n",
    "newRectangle = Rectangle(12, 10)\n",
    "print(newRectangle.rectangle_area())\n"
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
      "200.96\n",
      "50.24\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "4--->Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle\n",
    "ans->\n",
    "'''\n",
    "class Circle():\n",
    "    def __init__(self, r):\n",
    "        self.radius = r\n",
    "\n",
    "    def area(self):\n",
    "        return self.radius**2*3.14\n",
    "    \n",
    "    def perimeter(self):\n",
    "        return 2*self.radius*3.14\n",
    "\n",
    "NewCircle = Circle(8)\n",
    "print(NewCircle.area())\n",
    "print(NewCircle.perimeter())\n"
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
    "5--->Explain Inheritance in Python with an example.?What Is init ? Or What Is A Constructor In Python?\n",
    "ans->In Python, every class inherits from a built-in basic class called 'object'\n",
    "   ->The constructor i.e. the '__init__' function of a class is invoked when we create an object \n",
    "     variable or an instance of the class.\n",
    "   ->The variables defined within __init__() are called as the instance variables or objects.\n",
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
    "6--->What is Instantiation in terms of OOP terminology?\n",
    "ans->In computer science, instantiation is the realization of a predefined object.\n",
    "     In OOP (object-oriented programming), a class of object may be defined. ... \n",
    "     An instance of that object may then be declared, giving it a unique, named identity so \n",
    "     that it may be used in the program. This process is called \"instantiation.\"\n",
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
    "7--->What is used To check whether an object o is an instance of class A\n",
    "ans->isinstance :-\n",
    "     The isinstance() function checks if the object (first argument) is an instance or subclass of classinfo class \n",
    "     (second argument). Return Value : true if the object is an instance or subclass of a class, or any element of the\n",
    "     tuple false otherwise.\n",
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
    "8--->What relationship is appropriate for Course and Faculty?\n",
    "ans->association\n",
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
    "9--->What relationship is appropriate for Student and Person?\n",
    "ans->inheritance\n",
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
    "10-->Which function overloads the + operator?Which operator is overloaded by invert()?\n",
    "ans->The function __or__() overloads the bitwise OR operator.\n",
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
    "11-->Which function overloads the >>operator?\n",
    "ans->__rshift__() overloads the >> operator.\n",
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
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Numbers : (1, 2)\n",
      "Add : 3\n",
      "Numbers : (3, 4)\n",
      "Add : 7\n",
      "Numbers : (None, None)\n",
      "Multiply 4 with 2 : 8\n",
      "Subtract 4 with 2 : -2\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "12-->Create a class called Numbers, which has a single class attribute called MULTIPLIER, and a \n",
    "     constructor which takes the parameters x and y (these should all benumbers).\n",
    "ans->\n",
    "'''\n",
    "class Numbers:\n",
    "    MULTIPLIER = 2\n",
    "    \n",
    "    def __init__(self,x,y):\n",
    "        self.x = x\n",
    "        self.y = y\n",
    "        \n",
    "    def add(self):\n",
    "        return self.x+self.y\n",
    "    \n",
    "    @classmethod\n",
    "    def multiply(cls,a):\n",
    "        return cls.MULTIPLIER*a\n",
    "    \n",
    "    @staticmethod\n",
    "    def subtract(b,c):\n",
    "        return b-c\n",
    "    \n",
    "    @property\n",
    "    def value(self):\n",
    "        return (self.x, self.y)\n",
    "    \n",
    "    @value.setter\n",
    "    def value(self, t):\n",
    "        self.x = t[0]\n",
    "        self.y = t[1]\n",
    "\n",
    "    @value.deleter\n",
    "    def value(self):\n",
    "        self.x = None\n",
    "        self.y = None\n",
    "        \n",
    "obj1 = Numbers(1,2)\n",
    "print(\"Numbers :\",obj1.value)\n",
    "print(\"Add :\",obj1.add())\n",
    "\n",
    "obj1.value = (3,4)\n",
    "print(\"Numbers :\",obj1.value)\n",
    "print(\"Add :\",obj1.add())\n",
    "\n",
    "del obj1.value\n",
    "print(\"Numbers :\",obj1.value)\n",
    "\n",
    "print(\"Multiply 4 with 2 :\",Numbers.multiply(4))\n",
    "print(\"Subtract 4 with 2 :\",Numbers.subtract(2,4))"
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
      "0.125\n",
      "243\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "13-->Write a Python class to implement pow(x,n)\n",
    "'''\n",
    "class py_solution:\n",
    "    def pow(self, x, n):\n",
    "        if x==0 or x==1 or n==1:\n",
    "            return x \n",
    "\n",
    "        if x==-1:\n",
    "            if n%2 ==0:\n",
    "                return 1\n",
    "            else:\n",
    "                return -1\n",
    "        if n==0:\n",
    "            return 1\n",
    "        if n<0:\n",
    "            return 1/self.pow(x,-n)\n",
    "        val = self.pow(x,n//2)\n",
    "        if n%2 ==0:\n",
    "            return val*val\n",
    "        return val*val*x\n",
    "\n",
    "print(py_solution().pow(2, -3));\n",
    "print(py_solution().pow(3, 5));\n",
    "print(py_solution().pow(100, 0));\n"
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
