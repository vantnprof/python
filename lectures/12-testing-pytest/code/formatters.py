import csv
import io


def format_people(people):
    rows = []
    for person in people:
        name = (
            f"{person['given']} "
            f"{person['family']}"
        )
        rows.append(
            f"{name}: {person['role']}"
        )
    return rows


def export_csv(people):
    buffer = io.StringIO()
    writer = csv.DictWriter(
        buffer,
        fieldnames=["given", "family", "role"],
        lineterminator="\n",
    )
    writer.writeheader()
    writer.writerows(people)
    return buffer.getvalue()
