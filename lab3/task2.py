def find_common_participants(
    group1: str, group2: str, sep: str = ","
) -> list[str]:
    return sorted(set(group1.split(sep)).intersection(group2.split(sep)))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(
    participants_first_group, participants_second_group, "|"
)

print(common_participants)
