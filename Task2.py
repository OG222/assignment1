students = {}


class Student_Management:
      def __init__(self, students) -> None:
        self.students = students
        self.id = 0

      def register_student(self, name):
          self.id += 1
          details = {"name" : name, "grades": []}
          self.students[str(self.id)] = details
          return f"New student {name} registered"
      
      def record_grade(self, id, *grade):
          for i in grade:
            self.students[id]["grades"].append(i)
          return f"Grade recorded for {students[id]["name"]}"
          
      def calculate_average_grade(self, id):
          average = 0
          grades = self.students[id]["grades"]
          if grades:
            for i in grades:
              average += i
            return round(average/(len(grades)),2)
          else:
             return average
      
      def find_top_student(self):
          top_average = 0
          count = 0
          top_students = []
          for i in self.students:
            average = self.calculate_average_grade(i)
            if average > top_average:
                top_average = average
          for i in self.students:
            average = self.calculate_average_grade(i)
            if average == top_average:
                count += 1
                top_students.append(i)
          if count == 1:
                return f"The top student is {"".join([self.students[i]["name"] for i in top_students])} with average grade: {top_average}"
          else:
               top_students = [self.students[i]["name"] for i in top_students]
               return f"The top students are {", ".join(top_students[0:-1])} and {top_students[-1]} with average grade: {top_average}"
          
      def list_all_students(self):
          list = []
          for i in self.students:
              list.append(f"name: {self.students[i]["name"]} ID: {i} grades: {",".join((str(i) for i in self.students[i]["grades"]))}")          
          return "\n".join(list)

school = Student_Management(students)


print(school.register_student("Favour"))
print(school.register_student("Samuel"))
print(school.record_grade("1",99,80,96))
print(school.record_grade("2",97,88,90))
print(school.find_top_student())
print(school.list_all_students())
