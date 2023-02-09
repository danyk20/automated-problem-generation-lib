# Welcome to the generator library's documentation!

---

A generator library is a Python package that generates random data within set restrictions for you. A generator library is a Python package that generates random data within set restrictions for you. When you need to generate random individual values into a game for various players, this library is for you.

---

## Compatibility

It supports only Python 3.6, and the above Python versions may work as well, however it is not guaranteed. 

## Basic Usage

Open `demo.py`: 
0. remove SEED - it's just optional parameter for testing
1. update URL
2. update USERNAME
3. run `demo.py` using pipenv, you should see print of generated values as dictionary : {id. name: generated_value, ...}
    ```
    # pipenv install  
    # pipenv run python3 demo.py
   ```

Open and change `input.yml` base your needs or update PATH attribute of `demo.py` to your own file.

How it works
---
---
Generator pkg consists of `var_generator.py` where all required logical functions to generation process can be found, `var_parser.py` which function loads and processes the input data and finally `var_object.py` which stores class `Variable`. 

`var_generator.py` 
---
has function `generator(list_of_Variable)` with one argument that is a list filled with a `Variable` object. The result is that each object of `Variable` has been filled attribute `generated_value` with selected restrictions.

`var_parser.py` 
---
has function `parser_var_file(var_file)` that reads all input data from `var_file` the Python file object and fill them into `Variable` objects that are returned as a list. 

`var_object.py` 
---
has a constructor with all possible attributes that have an impact on the generation process. The only mandatory arguments are name and type.

`var_challenge.py` 
---
help class to store name and id of generated value.

Supported variable types:
---
---

* **username** - randomly chosen username
* **password** - randomly generated characters
* **port**     - randomly generated number
* **text**     - randomly chosen sentence

## How should variable in the input file look like?

---
---
You have to create one input file to set minimal or maximal generated values, set prohibited values for each generated variable.

| keyword / type: | username | password | text | port | IP |
| -------------   |:-----: | :-----:| :----:| :----:| :-----:|
| ***type***      | ✓      | ✓      | ✓     | ✓     | ✓     |
| min             | -      | -      | -     | ✓     | ✓     |
| max             | -      | -      | -     | ✓     | ✓     |
| prohibited      | ✓      | ✓      | -     | ✓     | ✓     |
| challenge_id    | ✓      | ✓      | ✓     | ✓     | ✓     |
| length          | ✓      | ✓      | -     | -     | -     |

***bold*** - required attribute

normal     - optional attribute

### Structure of input file:

      <variable_name>:
         - type: <variable_type>  
            min: <value>
            max: <value>
            length: <value>
            prohibited: [<value>,<value>,...]
            challenge_id: <int>  
    
      <variable_name>:
            ...

#### Attributes:
- min - Minimal value that still can be generated
- max - Maximal value that still can be generated
- length - Number variable of characters   
- prohibited - List of values that are excluded
- challenge_id - ID of the challenge where will be generated flag uploaded 

> NOTE: challenge_id - required to map flag to correct challenge