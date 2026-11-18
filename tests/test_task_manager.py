import unittest

from task_manager import add_task, complete_task, delete_task


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.tasks = []

    def test_add_task(self):
        task = add_task(self.tasks, "Finish DevOps assignment")
        self.assertEqual(len(self.tasks), 1)
        self.assertEqual(task["id"], 1)
        self.assertEqual(task["title"], "Finish DevOps assignment")
        self.assertFalse(task["done"])

    def test_add_empty_task_rejected(self):
        with self.assertRaises(ValueError):
            add_task(self.tasks, "   ")
        self.assertEqual(len(self.tasks), 0)

    def test_complete_task(self):
        add_task(self.tasks, "Read chapter 3")
        complete_task(self.tasks, 1)
        self.assertTrue(self.tasks[0]["done"])

    def test_complete_invalid_id(self):
        with self.assertRaises(ValueError):
            complete_task(self.tasks, 99)

    def test_delete_task(self):
        add_task(self.tasks, "Task A")
        add_task(self.tasks, "Task B")
        delete_task(self.tasks, 1)
        self.assertEqual(len(self.tasks), 1)
        self.assertEqual(self.tasks[0]["title"], "Task B")

    def test_delete_invalid_id(self):
        with self.assertRaises(ValueError):
            delete_task(self.tasks, 5)


if __name__ == "__main__":
    unittest.main()
