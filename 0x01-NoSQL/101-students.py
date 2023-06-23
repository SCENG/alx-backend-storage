#!/usr/bin/env python3
"""
Top students
"""


def top_students(mongo_collection):
    students = mongo_collection.find({}, {"name": 1,
                                          "topics.score": 1
                                          }
                                     )
    sorted_students = sorted(students, key=lambda x: sum(
                topic["score"] for topic in x["topics"]
                                                        )
                                / len(x["topics"]), reverse=True
                                )
    for student in sorted_students:
        student["averageScore"] = sum(topic["score"] for topic in
                                      student["topics"]) / len(
                                      student["topics"]
                                )
    return sorted_students
