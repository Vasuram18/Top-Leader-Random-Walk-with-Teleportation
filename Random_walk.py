import csv
import networkx as nx
import random
import numpy as np

def random_walk(G):
    
    nodes = list(G.nodes())  # Convert nodes to a list
    
    node_indices = {node: idx for idx, node in enumerate(nodes)}  # Map node labels to their indices
    
    RW_points = [0 for _ in range(G.number_of_nodes())]
    
    r = random.choice(nodes) #1st node randomly across the whole 
    
    RW_points[node_indices[r]] += 1 

    out = list(G.out_edges(r))

    count = 0
    
    while count != 100000:
    
        if len(out) == 0:
    
            focus = random.choice(nodes)
    
        else:
    
            r1 = random.choice(out)
            focus = r1[1]
        RW_points[node_indices[focus]] += 1
        out = list(G.out_edges(focus))
        count += 1

    return RW_points


def nodes_sort(results_rw):

    results_rw_array = np.array(results_rw)
    nodes_sorted_by_points = np.argsort(results_rw_array)
    nodes_sorted_by = nodes_sorted_by_points[::-1]

    return nodes_sorted_by
 
# Create a graph object

G = nx.DiGraph()

# Open the CSV file
with open('data.csv', newline='') as csvfile:
    # Create a CSV reader object
    reader = csv.reader(csvfile)
    
    # Skip the first row (headers)
    next(reader)
    
    # Initialize an empty list to store edge numbers
    edge_numbers = []
    c = 0
    l = []
    # Iterate over each row in the CSV file
    for row in reader:
        
        # Initialize an empty string for node entry number
        node_entry_number = ''
        length = 0
        
        # Iterate over each character in the entry
        for i in row[1]:
            if length == 11: #2022csb1150@iitrpr.ac.in
                break
            # Check if the character is a digit
            if i.isdigit():
                # Append the digit to the node entry number
                node_entry_number += i
                length += 1
            # Check if the character is an alphabet character
            elif i.isalpha():
                # Append the uppercase version of the alphabet character to the node entry number
                node_entry_number += i.upper()
                length += 1

        # Add the node to the graph only if node_entry_number is not empty
        if node_entry_number:
            G.add_node(node_entry_number)
        
        # Iterate over each element in the row (excluding the first two columns
        for element in row[2:]:

            # Find the index of the first digit
            i=len(element)-1
            s=''
            k= 0
            while(i>=0): #name 2022CSB1150
                if element[i]==' ':
                    k=i
                    break
                i = i-1
            for m in range(k+1,len(element)):
                    s += element[m]
                

            
            # Convert alphabetic characters to uppercase
            s= s.upper()
            
            # Add the edge number to the list
            edge_numbers.append(s)
            
            # Add the edge to the graph
            if s:
                G.add_edge(node_entry_number, s)
                with open('your_file.txt', 'a') as output_file:
                    c = c+1
                    output_file.write(f"{node_entry_number} {s}\n")
            
            #randomWalk

    
    results_rw = random_walk(G)
    #print(results_rw)
    nodes_sorted_by_points = nodes_sort(results_rw)
    #print(nodes_sorted_by_points)

    top_leader_index = nodes_sorted_by_points[0]
    top_leader_node = list(G.nodes())[top_leader_index]
    print("Top Leader:", top_leader_node)


    """ pr = nx.pagerank(G) 
    pr_sorted = sorted(pr.items(), key =lambda x:x[1],reverse=True)
    for i in pr_sorted:
        print(i[0]) """ 
            
# Write edge numbers to a text file


# Print the nodes and edges of the graph

print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())
print(c)
#nx.draw(G, with_labels=True)
#plt.show()
