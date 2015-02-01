__author__ = 'Huayong'
import urllib.request as request
import re
import os
import urllib.error as error

def download_png(url, dir_path, image_type):

    html_path = dir_path + '1.html'
    print('正在下载页面, 并保存为' + html_path)
    html = request.urlopen(url).read()

    #创建目录保存每个网页上的图片
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)

    page_data = html.decode('utf-8')
    page_image = re.compile('<img src=\"(.+?)\"')

    match_result = page_image.match(page_data)
    #print(match_result)
    search_result = page_image.search(page_data)
    #print(search_result)

    count = 1

    for image in page_image.findall(page_data):
        # print(image)
        pattern = re.compile(r'^http://.*.' + image_type + '$')
        if pattern.match(image):
            print(image)
            try:
                image_data = request.urlopen(image).read()
                image_path = dir_path + '/' + str(count) + '.' + image_type

                with open(image_path, 'wb') as image_file:
                    image_file.write(image_data)
                    count += 1
                image_file.close()
            except error.URLError as e:
                print('Download failed')
        with open(html_path, 'wb') as html_file:
            html_file.write(html)
        html_file.close()

def download_txt(url, dir_path):
    html = request.urlopen(url).read()
    page_data = html.decode('gbk')
    #print(page_data)

    all_txt = '\n\t\t'
    txt_path = dir_path + '1.txt'

    page_title = re.compile('正文 (.+?)</H1>')
    for title in page_title.findall(page_data):
        #print(title)
        all_txt += title + '\n\n\t'

    page_txt = re.compile('(?:&nbsp;)+(.+?)<br />')
    for txt in page_txt.findall(page_data):
        #print(txt)
        all_txt += txt + '\n\n\t'
    #print(all_txt)

    with open(txt_path, 'at', encoding='utf8') as txt_file:
        txt_file.write(all_txt)
    txt_file.close()

def find_url(url, dir_path):
    html = request.urlopen(url).read()
    page_data = html.decode('gbk')
    #print(page_data)

    page_url = re.compile('<li><a href=\"(.+?html)\">')
    for temp_url in page_url.findall(page_data):
        print(url + temp_url)
        download_txt(url + temp_url, dir_path)

if __name__ == "__main__":
    # url = "http://tieba.baidu.com/p/2400071099"
    # dir_path = 'G:/test/'
    # image_type = 'png'
    # download_png(url, dir_path, image_type)

    url = 'http://www.ppxsw.co/files/article/html/0/78/312207.html'
    dir_path = 'G:/test/'
    download_txt(url, dir_path)

    #http://www.ppxsw.co/files/article/html/0/78/315811.html