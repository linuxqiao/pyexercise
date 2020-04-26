#!/usr/bin/python3

#encoding:utf-8
import requests
import json
import time
import re
import datetime
import pandas as pd

def get_data(url):

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
    r = requests.get(url, headers=headers)
    html = r.text
    return html
    
print("=============start=============")

question_id = "65551651"

url = "https://www.zhihu.com/api/v4/questions/"+ question_id +"/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%2Cpaid_info_content%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics&limit=5&offset=0&platform=desktop&sort_by=default"

html = get_data(url)
totals = json.loads(html)['paging']['totals']
print("totals page:" + str(totals))

page = 0

while(page < totals):
    url = "https://www.zhihu.com/api/v4/questions/"+ question_id +"/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%2Cpaid_info_content%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics&limit=5&offset="+ str(page) +"&platform=desktop&sort_by=default"
    html = get_data(url)
    json_data = json.loads(html)['data']
    comments = []
    
    print("============= page:" + str(page) + "=============")
    print("name, gender, voteup_count, comment_count, content")
    for item in json_data:
        comment = []
        comment.append(item['author']['name'])
        comment.append(item['author']['gender'])
        comment.append(item['voteup_count'])
        comment.append(item['comment_count'])
        comment.append(item['content'])
        print(comment)
        comments.append(comment)
    
    filename="./comments.csv"
    df = pd.DataFrame(comments)
    df.to_csv(filename, mode='a', index=False, sep=',', header=False)
    page += 5

print("===============end===============")
