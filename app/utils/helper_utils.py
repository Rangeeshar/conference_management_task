from datetimerange import DateTimeRange


def give_object(start, end):
    return DateTimeRange(start, end)

def check_overlap(given_range, existing_ranges):
    current_interval = give_object(given_range[0], given_range[1])
    print("existing: {}".format(existing_ranges))
    print("current interval: {}".format(current_interval))
    for data in existing_ranges:
        start = data.get("start_time")
        end = data.get("end_time")
        if not start or not end:
            return False
        existing_interval = give_object(start, end)
        if current_interval.is_intersection(existing_interval):
            print("hii")
            return True
    return False


