import streamlit as st
import numpy as np
import pandas as pd

def read_binary_file(file):
    """Reads a binary file and returns its contents as a DataFrame."""
    # Define the data type structure
    dt = np.dtype([('col1', 'd'), ('col2', 'd'), ('col3', 'd'), ('col4', 'd')])
    
    # Read the binary data into a numpy array
    data = np.frombuffer(file.read(), dtype=dt)
    
    # Convert the numpy array to a pandas DataFrame
    df = pd.DataFrame(data)
    return df

def main():
    """Main function to run the Streamlit app."""
    st.title("Binary File Decoder")

    # File uploader widget
    uploaded_file = st.file_uploader("Upload a binary file", type=["bin", "npy"])
    
    if uploaded_file:
        # Display the raw bytes of the uploaded file
        st.subheader("Raw File Content:")
        st.write(uploaded_file.getvalue())
        
        # Decode the binary file and display the DataFrame
        st.subheader("Decoded Data:")
        df = read_binary_file(uploaded_file)
        st.write(df)

if __name__ == "__main__":
    main()
