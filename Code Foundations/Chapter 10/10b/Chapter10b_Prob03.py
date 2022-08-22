import os
os.system('cls||clear')

#----CODE STARTS HERE------

import heapq
from datetime import datetime

class Saseiko:
    def __init__(self):
        self.data = list()
        heapq.heapify(self.data)

    def add_activity(self, activity):
        heapq.heappush(self.data, activity)

    def most_urgent_activity(self):
        return heapq.heappop(self.data)


class Activity:
    def __init__(self, activity_title, deadline):
        self.activity_title = activity_title
        self.deadline = deadline

    def __lt__(self, other):
        return self.deadline < other.deadline

