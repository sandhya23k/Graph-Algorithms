import csv
import json
from graph_creation import TitleDictionary, MovieNetwork
from graph_algorithms import bfs, dfs, dijkstra, kosaraju

with open("Graph_Output.json", "r",encoding="iso-8859-1") as file:
    data = json.load(file)

total=0
f=0

td = TitleDictionary('imdb_network.csv')
nconst_title = td.title_dict
nconst_ar_dr = td.profession_dict

movie_network = MovieNetwork(nconst_title, nconst_ar_dr)
graph = movie_network.create_graph()

def dictionary_test():
    global total
    global f
    if(data["dictionary_test"] == nconst_title):
        print("\n{nconst_title} Dictionary Test Passed")
    else:
        print("{nconst : title} mapping is Mismatched")
        f+=1
    total+=1

    return nconst_title

def movie_network_test():
    global total
    global f
    if(data["movie_network_test"] == graph):
        print("\nMovie Network is Successfully created")
    else:
        print("\nMovie Network is Mismatched")
        f+=1
    total+=1

    return graph

def testcase_1_1():
    global total
    global f
    testcase_1_1 = bfs(graph, "nm0465106")
    if(len(set(data["testcase_1_1"])-set(testcase_1_1))==0):
        print("\nTestCase 1_1 Passed")
    else:
        print("\nTestCase 1_1 failed")
        f+=1
    total+=1

    return testcase_1_1

def testcase_1_2():
    global total
    global f
    testcase_1_2 = bfs(graph, "nm5822910", "nm5665539")
    if(data["testcase_1_2"]==testcase_1_2):
        print("\nTestCase 1_2 Passed")
    else:
        print("\nTestCase 1_2 failed")
        f+=1
    total+=1

    return testcase_1_2

def testcase_1_3():
    global total
    global f
    testcase_1_3 = bfs(graph, "nm5822910", "nm5775539")
    if(data["testcase_1_3"]==testcase_1_3):
        print("\nTestCase 1_3 Passed")
    else:
        print("\nTestCase 1_3 failed")
        f+=1
    total+=1

    return testcase_1_3

def testcase_2_1():
    global total
    global f
    testcase_2_1 = dfs(graph, "nm0465106")
    if(len(set(data["testcase_2_1"])-set(testcase_2_1))==0):
        print("\nTestCase 2_1 Passed")
    else:
        print("\nTestCase 2_1 failed")
        f+=1
    total+=1

    return testcase_2_1

def testcase_2_2():
    global total
    global f
    testcase_2_2 = dfs(graph, "nm5822910", search_node="nm5665539")
    if(data["testcase_2_2"]==testcase_2_2):
        print("\nTestCase 2_2 Passed")
    else:
        print("\nTestCase 2_2 failed")
        f+=1
    total+=1

    return testcase_2_2

def testcase_2_3():
    global total
    global f
    testcase_2_3 = dfs(graph, "nm5822910", search_node="nm5694296")
    if(data["testcase_2_3"]==testcase_2_3):
        print("\nTestCase 2_3 Passed")
    else:
        print("\nTestCase 2_3 failed")
        f+=1
    total+=1

    return testcase_2_3

def testcase_3_1():
    global total
    global f
    testcase_3_1 = dijkstra(graph, "nm4556923", "nm5822910")
    if(data["testcase_3_1"][0]==testcase_3_1[0] and data["testcase_3_1"][1]==testcase_3_1[1] and data["testcase_3_1"][2]==testcase_3_1[2]):
        print("\nTestCase 3_1 Passed")
    else:
        if(data["testcase_3_1"][0]==testcase_3_1[0]):
            print("\nYour path for TestCase 3_1 is passed")
        else:
            print("\nYour path for TestCase 3_1 is InCorrect")
        if(data["testcase_3_1"][1]==testcase_3_1[1]):
            print("\nYour Sum of minimum distances for TestCase 3_1 is Correct")
        else:
            print("\nYour Sum of minimum distances for TestCase 3_1 is InCorrect")
        if(data["testcase_3_1"][2]==testcase_3_1[2]):
            print("\nYour Hop count from start node to end node for TestCase 3_1 is Correct")
        else:
            print("\nYour Hop count from start node to end node for TestCase 3_1 is InCorrect")

        f+=1
    total+=1

    return testcase_3_1

def testcase_3_2():
    global total
    global f
    testcase_3_2 = dijkstra(graph, "nm0465106", "nm1118718")
    if(data["testcase_3_2"][0]==testcase_3_2[0] and data["testcase_3_2"][1]==testcase_3_2[1] and data["testcase_3_2"][2]==testcase_3_2[2]):
        print("\nTestCase 3_2 Passed")
    else:
        if(data["testcase_3_2"][0]==testcase_3_2[0]):
            print("\nYour path for TestCase 3_2 is passed")
        else:
            print("\nYour path for TestCase 3_2 is InCorrect")
        if(data["testcase_3_2"][1]==testcase_3_2[1]):
            print("\nYour Sum of minimum distances for TestCase 3_2 is Correct")
        else:
            print("\nYour Sum of minimum distances for TestCase 3_2 is InCorrect")
        if(data["testcase_3_2"][2]==testcase_3[2]):
            print("\nYour Hop count from start node to end node for TestCase 3_2 is Correct")
        else:
            print("\nYour Hop count from start node to end node for TestCase 3_2 is InCorrect")

        f+=1
    total+=1

    return testcase_3_2

def testcase_4_1():
    global total
    global f
    testcase_4_1 = kosaraju(graph)
    if(len(data["testcase_4_1"])==len(testcase_4_1)):
        print("\nTestCase 4_1 Passed")
    else:
        print("\nTotal number of strongly connected components for TestCase 4 is InCorrect")
        f+=1
    total+=1

    return testcase_4_1

def check_list_of_tuples_equality(list1, list2):
    # Convert the lists to sets of frozensets
    set1 = set(frozenset(item) for item in list1)
    set2 = set(frozenset(item) for item in list2)

    # Compare the sets for equality
    return set1 == set2

def testcase_4_2():
    global total
    global f
    testcase_4_2 = kosaraju(graph)
    if(check_list_of_tuples_equality(testcase_4_2,data["testcase_4_2"])==True):
        print("\nTestCase 4_2 Passed")
    else:
        print("\nTestCase 4_2 Failed")
        f+=1
    total+=1

    return testcase_4_1


testcase = {}

testcase['dictionary_test'] = dictionary_test()
testcase['movie_network_test'] = movie_network_test()
testcase['testcase_1_1'] = testcase_1_1()
testcase['testcase_1_2'] = testcase_1_2()
testcase['testcase_1_3'] = testcase_1_3()
testcase['testcase_2_1'] = testcase_2_1()
testcase['testcase_2_2'] = testcase_2_2()
testcase['testcase_2_3'] = testcase_2_3()
testcase['testcase_3_1'] = testcase_3_1()
testcase['testcase_3_2'] = testcase_3_2()
testcase['testcase_4_1'] = testcase_4_1()
testcase['testcase_4_2'] = testcase_4_2()

print("\n\nTotal Test Cases Passed : {}\nTotal Test Cases Failed : {}".format(total-f,f))