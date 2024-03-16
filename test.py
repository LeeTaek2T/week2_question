import unittest
from priority_queue import PriorityQueue

class TestPriorityQueue(unittest.TestCase):

  def test_priority_queue_push_pop(self):
    pq = PriorityQueue()

    pq.push("Task 1")
    pq.push("Task 2")
    pq.push("Task 3")

    self.assertEqual(pq.pop(), "Task 1")
    self.assertEqual(pq.pop(), "Task 2")
    self.assertEqual(pq.pop(), "Task 3")
    self.assertIsNone(pq.pop())

  def test_priority_queue_empty_pop(self):
    pq = PriorityQueue()

    self.assertIsNone(pq.pop())

  def test_priority_queue_push_pop_order(self):
    pq = PriorityQueue()

    pq.push("Task 1")
    pq.push("Task 2")
    pq.push("Task 3")
    pq.push("Task 4")
    pq.push("Task 5")

    self.assertEqual(pq.pop(), "Task 1")
    self.assertEqual(pq.pop(), "Task 2")
    self.assertEqual(pq.pop(), "Task 3")
    self.assertEqual(pq.pop(), "Task 4")
    self.assertEqual(pq.pop(), "Task 5")
    self.assertIsNone(pq.pop())

  def test_priority_queue_duplicate_push_pop(self):
    pq = PriorityQueue()

    pq.push("Task 1")
    pq.push("Task 2")
    pq.push("Task 3")
    pq.push("Task 1")

    self.assertEqual(pq.pop(), "Task 1")
    self.assertEqual(pq.pop(), "Task 2")
    self.assertEqual(pq.pop(), "Task 3")
    self.assertIsNotNone(pq.pop())

  def test_priority_queue_negative_priority(self):
    pq = PriorityQueue()

    pq.push("Task 1")
    pq.push("Task 2")
    pq.push("Task 3")

    self.assertEqual(pq.pop(), "Task 1")
    self.assertEqual(pq.pop(), "Task 2")
    self.assertEqual(pq.pop(), "Task 3")
    self.assertIsNone(pq.pop())


if __name__ == "__main__":
  unittest.main()
