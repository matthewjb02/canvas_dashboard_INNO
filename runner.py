import sys
from lib.file import read_course_instance
from lib.lib_date import get_actual_date
from model.observer.observer_pattern import ConcreteEvent, ConcreteObserver


def main(instance_name, a_event):
    print("Only instance:", instance_name)
    course_instances = read_course_instance()
    # print(course_instances.current_instance)
    observers = []
    events = {}
    for event in course_instances.events.keys():
        events[event] = ConcreteEvent(event)
    for instance in course_instances.instances.values():
        for trigger in events.keys():
            if len(instance_name) > 0:
                if instance_name == instance.name:
                    observer = ConcreteObserver(instance.name, instance.listen[trigger])
                    observers.append(observer)
                    events[trigger].attach(observer)
            else:
                observer = ConcreteObserver(instance.name, instance.listen[trigger])
                observers.append(observer)
                events[trigger].attach(observer)

    # for event in course_instances.events.keys():
    print("RU11 -", a_event)
    events[a_event].notify()

if __name__ == "__main__":
    l_actual_date = get_actual_date()
    if len(sys.argv) > 2:
        main(sys.argv[1], sys.argv[2])
    else: #sep24_inno TICT-V1SE1-24_SEP2024
        # main("TICT-V1SE1-24_SEP2024", "results_create_event")
        main("sep24_inno", "results_create_event")
        # main("")

    total_seconds = (get_actual_date() - l_actual_date).seconds
    seconds = total_seconds % 60
    minutes = total_seconds // 60

    print(f"Time running: {min}:{seconds:02d} (m:ss)".format(minutes, seconds))
    print("Time running:", total_seconds, "seconds")
    print("Date running:", get_actual_date())




