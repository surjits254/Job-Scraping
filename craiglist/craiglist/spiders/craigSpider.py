#!/usr/bin/python
from scrapy import Spider
from scrapy.http import Request
import configparser
from time import sleep
import boto3

class CraigspiderSpider(Spider):
    name = 'craigSpider'
    allowed_domains = ['craigslist.org']
    start_urls = ['http://craigslist.org/']
    
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('conf.ini')
        self.states = config['common']['states'].split(",")
        self.sleep_time = int(config['common']['sleep_time'])
        self.urlString = config['common']['url']
        self.bucket_name = config['common']['bucket_name']
        self.output_file = config['common']['output_file']

    def parse(self, response):
        
        for state in self.states:
            stateRep = state.replace(" ","")
            url = self.urlString.format(stateRep)
            print("**********"+url)
            yield Request(url,meta={'location':state}, callback=self.parse_links)
            sleep(self.sleep_time)
            
    def parse_links(self, response):
        location = response.meta['location'].title()
        total_lnks = int(response.xpath("//*[@class='button pagenum']")[-1].xpath("//*[@class='totalcount']/text()")[0].extract()) - 1
        lnks = response.xpath("//*[@class='result-info']/a/@href").extract() 
        lnks = lnks[:total_lnks]
        
        for lnk in lnks:
            yield Request(lnk,meta={'location':location}, callback=self.parse_final)
            sleep(self.sleep_time)
            
    def parse_final(self,response):
        location = response.meta['location'].title()
        url = response.request.url
        job_title = response.xpath("//*[@id='titletextonly']/text()").extract_first()
        etypes = response.xpath("//*[@class='attrgroup']/span/b/text()")
        if(len(etypes)>1):
            etype = etypes[1].extract()
        else:
            etype = ""
         
         
        yield {
            "type":etype,
            "job_title":job_title,
            "location":location,
            "url":url
            }

    def close(self, reason):
        s3 = boto3.resource('s3')
        s3.Object(self.bucket_name,self.output_file).upload_file(Filename=self.output_file)

