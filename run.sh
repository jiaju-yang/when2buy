#!/usr/bin/env bash

cd /home/psyche/projects/when2buy/crawler
source /home/psyche/projects/when2buy/env/bin/activate

scrapy crawl ctrip -L INFO --logfile ../log/`date +%Y-%m-%d`.log