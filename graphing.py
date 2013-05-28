import networkx as nx

def simple_grid_manipulator(node, data):
    """A manipulator to get the appropriate piece of data from a 2D grid,
    based on the tuple used as the key for the node on a graph.

    """
    
    return data[node[0]][node[1]]


def cube_manipulator(n, data):
    """A manipulator to get the appropriate piece of data from a 3D grid,
    based on the tuple used as the key for the node on a graph. This will
    work for a cube of any dimensions (within the bounds of any overflow).

    """
    
    return data[n[0]][n[1]][n[2]]


def n_dimension_manipulator(node, data):
    """A manipulator similar to the 2D and 3D versions, but able to handle
    graph nodes of any dimension. 

    """
    temp = data
    for key in node:
        temp = temp[key]

    return temp

class Class2DManipulator(object):
    """A manpulator that calls the __init__ method of a class and returns
    the object that is created.

    It uses the node key to get the appropriate data for a class.

    """
    def __init__(self, type_to_build):
        self.klass = type_to_build
        
    def manipulate(self, node, data):

        return self.klass(data[node[0]][node[1]])
    

def populate_graph(graph, data, data_manipulator=simple_grid_manipulator):
    """ A method that populates data for a graph.

    For each node in the graph, data is extracted from the data object via
    the data_manipulator.

    By default data should be a 2D indexable structure (the most common graph for codejam
    appears to be a 2D grid) as this is what the default data_manipulator expects.

    However the data_manipulator can be overriden by any function or callable, to construct
    a node value based on any input data structure.

    For example you can create 3D data using the cube_manipulator, or rather than
    returning a simple value, you could initialise a class before returning.

    """
    
    for node in graph.nodes():
        graph.node[node]['info'] = data_manipulator(node, data)



def test():

    g = nx.grid_2d_graph(4,3)

    test_heights = ((1,2,3),(4,5,6),(7,8,9),(10,11,12))

    populate_graph(g, test_heights)
    assert g.node[(1,0)]['info'] == 4
    assert g.node[(0,1)]['info'] == 2
    assert g.node[(1,1)]['info'] == 5
    assert g.node[(3,2)]['info'] == 12
    assert g.node[(2,2)]['info'] == 9

    cube_values = a = [[[ i + j*3 + k* 9 for i in range(3)] for j in range(3)] for k in range(3)]
    g = nx.grid_graph(dim=[3,3,3])
    populate_graph(g, cube_values, cube_manipulator)
    
    assert g.node[(0,0,0)]['info'] == 0
    assert g.node[(2,2,2)]['info'] == 26
    assert g.node[(0,0,1)]['info'] == 1
    assert g.node[(0,0,2)]['info'] == 2
    assert g.node[(0,1,0)]['info'] == 3
    

    print "Tests passed"
    

if __name__ == '__main__':
    test()


