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
        self.toc_urls = []
        r = self.client.get("/")
        pq = PyQuery(r.content)
        link_elements = pq("a")
        for l in link_elements:
            if "href" not in l.attrib:
                continue
            href=l.attrib["href"]
            if os.getenv("TARGET_URL") in href:
                if os.getenv("CACHE_BUSTER").lower() == "true":
                    href += "?test"
                self.toc_urls.append(href)

    @task(50)
    def load_page(self, url=None):
        self.urls_on_current_page=[]
        url = random.choice(self.toc_urls)
        r = self.client.get(url)
        pq = PyQuery(r.content)
        link_elements = pq("a")
        for l in link_elements:
            if "href" not in l.attrib:
                continue
            href=l.attrib["href"]
            if os.getenv("TARGET_URL") in href:
                if os.getenv("CACHE_BUSTER").lower() == "true":
                    href += "?test"
                self.urls_on_current_page.append(href)

    @task(30)
    def load_sub_page(self):
        url = random.choice(self.urls_on_current_page)
        r = self.client.get(url)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 2000
    max_wait = 9000
