class Operation:
    def __init__(self, operation_id, name):
        self.operation_id = operation_id
        self.name = name

    def __str__(self):
        return str(self.operation_id)

    def __repr__(self):
        return f"id: {self.operation_id}, name: {self.name}"


operations_by_id: dict[int, Operation] = {}

operations_by_id[1] = Operation(1, "Operation1")
operations_by_id[2] = Operation(2, "Operation2")

print(operations_by_id)