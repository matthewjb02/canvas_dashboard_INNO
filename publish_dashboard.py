import shutil
import sys

from lib.file import read_start, read_course_instance, read_file_list
from lib.lib_date import get_actual_date


def main(instance_name):
    g_actual_date = get_actual_date()
    instances = read_course_instance()
    if len(instance_name) > 0:
        instances.current_instance = instance_name
    print("PB02 - Instance:", instances.current_instance)
    start = read_start(instances.get_start_file_name())
    print("PB04 - Copy files to OneDrive docenten")
    file_names = read_file_list(instances.get_project_path(instances.current_instance) + 'file_list.json')
    file_names.append("index.html")
    file_names.append("totals_voortgang.html")
    file_names.append("totals_werkvoorraad.html")
    for file_name in file_names:
        shutil.copyfile(instances.get_html_path() + file_name, start.target_path + file_name)
        print(file_name)
    shutil.copytree(instances.get_student_path(), start.target_path + "students", copy_function=shutil.copy2,
                    ignore_dangling_symlinks=False,
                    dirs_exist_ok=True)
    print("PD99 - Time running:", (get_actual_date() - g_actual_date).seconds, "seconds")


if __name__ == "__main__":
    print("PB01 publish_dashboard.py")
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main("")
