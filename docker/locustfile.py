import os
import random
from locust import HttpLocust, TaskSet, task
from pyquery import PyQuery

class UserBehavior(TaskSet):
    def on_start(self):
        # assume all users arrive at the index page
        if os.getenv( "INSECURE_SSL" ).lower() == "true":
            self.client.verify = False
        self.index_page()
        self.urls_on_current_page = self.toc_urls

    @task(10)
    def index_page(self):
        r = self.client.get("/")
        pq = PyQuery(r.content)
        link_elements = pq(".nav-item a")
        self.toc_urls = [
            l.attrib["href"] for l in link_elements
        ]

    @task(50)
    def load_page(self, url=None):
        url = random.choice(self.toc_urls)
        r = self.client.get(url)
        pq = PyQuery(r.content)
        link_elements = pq("a")
        self.urls_on_current_page = [
            l.attrib["href"] for l in link_elements if "href" in l.attrib and l.attrib["href"].startswith(os.getenv("TARGET_URL"))
        ]

    @task(30)
    def load_sub_page(self):
        url = random.choice(self.urls_on_current_page)
        r = self.client.get(url)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 2000
    max_wait = 9000
