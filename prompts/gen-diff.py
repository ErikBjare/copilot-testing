def main():
    print("Hello World")


# translate above function main to JavaScript.
# post-generation action: uncommented, put output in multiline string instead
"""
function main() {
  console.log("Hello World");
}
"""

# output diff for translation
"""
1,2c1,3
< def main():
<     print("Hello world")
---
> function main() {
>     console.log("Hello world")
> }
4,6c5
<
< if __name__ == "__main__":
<     main()
---
> main();
"""


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# output resulting js code
"""
function fib(n) {
  if (n == 0) {
    return 0;
  } else if (n == 1) {
    return 1;
  } else {
    return fib(n - 1) + fib(n - 2);
  }
}
"""

# output diff for translation
"""
1,2c1,3
< def fib(n):
<     if n == 0:
<         return 0
<     elif n == 1:
<         return 1
<     else:
<         return fib(n - 1) + fib(n - 2)
---
> function fib(n) {
>     if (n == 0) {
>         return 0;
>     } else if (n == 1) {
>         return 1;
>     } else {
>         return fib(n - 1) + fib(n - 2);
>     }
> }
4,6c5
<
< if __name__ == "__main__":
<     fib(10)
---
> fib(10);
"""
