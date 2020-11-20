# include <iostream>
# include <list>

using namespace std;

class Graph{
    private:
        int V;
        list<int> *adj;
        void DFS_helper(int s, bool *visited);
    public:
        Graph(int v);
        void addEdge(int v, int w);
        void DFS(int s);
};

Graph::Graph(int v){
    V = v;
    adj = new list<int>[v];
}