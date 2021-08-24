import json
import requests
from bs4 import BeautifulSoup


class Config:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.url = None
        self.log = None
        self.div_class = None
        self.num_span_class = None
        self.text_span_class = None
        self.__readFile()

    def __readFile(self):
        with open(self.config_file, 'r') as config_file:
            conf = json.load(config_file)
            self.url = conf.get('url')
            self.log = conf.get('log')
            self.div_class = conf.get('class').get('div_class')
            self.num_span_class = conf.get('class').get('num_span_class')
            self.text_span_class = conf.get('class').get('text_span_class')


class Parser:
    def __init__(self, config):
        self.config = config
        self.html = None
        self.div = None

        self.giveTitle = lambda x: x.find('h3').text
        self.giveNum = lambda i: i.find('span', class_=self.config.num_span_class).text
        self.giveText = lambda i: i.find('span', class_=self.config.text_span_class).text

        self.__initialize()

    def __initialize(self):
        self.configureHtml()
        self.configureDiv()

    def configureHtml(self):
        """
        Accesses the HTML and assigns it to the variable.
        :return: html
        """
        r = requests.get(self.config.url)
        self.html = BeautifulSoup(r.content, 'html.parser')
        return self.html

    def configureDiv(self):
        """
        Extracts the div from the html.
        :return: div
        """
        self.div = self.html.findAll('div', class_=self.config.div_class)
        return self.div

    def givePrintList(self, div_element):
        """
        Returns parsed data for printing.
        [[Number., String], ..]
        :param div_element: Div element
        :return: List of div element
        """
        return [[self.giveNum(li) + '.', self.giveText(li)] for li in div_element.findAll('li')]
    
    def log(self):
        """
        Prints all parsed data to the screen.
        """
        if not self.config.log: return None
        data = dict()
        for column in self.div:
            title_name = self.giveTitle(column)
            printList = self.givePrintList(column)
            data[title_name] = printList
        self.consoleLog(**data)
    
    def giveList(self, div_element):
        """
        Returns parsed data for the entered div element.
        [[Group, Number, String], ..]
        :param div_element: Div element
        :return: List of div element
        """
        title_name = self.giveTitle(div_element)
        return [[title_name, self.giveNum(li), self.giveText(li)] for li in div_element.findAll('li')]

    def giveDict(self):
        """
        Returns all parsed data as a dictionary.
        :return: Dictionary
        """
        data = dict()
        data['clues'] = []
        for column in self.div:
            for row in self.giveList(column):
                title, num, text = row
                data['clues'].append(
                    {
                        'Group': title,
                        'Number': num,
                        'String': text
                    })
        return data

    def saveJSON(self, filepath='./bot-crosswordsParser-clues.json', message=True):
        """
        Saves clues as a JSON file.
        :param filepath: 'clues.json' path.
        :param message: Print successfully message.
        """
        with open(filepath, 'w') as file:
            json.dump(self.giveDict(), file)
        if message: print('JSON file saved successfully.')

    @staticmethod
    def consoleLog(**kwargs):
        """
        Prints dictionary to the console.
        Values must be nested.
        :param kwargs: Dictionary
        """
        print(kwargs)
        for key, values in kwargs.items():
            print(f"=== {key} ===")
            for value in values:
                print(*value)

    def __getitem__(self, item):
        return self.div[item]

    def __len__(self):
        return len(self.div)


if __name__ == '__main__':
    config = Config()
    parser = Parser(config=config)

    parser.log()
    parser.saveJSON()
