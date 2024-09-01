from todo import Todo
    
class TodoList:
    def __init__(self, title):
        self._title = title
        self._todos = []
    
    @property
    def title(self):
        return self._title
    
    def add(self, todo):
        if not isinstance(todo, Todo):
            raise TypeError("Can only add Todo objects")
    
        self._todos.append(todo)

    def __str__(self):
        output_lines = [f'----- {self.title} -----']
        output_lines += [str(todo) for todo in self._todos]
        return '\n'.join(output_lines)
    
    def __len__(self):
        return len(self._todos)
    
    def first(self):
        if self._todos == []:
            raise IndexError("List is empty")

        return self._todos[0]
    
    def last(self):
        if self._todos == []:
            raise IndexError("List is empty")

        return self._todos[-1]

    def to_list(self):
        return list(self._todos)
    
    def todo_at(self, idx):
        return self._todos[idx]
    
    def mark_done_at(self, idx):
        self.todo_at(idx).done = True

    def mark_undone_at(self, idx):
        self.todo_at(idx).done = False

    def mark_all_done(self):
        def mark_done(todo):
            todo.done = True

        self.each(mark_done)

    def mark_all_undone(self):
        def mark_undone(todo):
            todo.done = False
        
        self.each(mark_undone)
        
    def all_done(self):
        return all([todo.done for todo in self._todos])
    
    def remove_at(self, idx):
        self._todos.pop(idx)
    
    def each(self, callback):
        for item in self._todos:
            callback(item)
            
    def select(self, callback):
        selected = TodoList(self.title)
        for item in filter(callback, self._todos):
            selected.add(item)
        
        return selected
    
    def find_by_title(self, title):
        filtered = self.select(lambda item: item.title == title)
        return filtered._todos[0]

    def done_todos(self):
        done = self.select(lambda item: item.done)
        return done
    
    def undone_todos(self):
        undone = self.select(lambda item: not item.done)
        return undone
    
    def mark_done(self, title):
        matched = self.find_by_title(title)
        matched.done = True


# Code omitted
empty_todo_list = TodoList('Nothing Doing')


def setup():
    todo1 = Todo("Buy milk")
    todo2 = Todo("Clean room")
    todo3 = Todo("Go to gym")

    todo2.done = True

    todo_list = TodoList("Todays' Todos")
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.add(todo3)

    return todo_list

