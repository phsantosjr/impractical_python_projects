# Impractical Python Projects
![](https://img.shields.io/badge/Python-3.9-blue.svg)

Contains a source code based in the Chapter and exercises for the book Impractical Python Projects: Playful Programming Activities to Make You Smarter by Lee Vaughan. 

The files are organized by chapter. 

![image](https://user-images.githubusercontent.com/31315095/86491992-2382a380-bd32-11ea-82c2-e26febc82187.png) 

### Configure your environment

```
python3.9 -m venv .env
```

Activate your virtual environment

```
source .env/bin/activate 
```

### Pylint

>Pylint analyses your code without actually running it. It checks for errors, 
> enforces a coding standard, looks for code smells, and can make suggestions about how the code could be refactored. 
> Pylint can infer actual values from your code using its internal code representation (astroid).
> (Pylint official documentation)

[Pylint Official Documentation](https://pylint.pycqa.org/en/latest/)

```
pylint <name_of_your_file>.py
```

### Tests

```
pytest
```

## Chapter 1

#### Pseudonyms

>the code for the funny name generator, pseudonyms.py, which
compiles and prints a list of pseudonyms from two tuples of names. If you
don’t want to type all the names
> (Vaughan, Lee)

- How to config?
In file ```main.py``` you can change the variable ```language``` for one support by [Faker](https://faker.readthedocs.io/en/master/locales.html) and change the value for ```total_names```


#### Pig Latin

>To form Pig Latin, you take an English word that begins with a consonant,
move that consonant to the end, and then add “ay” to the end of the word.
If the word begins with a vowel, you simply add “way” to the end of the
word. One of the most famous Pig Latin phrases of all time is “ixnay on the
ottenray,” 
> (Vaughan, Lee)

#### Poor Man Bar Chart

Simple chart for character count

