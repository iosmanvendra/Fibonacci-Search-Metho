import streamlit as st
import pandas as pd

# Fibonacci Search Method
def fibonacci_search(func, a, b, epsilon):
    # Generate the Fibonacci sequence until the interval size is smaller than epsilon
    fib = [0, 1]
    while fib[-1] < (b - a) / epsilon:
        fib.append(fib[-1] + fib[-2])
    
    # Number of iterations
    k = len(fib) - 1
    fib_reverse = fib[::-1]  # Reverse Fibonacci series for display

    # Initialize x1 and x2
    if k < 2:
        st.error("Error: Not enough Fibonacci numbers generated. Try reducing epsilon.")
        return None, None
    
    d = fib_reverse[k - 2] / fib_reverse[k] if fib_reverse[k] != 0 else 0
    x1 = b - d * (b - a)
    x2 = a + d * (b - a)
    
    # Initial function evaluations
    f1 = func(x1)
    f2 = func(x2)
    
    steps = []  # To store the steps for displaying in the table
    steps.append({
        'Iteration': len(fib) - k - 1,  # Iteration counter
        'Fibonacci Series': fib_reverse[k],  # Fibonacci series in reverse
        'Current a': a, 
        'Current b': b, 
        'd': d, 
        'x1': x1, 
        'x2': x2, 
        'f(x1)': f1, 
        'f(x2)': f2, 
        'New a': a, 
        'New b': b
    })
    
    while k > 1:
        if f1 < f2:
            b = x2
            x2 = x1
            f2 = f1
            k -= 1
            if k < 2:
                break
            d = fib_reverse[k - 2] / fib_reverse[k] if fib_reverse[k] != 0 else 0
            x1 = b - d * (b - a)
            f1 = func(x1)
        else:
            a = x1
            x1 = x2
            f1 = f2
            k -= 1
            if k < 2:
                break
            d = fib_reverse[k - 2] / fib_reverse[k] if fib_reverse[k] != 0 else 0
            x2 = a + d * (b - a)
            f2 = func(x2)
        
        steps.append({
            'Iteration': len(fib) - k - 1,  # Iteration counter
            'Fibonacci Series': fib_reverse[k],  # Fibonacci series in reverse
            'Current a': a, 
            'Current b': b, 
            'd': d, 
            'x1': x1, 
            'x2': x2, 
            'f(x1)': f1, 
            'f(x2)': f2, 
            'New a': a, 
            'New b': b
        })
    
    # The minimum point
    return (a + b) / 2, steps

# Streamlit user interface
def main():
    # Custom CSS for colorful UI
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #f0f2f6;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 5px;
            padding: 10px 20px;
            font-size: 16px;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .stHeader {
            color: #4CAF50;
        }
        .stNumberInput>label, .stTextInput>label {
            color: #4CAF50;
            font-weight: bold;
        }
        .stTable {
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.title("Fibonacci Search Method")
    
    # Left-side input panel
    with st.sidebar:
        st.header("Inputs")
        
        # User input for the function
        func_str = st.text_input("Enter the function (e.g., x**2 + 2*x):", "x**2 + 2*x")
        func = lambda x: eval(func_str)  # Convert the string to an executable function
        
        # User input for interval
        a = st.number_input("Enter the starting point of the interval (a):", 0.0)
        b = st.number_input("Enter the ending point of the interval (b):", 1.0)
        
        # User input for epsilon
        epsilon = st.number_input("Enter the error tolerance (epsilon):", 0.001)
        
    # Perform Fibonacci Search and capture steps
    if st.button('Find Minimum'):
        minimum, steps = fibonacci_search(func, a, b, epsilon)
        
        if minimum is not None:
            # Display minimum result
            st.subheader(f"The minimum point is approximately at x = {minimum}")
            
            # Display the steps in table format
            st.subheader("Steps of Fibonacci Search")
            df = pd.DataFrame(steps)
            st.table(df)

# Run the main function
if __name__ == "__main__":
    main()
