#!/usr/bin/env python

import textwrap


def check_for_filter():
    return True


def write_unload(table):
    sql = "select * from {}".format(table)

    filter_table = "filter_table"
    match = check_for_filter()

    join = ""
    if match:
        join = "join {} on {}.case_id = {}.case_id".format(table,
                                                           filter_table,
                                                           filter_table)
    sql = "{} {}".format(sql, join)

    cmd = """\
        unload ('{}')
        to 's3://mybucket/unload/'
        iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole'
        """.format(sql)

    print(textwrap.dedent(cmd))


if __name__ == "__main__":
    tables = ['table_a', 'table_b', 'table_c']

    for table in tables:
        write_unload(table)
