def main():
    print("Hello world")


# translate the function to javascript
"""
function main() {
    console.log("Hello world")
}
"""


def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# translate the function to javascript
"""
function fib(n) {
  if (n <= 1) {
    return 1;
  } else {
    return fib(n - 1) + fib(n - 2);
  }
}
"""

import aw_core

def flood(e1: Event)
