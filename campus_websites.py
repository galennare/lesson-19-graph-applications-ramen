import networkx as nx
from pprint import *

websites = [
    "Campus Life and Events", "Admissions and Enrollment", "Academic Programs and Departments", "Student Resources and Services",
    "Athletics and Sports Programs", "Campus News and Updates", "Campus Maps and Directions",
    "Financial Aid and Scholarships", "Housing and Residence Life", "Student Organizations and Clubs",
    "Campus Health and Wellness", "Career Services and Job Opportunities", "Diversity and Inclusion Initiatives",
    "Study Abroad and International Programs", "Library and Research Resources", "Technology and Computing Services",
    "Alumni Relations and Giving", "Campus Safety and Security", "Arts and Culture on Campus", "Faculty and Staff Directory"]

g = nx.complete_graph(len(websites), create_using=nx.Graph())

# Set the node labels as the websites
node_labels = {i: website for i, website in enumerate(websites)}
g = nx.relabel_nodes(g, node_labels)

pp = PrettyPrinter(indent=4, width=80)
pp.pprint(str(g))
