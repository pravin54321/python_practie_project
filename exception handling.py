{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "912ca6bb",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Exception handling\n",
    "try:\n",
    "    print(10/0)\n",
    "except ZeroDivisionError  as e:\n",
    "    print(e)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "8e580295",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter first Number10\n",
      "Enter Second Number2\n",
      "5.0\n"
     ]
    }
   ],
   "source": [
    "# multiple Exception\n",
    "try:\n",
    "    x=int(input(\"Enter first Number\"))\n",
    "    y=int(input(\"Enter Second Number\"))\n",
    "    print(x/y)\n",
    "except ZeroDivisionError:\n",
    "    print(\"canot DIVIDE WITH ZERO\")\n",
    "except ValueError:\n",
    "    print(\"please provide integer value\")\n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f4877fee",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
