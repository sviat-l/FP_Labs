"""
Explore browser history
"""


def sites_on_date(visits: list, date: str):
    """
    Returns set of all urls that have been visited
    on current date
    :param visits: all visits in browser history
    :param date: date in format "yyyy-mm-dd"
    :return: set of url visited on date
    >>> sites_on_date([('www.archlinux.org/','Archlinux','2021-10-10','03:30:01.30', 42),\
                    ('www.cms.ucu.edu.ua/','CMS','2021-10-11','03:35:01.30', 42),\
                    ('www.archlinux.org/','Archlinux','2021-10-10','03:59:01.30', 42)],\
                                                                           '2021-10-10')
    {'www.archlinux.org/'}
    >>> sites_on_date([('www.archlinux.org/','Archlinux','2021-10-10','03:30:01.30', 42),\
                    ('www.cms.ucu.edu.ua/','CMS','2021-10-11','03:35:01.30', 42),\
                    ('www.archlinux.org/','Archlinux','2021-10-10','03:59:01.30', 42)],\
                                                                           '2021-10-12')
    set()
    """
    visited_by_date = set()
    for current_visit in visits:
        # check if url visit date is equal to stated date
        if current_visit[2] == date:
            visited_by_date.add(current_visit[0])
    return visited_by_date


def most_frequent_sites(visits: list, number: int):
    """
    Returns set of most frequent sites visited in total
    Return only 'number' of most frequent sites visited
    :param visits: all visits in browser history
    :param number: number of most frequent sites to return
    :return: set of most frequent sites
    >>> most_frequent_sites([('www.archlinux.org/','Archlinux','2021-10-10','03:30:01.30', 42),\
                    ('www.cms.ucu.edu.ua/','CMS','2021-10-10','03:35:01.30', 42),\
                    ('www.archlinux.org/','Archlinux','2021-10-10','03:59:01.30', 42)], 1)
    {'www.archlinux.org/'}
    >>> most_frequent_sites([('www.archlinux.org/','Archlinux','2021-10-10','03:30:01.30', 42)],\
                                                                                             10)
    {'www.archlinux.org/'}
    >>> most_frequent_sites([('www.archlinux.org/','Archlinux','2021-10-10','03:30:01.30', 42),\
                    ('www.cms.ucu.edu.ua/','CMS','2021-10-10','03:35:01.30', 42),\
                    ('www.archlinux.org/','Archlinux','2021-10-10','03:59:01.30', 42)], 0)
    set()
    """
    most_visited_sites = set()
    if number == 0:
        return most_visited_sites
    dict_with_sites = {}
    # create dictionary where keys are urls and values are number of visits on it
    for cur_visit in visits:
        dict_with_sites[cur_visit[0]] = dict_with_sites.get(cur_visit[0], 0) + 1
    # if number of visited sites is not more than number return set of all urls
    if len(dict_with_sites) <= number:
        # return set with all urls (dictionary keys)
        return set(dict_with_sites)
    # find how many times user visited site that is № number in most frequently visited sites list
    min_number_of_visits = sorted(dict_with_sites.values(), reverse=True)[number - 1]
    last_most_visited_list = []
    # check in dict for keys(url) and value(number of visits)
    for cur_url, visit_number in dict_with_sites.items():
        if visit_number > min_number_of_visits:
            #  add ulr to set of most frequently visited sites
            most_visited_sites.add(cur_url)
        elif visit_number == min_number_of_visits:
            # add url to tuples with urls (which number of visits is equal to № number
            #  in list of top visited sites) that will supplement set
            last_most_visited_list.append(cur_url)
    # supplement set of most visited sites urls
    for i in range(number - len(most_visited_sites)):
        most_visited_sites.add(last_most_visited_list[i])
    return most_visited_sites


