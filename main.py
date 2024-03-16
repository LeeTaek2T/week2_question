from priority_queue import PriorityQueue
def main():
  pq = PriorityQueue()
  pq.push("Task 1")
  pq.push("Task 2")
  pq.push("Task 3")
  print(pq.pop())
  print(pq.pop())
  print(pq.pop())
if __name__ == "__main__":
  main()
