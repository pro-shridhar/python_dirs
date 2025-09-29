def top_note(student):

    ans = {}
    for key in student:
        if key == "notes":
            ans["top_note"] = max(student[key])
        else:
            ans[key] = student[key]

    return ans
