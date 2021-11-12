#!/usr/bin/env python
import sys
import re


if len(sys.argv) < 4:
    print('At least three arguments are required.')
    sys.exit(0)


def read_file(file_path):
    with open(file_path) as file:
        return file.read()


def write(file_path, data):
    with open(file_path, 'r+') as the_file:
        the_file.write(data)


def merge_instance_infrastructure(svc_data, tmpl_data):
    svc_p1, sp, svc_p2 = re.split('(Outputs:)', svc_data)
    svc_p2 = f'{sp}{svc_p2}'
    tmpl = tmpl_data.split('Resources:')[1]

    return f'{svc_p1}{tmpl}{svc_p2}'


def merge_schema(svc_data, tmpl_data):
    svc_p1, sp, svc_p2, inf1, inf2 = re.split('(properties:)', svc_data)
    tmpl_p1, tmpl_sp, tmpl_p2 = re.split('(required:)', tmpl_data)
    prop_p1, prop_sp, prop_p2 = re.split('(properties:)', tmpl_p2)

    return f'{tmpl_p1}{svc_p1}{tmpl_sp}{prop_p1}{prop_sp}{prop_p2}{svc_p2}{inf1}{inf2}'


def merge_specs(svc_data, tmpl_data):
    svc_p1, sp, svc_p2 = re.split('(spec:)', svc_data)
    tmpl_p1, sp, tmpl_p2 = re.split('(spec:)', tmpl_data)

    return f'{svc_p1}{sp}{tmpl_p2}{svc_p2}'


if __name__ == "__main__":
    cmd = sys.argv[1]
    target_file_path = sys.argv[2]
    template_file_path = sys.argv[3]

    svc_data = read_file(target_file_path)
    tmpl_data = read_file(template_file_path)

    data = ''
    if cmd == 'instance_infrastructure':
        data = merge_instance_infrastructure(svc_data, tmpl_data)
    elif cmd == 'schema':
        data = merge_schema(svc_data, tmpl_data)
    elif cmd == 'specs':
        data = merge_specs(svc_data, tmpl_data)
    else:
        sys.exit(0)

    write(target_file_path, data)
