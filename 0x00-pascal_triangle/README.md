<p align="center">
    <a href=#><img src="https://raw.githubusercontent.com/jbocane6/logos/main/holberton-logo.png" alt="holberton" /></a></p>
  
  <p align="center">
    <a href="https://twitter.com/juanoso07555284" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="juanoso07555284" height="30" width="40" /></a>
  <a href="https://linkedin.com/in/juan-camilo-bocanegra-osorio-18b1821a6" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="juan-camilo-bocanegra-osorio-18b1821a6" height="30" width="40" /></a>
  </p>
<br>

-----
0x00. Pascal's Triangle
=======================

Tasks
-----

### 0\. Pascal's Triangle

Mandatory

Create a function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal’s triangle of `n`:

*   Returns an empty list if `n <= 0`
*   You can assume `n` will be always an integer

main.py:

    camilo@home-laptop:~/0x00$ cat 0-main.py
    #!/usr/bin/python3
    """
    0-main
    """
    pascal_triangle = __import__('0-pascal_triangle').pascal_triangle
    
    def print_triangle(triangle):
        """
        Print the triangle
        """
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))
    
    
    if __name__ == "__main__":
        print_triangle(pascal_triangle(5))
    
Test:

    camilo@home-laptop:~/0x00$ 
    camilo@home-laptop:~/0x00$ ./0-main.py
    [1]
    [1,1]
    [1,2,1]
    [1,3,3,1]
    [1,4,6,4,1]
    camilo@home-laptop:~/0x00$ 
    

**Repo:**

*   GitHub repository: `holbertonschool-interview`
*   Directory: `0x00-pascal_triangle`
*   File: `0-pascal_triangle.py`

-----
Copyright © 2022 Holberton Inc, All rights reserved.