# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ah/2

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: S = a + b + c

# Functions for calculating the areas and perimeters of a square, triangle, rectangle, and circle

## rectangle.py
```python
def area(a, b):
    return a * b
```
### The function takes the lengths of two different sides of a rectangle (a, b) and returns the area of that rectangle by multiplying the lengths of the two different sides (a * b)

### **Parameters:**
```
- `a` (float/int) - length of the first side
- `b` (float/int) - length of the second side
```
    
### **Returns:**
```
- float/int - area of the rectangle
```

### **Example of a call**
```
area(1, 2) # the function will return 2
```

```python
def perimeter(a, b):
    return 2 *(a + b)
```
### The function takes the lengths of two different sides of a rectangle (a, b) and returns the perimeter of that rectangle by adding the double lengths of the two different sides of that rectangle (2*(a + b))

### **Parameters:**
```
- `a` (float/int) - length of the first side
- `b` (float/int) - length of the second side
```

### **Returns:**
```
- float/int - perimeter of the rectangle
```

### **Example of a call**
```
perimeter(1, 2) # the function will return 6
```

## circle.py

```python
def area(r):
    return math.pi * r * r
```
### The function takes the radius of the circle (r) and returns the area of the circle by multiplying pi by the square of the radius (math.pi * r * r)

### **Parametr:**
```
- `r` (float/int) - circle radius
```

### **Returns:**
```
- float/int - area of the circle
```

### **Example of a call**
```
area(1) # the function will return 1 * pi
```

```python
def perimeter(r):
    return 2 * math.pi * r
```

### The function takes the radius of a circle (r) and returns the perimeter of the circle by multiplying pi by twice the radius (2 * math.pi * r)

### **Parametr:**
```
- `r` (float/int) - circle radius
```

### **Returns:**
```
-float/int - perimeter of the circle
```

### **Example of a call**
```
perimeter(1) # the function will return 2 * pi
```

## square.py
```python 
def area(a):
    return a * a
```

### The function takes the side length of a square (a) and returns the area of that square by squaring the side length (a * a)

### **Parametrs**
```
- `a` (float/int) - length off square side
```

### **Returns**
```
-float/int - area of the square
```

### **Example of a call**
```
area(2) # the function will return 4
```

```python
def perimeter(a):
    return 4 * a
```

### The function takes the side length of a square (a) and returns the perimeter of that square by multiplying the side length of the square by 4 (a * 4)

### **Parametrs**
```
- `a` (float/int) - length off square side
```

### **Returns**
```
-float/int - perimeter of the square
```

### **Example of a call**
```
perimeter(2) # the function will return 8
```

## triangle.py
```python
def area(a, h):
    return a * h / 2
```

### The function takes the length of a triangle's side and the height based on that side (a, h) and returns the area of the triangle by multiplying the length of the triangle's side, the length of its height, and one-half (a * h / 2).

### **Parametrs**
```
- `a` (float/int) - the length of the side of the triangle
- `h` (float/int) - the length of the height of the triangle
```

### **Returns**
```
- (float/int) - area of the triangle
```

### **Example of a call**
```
area(1, 2) # the function will return 1
```

```python
def perimeter(a, b, c):
    return a + b + c
```

### The function takes the lengths of all sides of a triangle (a, b, c) and returns the perimeter of that triangle by adding the lengths of all sides (a + b + c)

### **Parametrs**
```
- `a` (float/int) - the length of the side of the triangle
- `b` (float/int) - the length of the side of the triangle
- `c` (float/int) - the length of the side of the triangle
```

### **Returns**
```
- (float/int) - perimeter of the triangle
```

### **Example of a call**
```
perimeter(1, 2, 3) # the function will return 6
```

## Commits
```
'8ba9aeb3cea847b63a91ac378a2a6db758682460' # Circle.py and square.py added
'd078c8d9ee6155f3cb0e577d28d337b791de28e2' # Docs added
'b3c66a5a80afb8dc978d01e71316693c8bffce5' # added triangle.py and rectangle.py
'8e9fcb7675d7984481f86a7806ff3700326ef78a' # Descriptions have appeared in the functions
```



