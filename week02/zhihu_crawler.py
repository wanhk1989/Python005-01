import requests
from lxml import etree

'''
抓取知乎任意一個话题下排名前15的答案；并将内容保存到本地的一个文件
'''

ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'

header = {'user-agent':ua}

url = 'https://www.zhihu.com/question/433528314'


response = requests.get(url, headers=header)

selector = etree.HTML(response.text)

topic = selector.xpath('//h1[@class="QuestionHeader-title"]/text()')

# <meta itemprop="answerCount" content="153">
answer_count = selector.xpath('//meta[@itemprop="answerCount"]')[0].attrib.get("content")
print(answer_count)

# for i in range(15):
#     xpath_sel = f'//div[@class="ContentItem AnswerItem" and @data-za-index="{i}"]/meta[@itemprop="url"]'
#     answer_url = selector.xpath(xpath_sel)[0].attrib.get("content")
#     print(answer_url)


def handle_answer(answer):
    contents = []
    for element in answer:
        if element.tag == "p":
            print(type(element.text))
            contents.append(element.text)
    print(contents)
    return contents
            
        # if element.tag == "figure":
        #     for child in element:
        #         if child.tag == "img":
        #             print(child.attrib.get("src"))




with open("answers.txt", "a") as f:
    for i in range(15):
        xpath_sel = f'//div[@class="ContentItem AnswerItem" and @data-za-index="{i}"]//div[@class="RichContent-inner"]/span/*'
        print(xpath_sel)
        answer = selector.xpath(xpath_sel)
        contents = handle_answer(answer)
        for content in contents:
            if content:
                print(content)
                f.write(content)