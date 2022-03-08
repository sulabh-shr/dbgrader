import os
import sys
import json
import copy
from collections import OrderedDict


def get_query_fields(dbs, queries):
    fields = {}

    for query in queries:
        for db in dbs:
            c_out = correct_answers[db][query]
            if len(c_out) == 0:
                continue
            query_fields = [i for i in c_out[0]]
            fields[query] = query_fields
            break
    return fields


with open(os.path.join('..', 'testDBs/correct_answers.json'), 'r') as f:
    correct_answers = json.load(f)

with open('answers.json', 'r') as f:
    answers = json.load(f)

dbs = [i for i in correct_answers]
queries = [i for i in correct_answers[dbs[0]]]
fields = get_query_fields(dbs, queries)

report = OrderedDict({
    "correctQueries": 0,
    "outOf": len(queries),
    "perQueryReport": [
        {
            "query": q,
            "correct": False,
            "perDBreport": []
        } for q in queries
    ]
})

CHECK_ORDER = False

for query_idx, query in enumerate(queries):
    query_correct_all = True

    for db in dbs:
        c_out = copy.deepcopy(correct_answers[db][query])
        a_out = copy.deepcopy(answers[db][query])

        query_db_report = {
            "query": query,
            "db": db,
            "correct": True
        }

        if CHECK_ORDER:
            if c_out != a_out:
                query_db_report["correct"] = False
                query_correct_all = False
        else:
            for c_tuple in c_out:

                # Check if this tuple is in a_out
                # Break at once if not found
                if c_tuple in a_out:
                    a_out.remove(c_tuple)
                    continue

                query_db_report["correct"] = False
                query_correct_all = False
                break

            # If all tuples checked and a_out still has some tuples left
            if len(a_out) != 0:
                query_db_report["correct"] = False
                query_correct_all = False

        report['perQueryReport'][query_idx]['perDBreport'].append(query_db_report)

    if query_correct_all:
        report['perQueryReport'][query_idx]["correct"] = query_correct_all
        report["correctQueries"] += 1


with open("report.json", "w") as f:
    f.write(json.dumps(report))
