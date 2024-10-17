import contractions
import socket
import os


# Function to get the IP address of the machine
def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address


# Function to process a file and return a word count dictionary
def process_file(file_path):
    unique = {}
    with open(file_path) as file:
        for line in file:
            line = line.lower()
            line = contractions.fix(line)  # Handle contractions
            line = line.replace(",", "").replace("\n", "")
            line = line.split(" ")
            for word in line:
                if word not in unique:
                    unique[word] = 1
                else:
                    unique[word] += 1
    return unique


# File paths
file1_path = "/home/data/AlwaysRememberUsThisWay.txt"
file2_path = "/home/data/IF.txt"
output_path = "/home/data/output/result.txt"

# Process the files
word_counts_file1 = process_file(file1_path)
word_counts_file2 = process_file(file2_path)

# a. Total number of words in each file
total_words_file1 = sum(word_counts_file1.values())
total_words_file2 = sum(word_counts_file2.values())

# b. Grand total of words across both files
grand_total_words = total_words_file1 + total_words_file2

# c. Top 3 most frequent words in IF.txt
top_3_file2 = sorted(word_counts_file2.items(), key=lambda x: x[1], reverse=True)[:3]

# d. Top 3 most frequent words in AlwaysRememberUsThisWay.txt after handling contractions
top_3_file1 = sorted(word_counts_file1.items(), key=lambda x: x[1], reverse=True)[:3]

# e. Get the IP address of the machine running the container
ip_address = get_ip_address()

# f. Write the results to a file and print them before exiting
with open(output_path, "w") as f:
    f.write(f"Total words in {file1_path}: {total_words_file1}\n")
    f.write(f"Total words in {file2_path}: {total_words_file2}\n")
    f.write(f"Grand total words: {grand_total_words}\n")
    f.write(f"Top 3 words in IF.txt: {top_3_file2}\n")
    f.write(f"Top 3 words in AlwaysRememberUsThisWay.txt: {top_3_file1}\n")
    f.write(f"IP address of the machine: {ip_address}\n")

# Print the results to the console
with open(output_path, "r") as f:
    print(f.read())
