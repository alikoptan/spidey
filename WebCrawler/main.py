import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

print('ENTER YOUR WEBSITE NAME')
PROJECT_NAME = input()
print('ENTER YOUR HOMEPAGE URL')
HOMEPAGE = input()
print('ENTER NUMBER OF THREADS TO BE USED')
NUMBER_OF_THREADS = int(input())

DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
queue = Queue()

print('CRAWLING: ' + PROJECT_NAME + ' - DOMAIN: ' + DOMAIN_NAME + ' - HOMEPAGE: ' + HOMEPAGE)
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)

# Create worker threads (will die when main exists)
def create_spiders():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

# Do the next job in queue
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()

# Each queued link is a new job (thread)
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()

# Check if there are links in queue.txt, if so then crawl them
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' LINKS LEFT IN QUEUE')
        create_jobs()

create_spiders()
crawl()