from bs4 import BeautifulSoup
import requests
import numpy as np

def gen_link():
    if(np.random.choice([True, False])):
        #amc
        np.random.seed()
        year=np.random.randint(2015,2023)
        AB=np.random.choice(['A', 'B'])
        #question
        mu,sigma=18, 5
        s=np.random.normal(mu,sigma,1000)
        s = np.round(s)
        s=s[s>=10]
        s=s[s<=25]
        q=int(np.random.choice(s))
        link='https://artofproblemsolving.com/wiki/index.php/{}_AMC_12{}_Problems/Problem_{}'.format(year, AB, q)
    else:
        #aime
        np.random.seed()
        year=np.random.randint(2005,2023)
        I=np.random.choice(['I', 'II'])
        mu,sigma=6, 4
        s=np.random.normal(mu,sigma,1000)
        s = np.round(s)
        s=s[s>=1]
        s=s[s<=15]
        q=int(np.random.choice(s))
        link='https://artofproblemsolving.com/wiki/index.php/{}_AIME_{}_Problems/Problem_{}'.format(year,I, q)
    return link

def convert_to_renderable_html(text):
    text = text.replace('//latex.artofproblemsolving.com', 'https://latex.artofproblemsolving.com')
    return text

def get_problem(url):
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    problem_headline = soup.find('span', {'class': 'mw-headline', 'id': 'Problem'})
    
    if problem_headline:
        problem_content = []
        for sibling in problem_headline.parent.find_next_siblings():
            # If the sibling is a headline ('h2'), break the loop, as we've reached the next section
            if sibling.name == 'h2':
                break
            # If the sibling is a paragraph ('p'), add it to the problem content
            elif sibling.name == 'p':
                problem_content.append(convert_to_renderable_html(str(sibling)))

        # Join all paragraphs into a single string (HTML)
        problem_html = " ".join(problem_content)
        return problem_html
    else:
        print("No problem found")

def gen_html(num):
    all_q=str()
    num_tried=0
    num_succ=0
    while(True):
        try:
            link=gen_link()
            print(link)
            hype = '<a href="{}" target="_blank">to link</a>'.format(link)
            qhtml=get_problem(link)
            all_q+=(hype+qhtml)
            num_succ+=1
        except:
            pass
        num_tried+=1
        if num_succ>=num or num_tried>20:
            break

    all_q=f'''
    <html>
    <head>
    </head>
    <body>
    {all_q}
    </body>
    </html>
    '''
    
    return all_q
