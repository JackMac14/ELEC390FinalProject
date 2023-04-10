import tkinter as tk
from tkinter import filedialog
import pandas as pd

# Function to browse and select input file
def browse_input_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    input_file_entry.delete(0, tk.END)
    input_file_entry.insert(tk.END, file_path)

# Function to browse and select output file
def browse_output_file():
    file_path = filedialog.asksaveasfilename(filetypes=[("CSV Files", "*.csv")])
    output_file_entry.delete(0, tk.END)
    output_file_entry.insert(tk.END, file_path)

# Function to process input file and generate output file
def process_file():
    input_file_path = input_file_entry.get()
    output_file_path = output_file_entry.get()

    try:
        # Read input CSV file
        df = pd.read_csv(input_file_path)

        # Do processing on input data (e.g. windowing, labeling, any other shit)
        # ...

        # Write output CSV file with labels
        df.to_csv(output_file_path, index=False)

        # Show success message
        tk.messagebox.showinfo("Success", "File processed successfully!")

    except Exception as e:
        # Show error message
        tk.messagebox.showerror("Error", str(e))

# Create main window
root = tk.Tk()
root.title("CSV Processor")

# Create input file label and entry
input_file_label = tk.Label(root, text="Input File:")
input_file_label.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)

input_file_entry = tk.Entry(root, width=40)
input_file_entry.grid(row=0, column=1, sticky=tk.W, padx=10, pady=10)

input_file_button = tk.Button(root, text="Browse", command=browse_input_file)
input_file_button.grid(row=0, column=2, padx=10, pady=10)

# Create output file label and entry
output_file_label = tk.Label(root, text="Output File:")
output_file_label.grid(row=1, column=0, sticky=tk.W, padx=10, pady=10)

output_file_entry = tk.Entry(root, width=40)
output_file_entry.grid(row=1, column=1, sticky=tk.W, padx=10, pady=10)

output_file_button = tk.Button(root, text="Browse", command=browse_output_file)
output_file_button.grid(row=1, column=2, padx=10, pady=10)

# Create process button
process_button = tk.Button(root, text="Process", command=process_file)
process_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Run GUI event loop
root.mainloop() 
