from model import Role
from model.AssignmentGroup import AssignmentGroup
from model.Perspective import Perspective
from model.Section import Section
from model.StudentGroup import StudentGroup
from model.Teacher import Teacher


class CourseConfig:
    def __init__(self, name):
        self.name = name
        self.sections = []
        self.perspectives = []
        self.roles = []
        self.teachers = []
        self.assignmentGroups = []
        self.studentGroups = []

    def __str__(self):
        line = f'CourseConfig({self.name})\n'
        for section in self.sections:
            line += str(section)
        for teacher in self.teachers:
            line += str(teacher)
        # for role in self.roles:
        #     line += str(role)
        for perspectives in self.perspectives:
            line += str(perspectives)+"\n"
        for assignmentGroup in self.assignmentGroups:
            line += str(assignmentGroup)
        for studentGroup in self.studentGroups:
            line += str(studentGroup)
        return line

    def to_json(self, scope):
        return {
            'name': self.name,
            'sections': list(map(lambda s: s.to_json(), self.sections)),
            'perspectives': list(map(lambda p: p.to_json(), self.perspectives)),
            'roles': list(map(lambda r: r.to_json([]), self.roles)),
            'teachers': list(map(lambda t: t.to_json(), self.teachers)),
            'assignment_groups': list(map(lambda ag: ag.to_json(scope), self.assignmentGroups)),
            'student_groups': list(map(lambda sg: sg.to_json(['submission']), self.studentGroups)),
        }

    def find_student_group(self, group_id):
        for group in self.studentGroups:
            if group.id == group_id:
                return group
        return None

    def find_assignment_group(self, group_id):
        for group in self.assignmentGroups:
            if group.id == group_id:
                return group
        return None

    def find_perspective_by_assignment_group(self, group_id):
        for perspective in self.perspectives:
            if group_id in perspective.assignment_groups:
                return perspective
        return None

    def find_assignment_group_by_name(self, group_name):
        print(group_name)
        for group in self.assignmentGroups:
            print("find_assignment_group_by_name", group_name, group)
            if group.name == group_name:
                return group
        return None

    def find_assignment(self, assigment_group_id, assignment_id):
        assignmentGroup = self.find_assignment_group(assigment_group_id)
        if not assignmentGroup:
            return None
        for assigment in assignmentGroup.assignments:
            if assigment.id == assignment_id:
                return assigment
        return None

    def find_assignment_group_by_role(self, role_name):
        for role in self.roles:
            if role.name == role_name:
                return self.find_assignment_group(role.assignment_group_id)
        return None

    def get_role(self, role_short):
        for role in self.roles:
            if role.short == role_short:
                return role
        return None

    def find_role_by_section(self, section_id):
        for section in self.sections:
            if section.id == section_id:
                return section.role
        return None

    def find_student(self, student_id):
        for group in self.studentGroups:
            for student in group.students:
                if student.id == student_id:
                    return student
        return None

    def find_teacher_by_group(self, group_id):
        for teacher in self.teachers:
            if group_id in teacher.projects:
                return teacher
        return None

    def find_teacher(self, id):
        for teacher in self.teachers:
            if id == teacher.id:
                return teacher
        return None

    @staticmethod
    def from_dict(data_dict):
        new_course_config = CourseConfig(data_dict['name'])
        new_course_config.sections = list(map(lambda s: Section.from_dict(s), data_dict['sections']))
        new_course_config.teachers = list(map(lambda t: Teacher.from_dict(t), data_dict['teachers']))
        new_course_config.perspectives = list(map(lambda p: Perspective.from_dict(p), data_dict['perspectives']))
        new_course_config.roles = list(map(lambda r: Role.from_dict(r), data_dict['roles']))
        new_course_config.assignmentGroups = list(map(lambda g: AssignmentGroup.from_dict(g), data_dict['assignment_groups']))
        new_course_config.studentGroups = list(map(lambda s: StudentGroup.from_dict(s), data_dict['student_groups']))
        return new_course_config
