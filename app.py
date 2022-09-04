import grequests

urls = ['https://www.python.org/', 'https://www.python.org/about/help/',
        'https://www.python.org/community/logos/']

heads = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.167 YaBrowser/22.7.4.957 Yowser/2.5 Safari/537.36'
}

req = (grequests.get(url, headers=heads) for url in urls)
responses_list = grequests.map(req)

for i in range(len(responses_list)):
    with open('index'+str([i])+'.html', 'w', encoding="utf-8") as file:
        file.write(responses_list[i].text)
        with open('index'+str([i])+'.html', 'r', encoding="utf-8") as file:
            print(file.read().count('Python'))
