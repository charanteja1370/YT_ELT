# from datetime import timedelta, datetime


# def parse_duration(duration_str):

#     duration_str = duration_str.replace("P", "").replace("T", "")

#     components = ["D", "H", "M", "S"]
#     values = {"D": 0, "H": 0, "M": 0, "S": 0}

#     for component in components:
#         if component in duration_str:
#             value, duration_str = duration_str.split(component)
#             values[component] = int(value)

#     total_duration = timedelta(
#         days=values["D"], hours=values["H"], minutes=values["M"], seconds=values["S"]
#     )

#     return total_duration


# def transform_data(row):

#     duration_td = parse_duration(row["duration"])

#     row["Duration"] = (datetime.min + duration_td).time()

#     row["Video_Type"] = "Shorts" if duration_td.total_seconds() <= 60 else "Normal"

#     return row

from datetime import timedelta, datetime


def parse_duration(duration_str):

    duration_str = duration_str.replace("P", "").replace("T", "")

    components = ["D", "H", "M", "S"]
    values = {"D": 0, "H": 0, "M": 0, "S": 0}

    for component in components:
        if component in duration_str:
            value, duration_str = duration_str.split(component)
            values[component] = int(value)

    total_duration = timedelta(
        days=values["D"],
        hours=values["H"],
        minutes=values["M"],
        seconds=values["S"],
    )

    return total_duration


def transform_data(row):

    duration_td = parse_duration(row["duration"])

    transformed_row = {
        "Video_ID": row["video_id"],
        "Video_Title": row["video_title"],
        "Upload_Date": row["upload_date"],
        "Duration": (datetime.min + duration_td).time(),
        "Video_Type": "Shorts" if duration_td.total_seconds() <= 60 else "Normal",
        "Video_Views": int(row["video_views"] or 0),
        "Likes_Count": int(row["likes_count"] or 0),
        "Comments_Count": int(row["comments_count"] or 0),
    }

    return transformed_row