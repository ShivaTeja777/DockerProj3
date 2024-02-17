#importing modules
import os
import socket
from collections import Counter

# Defining a function to retrieve the IP address of the machine
def retrieve_ip_address():
    try:
        # Getting the hostname of the machine
        hostname = socket.gethostname()
        
        # Getting the IP address associated with the hostname
        ip_adrs = socket.gethostbyname(hostname)
        return ip_adrs

    except Exception as e:
        print("The error is :", e)
        return None

    
# Defining a function to list all text files in a directory
def list_text_files(directory):
    txt_files = [file for file in os.listdir(directory) if file.endswith('.txt')]
    return txt_files

# Defining a function to count words in a text file
def count_words(file_path):
    with open(file_path, 'r') as file:
        words = file.read().split()
        return len(words)

# Defining the directory containing the text files
directory =  "/home/data"

# Listing all text files in the directory
data_files = list_text_files(directory)

# Read and count words in all text files
word_cnts = Counter()
for file in data_files:
    file_path = os.path.join(directory, file)
    word_cnts[file] = count_words(file_path)

# Calculating the total number of words
ttl_words = sum(word_cnts.values())

# Finding the top 3 words with maximum counts in IF.txt
if_word_cnts = Counter()
if_file_path = os.path.join(directory, 'IF.txt')
with open(if_file_path, 'r') as if_file:
    if_words = if_file.read().split()
    if_word_cnts.update(if_words)
top_words = if_word_cnts.most_common(3)

# Retrieving the IP address
ip_adrs = retrieve_ip_address()

# Writing the output to result.txt
output_file_pth = '/home/output/result.txt'
with open(output_file_pth, 'w') as otpt_file:
    otpt_file.write(f"List of text files: {', '.join(data_files)}\n")
    for file in data_files:
        otpt_file.write(f"Total number of words in {file}: {word_cnts[file]}\n")
    otpt_file.write(f"Grand total number of words: {ttl_words}\n")
    otpt_file.write("Top 3 words with maximum counts in IF.txt:\n")
    for word, count in top_words:
        otpt_file.write(f"{word}: {count}\n")
    otpt_file.write(f"IP Address of the machine: {ip_adrs}\n")

# Printing the output from result.txt to console
with open(output_file_pth, 'r') as res_file:
    for line in res_file:
        print(line.strip())