def get_url_info(visits: list, url: str):
    """
    Returns tuple with info about site, which title is passed
    Function should return:
    title - title of site with this url
    last_visit_date - date of the last visit of this site, in format "yyyy-mm-dd"
    last_visit_time - time of the last visit of this site, in format "hh:mm:ss.ms"
    num_of_visits - how much time was this site visited
    average_time - average time, spend on this site
    :param visits: all visits in browser history
    :param url: url of site to search
    :return: (title, last_visit_date, last_visit_time, num_of_visits, average_time)
    >>> get_url_info([('www.archlinux.org/','Archlinux','2021-10-10','03:30:01.301234', 42),\
                    ('www.cms.ucu.edu.ua/','CMS','2021-10-10','03:35:01.301234', 42),\
                    ('www.archlinux.org/','Archlinux','2021-10-10','03:59:01.301234', 42)],\
                                                                  'www.cms.ucu.edu.ua/')
    ('CMS', '2021-10-10', '03:35:01.301234', 1, 42.0)
    >>> get_url_info([('www.archlinux.org/','Archlinux','2021-10-10','03:30:01.301234', 42),\
                    ('www.cms.ucu.edu.ua/','CMS','2021-10-10','03:35:01.301234', 42),\
                    ('www.archlinux.org/','Archlinux','2021-10-10','03:59:01.301234', 42)],\
                                                                  'www.archlinux.org/')
    ('Archlinux', '2021-10-10', '03:59:01.301234', 2, 42.0)
    >>> get_url_info([('www.archlinux.org/','Archlinux','2021-10-10','03:30:01.301234', 42),\
                    ('www.cms.ucu.edu.ua/','CMS','2021-10-10','03:35:01.301234', 42),\
                    ('www.archlinux.org/','Archlinux','2021-10-10','03:59:01.301234', 42)],\
                                                                  'www.stackoverflow.com/')
    ('', '', '', 0, 0)
    >>> get_url_info([], 'www.archlinux.org/')
    ('', '', '', 0, 0)
    """
    # set starting url info parameters
    title = ''
    last_visit_date = 0
    last_visit_time = 0
    num_of_visits = 0
    total_time = 0
    # if list of visits is empty return starting valuel
    if len(visits) == 0:
        return '', '', '', 0, 0
    # check in cycle for each visit info in format of tuple(url, title, date, time, time on page)
    for current_visit_info in visits:
        # check if this visit info url is set url
        if current_visit_info[0] == url:
            if not title:
                # set title of site by its url
                title = current_visit_info[1]
            num_of_visits += 1
            total_time += current_visit_info[4]
            # introduce visit date value in format like yyyymmdd
            visit_date = int(current_visit_info[2].replace('-', ''))
            # introduce visit date value in format like hhmmssms
            visit_time = int(current_visit_info[3].replace(':', '').replace('.', ''))
            # check whether current visit was after previous last site visit
            if visit_date > last_visit_date or (visit_date == last_visit_date and
                                                visit_time > last_visit_time):
                # change last visits date and time to current visit values
                last_visit_time = visit_time
                last_visit_date = visit_date
    # if user did not visited site return None
    if num_of_visits == 0:
        return '', '', '', 0, 0
    # calculate average time on site
    average_time = total_time / num_of_visits
    # transform last visit date to stated format (yyyy-mm-dd)
    date = str(last_visit_date)
    last_visit_date = date[:4] + '-' + date[4:6] + '-' + date[-2:]
    # transform last visit time  to stated format (hh:mm:ss.ms)
    time = str(last_visit_time)
    time = '0' *(12-len(time)) + time
    last_visit_time = time[:2] + ':' + time[2:4] + ':' + time[4:6] + '.' + time[6:]

    return title, last_visit_date, last_visit_time, num_of_visits, average_time

# print(get_url_info([('www.archlinux.org/','Archlinux','2021-10-10','03:30:01.300000', 42),\
                    # ('www.cms.ucu.edu.ua/','CMS','2021-10-10','03:35:01.300000', 42),\
                    # ('www.archlinux.org/','Archlinux','2021-10-10','03:59:01.300000', 58)],\
                                                                # 'www.archlinux.org/'))

# if __name__ == '__main__':
#     import doctest
#     print(doctest.testmod())


# print(get_url_info([('www.archlinux.org/','Archlinux','2021-10-10','03:30:01.300000', 42),\
#                     ('www.cms.ucu.edu.ua/','CMS','2021-10-11','03:35:01.300000', 42),\
#                     ('www.archlinux.org/','Archlinux','2021-10-10','03:59:01.300000',42),\
#                         ('www.cms.ucu.edu.ua/','CMS','2021-10-11','03:35:01.300000', 42),\
#                             ('www.cms.ucu.edu.ua/','CMS','2021-10-11','03:35:01.300000', 42),('www.cms.ucu.edu.us/',\
# 'CMS','2021-10-11','03:35:01.30', 42)],'www.archlinux.org/'))


print(get_url_info([('https://www.grammarly.com/', 'Grammarly: Free Online Writing Assistant',\
     '2021-10-08', '22:53:30.072153', 543),
('https://www.grammarly.com/', 'Grammarly: Free Online Writing Assistant', '2021-10-08',\
     '22:53:33.911339', 2767046),
('https://app.grammarly.com/', 'Grammarly', '2021-10-08', '22:53:36.678385', 32348356),
('https://account.grammarly.com/', 'Account | Grammarly', '2021-10-08', '22:53:40.009853', 34),
('https://account.grammarly.com/customize', 'Account | Grammarly', '2021-10-08', '22:54:07.961370', 63),
('https://account.grammarly.com/subscription', 'Account | Grammarly', '2021-10-08', '22:54:09.026739', 345)],'https://account.grammarly.com/subscription'))