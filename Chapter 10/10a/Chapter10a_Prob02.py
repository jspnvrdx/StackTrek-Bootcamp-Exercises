import os
os.system('cls||clear')

#----CODE STARTS HERE------

class Child:
    def __init__(self, name, small_stickers, big_stickers):
        self.name = name
        self.total_small_stickers = small_stickers * 5
        self.total_big_stickers = big_stickers * 10

    def get_total_points(self):
        return self.total_small_stickers + self.total_big_stickers


class ChildrenQueue:
    def __init__(self, children):
        self.children = children

    def get_points_list(self):
        kids = [i.get_total_points() for i in self.children]
        kids.sort()
        return kids
        
    def get_children_queue(self):
        sorted_children = sorted(self.children, key=lambda x: x.get_total_points(), reverse=True)
        self.children_queue = [child.name for child in sorted_children]
        return self.children_queue

    def get_first_child_to_go(self):
        return self.children_queue[0] if len(self.children_queue) else None


child1 = Child("Terry", 2, 5)
child2 = Child("Alex", 3, 2)
child3 = Child("Lizzie", 6, 3)
child4 = Child("Donald", 2, 3)
child5 = Child("Roy", 1, 3)

children = []
children.append(child1)
children.append(child2)
children.append(child3)
children.append(child4)
children.append(child5)
childrenQueue = ChildrenQueue(children)
# print(child1.get_total_points())
print(childrenQueue.get_children_queue())