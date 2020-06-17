# MazeSolver
MazeSolver is a python script that finds the shortest path between Source and Destination in a binary maze of size (MxN).

>A binary maze is just a grid/matrix consisting of *0's and 1's*.  
>The 0's, in this case, represents inaccessible cells and 1's represent the accessible cells.  
>This means that we are allowed to traverse on the grid only through cells having value of 1.  
>  
>    Sample `[M=4]x[N=6]` binary maze:  
>    1 1 1 1 1 0  
     0 0 1 0 1 1  
     0 1 1 1 1 1  
     0 0 0 1 0 0 



The code used is based on [**Breadth First Search**](https://en.wikipedia.org/wiki/Breadth-first_search) and [**Lee Algorithm**](https://www.freecodecamp.org/news/lees-algorithm-explained-with-examples/). The algorithm is quite inefficient, especially in terms of space-complexity but it serves well in this case as it always returns the shortest path.

This script uses 

## Installation

[Clone](https://github.com/vibhor-vibhav-au6/MazeSolver-python-project.git) the project and in your terminal execute the following command:  

```
python mazeSolver.py <input> <output> --optional arguments
```
Alternatively, copy the contents of [mazesolver.py](https://github.com/vibhor-vibhav-au6/MazeSolver-python-project/blob/master/mazeSolver.py) to a new file: `<filename.py>` and in your terminal execute the following command:
```
python filename.py <input> <output> --optional arguments
```
>For `positional` and `optional` arguments, check **Usage**.  
>Alternatively, include `-h` in the Command line interface to get help.  
>```
>python mazeSolver.py -h 
>```  
>```
>python filename.py -h  
>```

## Usage
The positional arguments are:
- `input` A text file containing space separated values representing the input maze. Eg: `inputfile.txt`
- `output` A text file containing the generated solution matrix. Eg: `outputfile.txt`
- There are no default values for `input` & `output`. It **must be specified** while execution.
>```python
>python mazeSolver.py inputfile.txt outputfile.txt
>```
The optional arguments are:
- `--i` `--j` The (x,y) co-ordinates of the **starting** cell.  
- `--x` `--y` The (x,y) co-ordinates of the **destination** cell.

>For example, if the starting cell is (0,0) and destination cell is (7,5) :  
>```bash
>python mazeSolver.py inputfile.txt outputfile.txt --i 0 --j 0 --x 7 --y 5
>```


## Tech Specs
- Python 3.8.2
  -  `argsparse` for command line interface parsing.
  - `collections` for importing `dequeue`. 
- Flake8 linter for PEP8 standerds
- VS Code
- GIT bash 


## License
[MIT](https://choosealicense.com/licenses/mit/)

Feel free to Use, Modify and Share in any form. No credits required!