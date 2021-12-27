def solution(id_list, report, k):

    idx_to_id = dict(zip(range(len(id_list)),id_list))
    id_to_idx = dict(zip(id_list,range(len(id_list))))

    user_report_list = [content.split(' ') for content in report]

    user_report_dict = {id:[] for id in id_list}

    for items in user_report_list:
        if items[1] not in user_report_dict[items[0]]:
            user_report_dict[items[0]].append(items[1])

    user_report_count = {id:0 for id in id_list}

    for key,value in user_report_dict.items():
        for id in value:
            user_report_count[id] += 1

    user_report_count = sorted(user_report_count.items(), key=lambda x:x[1], reverse=True)

    abuser_list = []

    for key,value in user_report_count:
        if int(value) >= k:
            abuser_list.append(key)
        else:
            break

    user_feedback_dict = {id:0 for id in id_list}

    for key,value in user_report_dict.items():
        num_feedback = len(value) - len(set(value) - set(abuser_list))
        user_feedback_dict[key] = num_feedback

    return list(user_feedback_dict.values())



id_list = ["con", "ryan"]


report = ["ryan con", "ryan con", "ryan con", "ryan con"]

k = 3


print(solution(id_list, report, k))
