# 201901564/TESOL 영어학/박시온
# 정상동작

# Node 클래스 정의
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


# LinkedList 클래스 정의
class LinkedList:

	# 초기화 메소드
	def __init__(self):
		dummy = Node("dummy")
		self.head = dummy
		self.tail = dummy

		self.current = None
		self.before = None

		self.num_of_data = 0

	# append 메소드 (insert - 맨 뒤에 노드 추가, tail과 node의 next, 데이터 개수 변경)
	def append(self, data):
		new_node = Node(data)
		self.tail.next = new_node
		self.tail = new_node

		self.num_of_data += 1

	# delete 메소드 (delete - current 노드 삭제, 인접 노드의 current, next 변경, 데이터 개수 변경)
	def delete(self):
		pop_data = self.current.data

		if self.current is self.tail:
			self.tail = self.before

		# 중요 : current가 next가 아닌 before로 변경된다.
		self.before.next = self.current.next
		self.current = self.before 

		self.num_of_data -= 1

		return pop_data

	# first 메소드 (search1 - 맨 앞의 노드 검색, before, current 변경)
	def first(self):
		# 데이터가 없는 경우 첫번째 노드도 없기 때문에 None 리턴
		if self.num_of_data == 0: 
			return None

		self.before = self.head
		self.current = self.head.next

		return self.current.data

	# next 메소드 (search2 - current 노드의 다음 노드 검색, 이전에 first 메소드가 한번은 실행되어야 함)
	def next(self):
		if self.current.next == None:
			return None

		self.before = self.current
		self.current = self.current.next

		return self.current.data

	# size 메소드
	def size(self):
		return self.num_of_data 

	# traverse_all 메소드 구현
	def traverse_all(self):
		current = self.head.next
		result = "head"
		while current != None:
			result += f" -> ({current.data})"
			current = current.next
		result += " -> null"
		return result
	
	# insert_at 메소드 구현
	def insert_at(self, position, new_data):
		if position <= 0:
			print("Error: position 값이 0 이하입니다.")
			return

		new_node = Node(new_data)

		idx = 1
		current = self.head

		while idx < position and current.next != None:
			current = current.next
			idx += 1

		new_node.next = current.next
		current.next = new_node

		if new_node.next == None:
			self.tail = new_node

		self.num_of_data += 1

	# remove 메소드 구현
	def remove(self, key):
		self.before = self.head
		self.current = self.head.next

		found = False
		while self.current != None:
			if self.current.data == key:
				found = True
				self.delete()
				print(f"{key} 값의 노드를 삭제합니다.")
			else:
				self.before = self.current
				self.current = self.current.next

		if not found:
			print("해당하는 원소가 없습니다.")