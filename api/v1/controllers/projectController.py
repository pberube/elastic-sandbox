

def validate_project_name(project):
    projects = [
        {'projet1_reqs': {'read': True, 'write': False}},
        {'project1': {'read': True, 'write': True}}]
    return any(project in p for p in projects)


def nums(s):
    try:
        return int(s)
    except ValueError:
        float(s)

def validate_id(id):
    prefixes = ['SRS', 'SDS']
    is_valid = False
    try:
        split = id.split('-', 1)
        prefix = split[0]
        digits = split[1].split('.')
        if prefix.upper() in prefixes:
            if all(nums(d) for d in digits):
                is_valid = True
    except:
        pass
    return is_valid
