import streamlit as st
import math

# Fibonacci Search Method
def fibonacci_search(func, a, b, epsilon):
    # Generate the Fibonacci sequence until the interval size is smaller than epsilon
    fib = [0, 1]
    while fib[-1] < (b - a) / epsilon:
        fib.append(fib[-1] + fib[-2])
    
    # Number of iterations
    k = len(fib) - 1
    x1 = a + (fib[k-2] / fib[k]) * (b - a)
    x2 = a + (fib[k-1] / fib[k]) * (b - a)
    
    # Initial function evaluations
    f1 = func(x1)
    f2 = func(x2)
    
    while k > 1:
        if f1 < f2:
            b = x2
            x2 = x1
            f2 = f1
            k -= 1
            x1 = a + (fib[k-2] / fib[k]) * (b - a)
            f1 = func(x1)
        else:
            a = x1
            x1 = x2
            f1 = f2
            k -= 1
            x2 = a + (fib[k-1] / fib[k]) * (b - a)
            f2 = func(x2)
    
    # The minimum point
    return (a + b) / 2

# Streamlit user interface
def main():
    st.title("Fibonacci Search Method")

    # User input for the function
    func_str = st.text_input("Enter the function (e.g., x**2 + 2*x):", "x**2 + 2*x")
    func = lambda x: eval(func_str)  # Convert the string to an executable function
    
    # User input for interval
    a = st.number_input("Enter the starting point of the interval (a):", -3.0)
    b = st.number_input("Enter the ending point of the interval (b):", 5.0)
    
    # User input for epsilon
    epsilon = st.number_input("Enter the error tolerance (epsilon):", 0.05)
    
    if st.button('Find Minimum'):
        # Perform Fibonacci Search
        minimum = fibonacci_search(func, a, b, epsilon)
        st.write(f"The minimum point is approximately at x = {minimum}")
        
if __name__ == "__main__":
    main()
