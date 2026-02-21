`map()` is a built-in function used to apply a function to **each item of an iterable** (like a list, tuple, etc.) and return a map object (which is an iterator).

Here's the **basic syntax**:

```python
map(function, iterable, ...)
```

### Explanation:

* **`function`** – The function to apply to each item. It can be a built-in function, a user-defined function, or a `lambda`.
* **`iterable`** – The iterable(s) whose items will be passed to the function. You can pass **more than one iterable**, but then the function must accept that many arguments.

---

### Examples:

**1. Applying a function to a list:**

```python
def square(x):
    return x ** 2

nums = [1, 2, 3, 4]
squared = map(square, nums)

print(list(squared))  # Output: [1, 4, 9, 16]
```

**2. Using `lambda` with map:**

```python
nums = [1, 2, 3, 4]
squared = map(lambda x: x**2, nums)

print(list(squared))  # Output: [1, 4, 9, 16]
```

**3. Using multiple iterables:**

```python
a = [1, 2, 3]
b = [4, 5, 6]

result = map(lambda x, y: x + y, a, b)
print(list(result))  # Output: [5, 7, 9]
```

**4. Converting strings to integers:**

```python
strings = ["1", "2", "3"]
numbers = map(int, strings)

print(list(numbers))  # Output: [1, 2, 3]
```

---

💡 **Tip:** `map()` returns a **map object**, so if you want a list, you need to wrap it in `list()` or iterate over it.

