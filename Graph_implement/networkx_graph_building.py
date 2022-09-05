import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import os
from networkx.algorithms.link_analysis.pagerank_alg import pagerank_numpy

path = "D:/Data/Mylecture/DATA7901/project_codes/Outbound_Dataset/cleaning_dataset"
dirs = os.listdir(path)

def main():
    # Create an empty graph entity
    graph = nx.DiGraph()

    # Read the origin name and their corresponding destinations from the csv file
    origin_list = []
    df_list = []
    for file in dirs:
        df = pd.read_csv(path + '/' + file)
        df_list.append(df)
        # All origins' names
        origin_name = str(file).split('.csv')[0]
        origin_list.append(origin_name)

    for index in range(len(df_list)):
        df = df_list[index]
        origin = origin_list[index]
        graph.add_node(origin)
        for i, line in df.iterrows():
            graph.add_node(line['Destination'])
            graph.add_edge(origin, line['Destination'], weight=line['Average'])

    pagerank = pagerank_numpy(graph)
    result = sorted(pagerank.items(), key=lambda x: x[1], reverse=True)
    df = pd.DataFrame(result, columns=['Region', 'Score'])
    df.to_csv(path_or_buf="page_rank_result.csv", index=False)
    print(df)


if __name__ == "__main__":
    main()