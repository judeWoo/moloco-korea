import csv
from datetime import datetime


def getAnalytics(filePath):
    # Q1
    target_c_id = "BDV"
    # <Key> : <Value>
    # "site_id" : {user_id}
    # "country_id" == "BDV"
    sites_in_bdv = {}

    # Q2
    ts_format = "%Y-%m-%d %H:%M:%S"
    start_ts = datetime.strptime("2019-02-03 00:00:00", ts_format)
    end_ts = datetime.strptime("2019-02-04 23:59:59", ts_format)
    # <Key> : <Value>
    # "site_id" : {user_id : frequency}
    sites_user_freq = {}

    # Q3
    # <Key> : <Value>
    # "user_id" : [last ts, site_id]
    users_last_site = {}
    # <Key> : <Value>
    # "site_id" : {user_id}
    sites_user_freq_last_ts = {}

    # Q4
    # <Key> : <Value>
    # "user_id" : [first ts, site_id]
    users_first_site = {}

    # Read CSV
    with open(filePath) as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row.
        for row in reader:
            site_id = row[3]
            country_id = row[2]
            user_id = row[1]
            if country_id == target_c_id:
                if site_id not in sites_in_bdv:
                    sites_in_bdv[site_id] = {user_id}
                elif user_id not in sites_in_bdv[site_id]:
                    sites_in_bdv[site_id].add(user_id)

            ts = datetime.strptime(row[0], ts_format)
            if ts > start_ts and ts < end_ts:
                if site_id not in sites_user_freq:
                    sites_user_freq[site_id] = {user_id: 1}
                elif user_id in sites_user_freq[site_id]:
                    sites_user_freq[site_id][user_id] += 1
                else:
                    sites_user_freq[site_id][user_id] = 1

            if user_id not in users_last_site:
                users_last_site[user_id] = [ts, site_id]
            elif users_last_site[user_id][0] <= ts:
                users_last_site[user_id][0] = ts
                users_last_site[user_id][1] = site_id

            if user_id not in users_first_site:
                users_first_site[user_id] = [ts, site_id]
            elif users_first_site[user_id][0] > ts:
                users_first_site[user_id][0] = ts
                users_first_site[user_id][1] = site_id

    # 1. Compute site_id that has the largest number of unique users when country_id == BDV
    most_site_bdv = ""
    most_user_bdv = 0
    for site in sites_in_bdv:
        num_unique_users = len(sites_in_bdv[site])
        if num_unique_users > most_user_bdv:
            most_site_bdv = site
            most_user_bdv = num_unique_users
    print("Which site_id has the largest number of unique users? And what's the number? \"" +
          most_site_bdv + ", " + str(most_user_bdv) + "\"")

    # 2. Find the four users & which sites they (each) visited more than 10 times.
    more_ten_users = {}
    target_freq = 10
    for site in sites_user_freq:
        for user in sites_user_freq[site]:
            frequency = sites_user_freq[site][user]
            if frequency > target_freq:
                more_ten_users[user] = [site, frequency]
    print("Find the four users & which sites they (each) visited more than 10 times. " + str(more_ten_users))

    # 3. What are top three sites? (Compute the unique number of users whose last visit was to that site.)
    top_three_sites = {}
    for user in users_last_site:
        site_id_last = users_last_site[user][1]
        if site_id_last not in sites_user_freq_last_ts:
            sites_user_freq_last_ts[site_id_last] = 1
        else:
            sites_user_freq_last_ts[site_id_last] += 1
    for site in sites_user_freq_last_ts:
        if len(top_three_sites) < 3:
            top_three_sites[sites_user_freq_last_ts[site]] = site
        elif min(top_three_sites) < sites_user_freq_last_ts[site]:
            top_three_sites[min(top_three_sites)] = site
    print("What are top three sites? " + str(top_three_sites))

    # 4. Compute the number of users whose first/last visits are to the same website.
    users_same_first_last = 0
    for user in users_last_site:
        if user in users_first_site and users_last_site[user][1] == users_first_site[user][1]:
            users_same_first_last += 1
    print("Compute the number of users whose first/last visits are to the same website. What is the number? " +
          str(users_same_first_last))


getAnalytics("sample-analytics.csv")
