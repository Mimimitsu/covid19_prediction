from importlib.resources import path
from Graph import Graph
import os
import pandas as pd

path = "D:/Data/Mylecture/DATA7901/Outbound_Dataset/cleaning_dataset"
dirs = os.listdir(path)

def main():
    origin_list = []
    df_list = []
    graph = Graph()
    for file in dirs:
        df = pd.read_csv(path + '/' + file)
        df_list.append(df)
        # All origins' names
        origin_name = str(file).split('.csv')[0]
        origin_list.append(origin_name)

    for index in range(len(df_list)):
        df = df_list[index]
        origin = origin_list[index]
        graph.addVertex(origin)
        for i, line in df.iterrows():
            graph.addVertex(line['Destination'])
            graph.addEdge(origin, line['Destination'], line['Average'])
    
    print(graph.verList['South Sudan'])

    

  
    # t_graph = Graph()
    # A = t_graph.addVertex("A")
    # B = t_graph.addVertex("B")
    # C = t_graph.addVertex("C")

    # t_graph.addEdge('A', 'B', 1)
    # t_graph.addEdge('A', 'C', 2)
    # t_graph.addEdge('B', 'C', 2)
    # print(t_graph.verList)
    # print(t_graph.numVertices) 
    # print(A) 


if __name__ == '__main__':
    main()