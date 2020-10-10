#!/usr/bin/env python3

import random
import rospy
from std_msgs.msg import String

websites = [
    "youtube.com",
    "en.wikipedia.org",
    "twitter.com",
    "facebook.com",
    "amazon.com",
    "yelp.com",
    "reddit.com",
    "imdb.com",
    "fandom.com",
    "pintrest.com",
    "tripadvisor.com",
    "instagram.com",
    "walmart.com",
    "craigslist.org",
    "ebay.com",
    "linkedin.com",
    "play.google.com",
    "healthline.com",
    "etsy.com",
    "indeed.com",
    "apple.com",
    "espn.com",
    "webmd.com",
    "fb.com",
    "nytimes.com",
    "google.com",
    "cnn.com",
    "merriam-webster.com",
    "gamepedia.com",
    "microsoft.com",
    "target.com",
    "homedepot.com",
    "quora.com",
    "nih.gov",
    "rottentomatoes.com",
    "netflix.com",
    "quizlet.com",
    "weather.com",
    "mapquest.com",
    "britannica.com",
    "businessinsider.com",
    "dictionary.com",
    "zillow.com",
    "mayoclinic.org",
    "bestbuy.com",
    "theguardian.com",
    "yahoo.com",
    "msn.com",
    "usatoday.com",
    "medicalnewstoday.com",
    "urbandictionary.com",
    "usnews.com",
    "foxnews.com",
    "genius.com",
    "allrecipes.com",
    "spotify.com",
    "glassdoor.com",
    "forbes.com",
    "cnet.com",
    "finance.yahoo.com",
    "irs.gov",
    "lowes.com",
    "mail.yahoo.com",
    "aol.com",
    "steampowered.com",
    "washintonpost.com",
    "usps.com",
    "office.com",
    "retailmenot.com",
    "wiktionary.org",
    "paypal.org",
    "foodnetwork.com",
    "hulu.com",
    "live.com",
    "cbssports.com",
    "wayfair.com",
    "ca.gov",
    "bleacherreport.com",
    "macys.com",
    "accuweather.com",
    "xfinity.com",
    "go.com",
    "techradar.com",
    "groupon.com",
    "investopedia.com",
    "yellowpages.com",
    "steamcommunity.com",
    "chase.com",
    "wellsfargo.com",
    "npr.org",
    "apartments.com",
    "roblox.com",
    "huffpost.com",
    "books.google.com",
    "bankofamerica.com",
    "bbb.org",
    "expedia.com",
    "wikihow.com",
    "ign.com",
    "wowhead.com",
]


def gen_url():
    pub = rospy.Publisher("url1", String, queue_size=10)
    rospy.init_node("scanner", anonymous=True)
    rate = rospy.Rate(0.5)
    print("Publishing random URLs to /url...")
    while not rospy.is_shutdown():
        url = random.choice(websites)
        print("Current URL: " + url + ' ' * (20 - len(url)), end='\r', flush=True)
        pub.publish(url)
        rate.sleep()

if __name__ == '__main__':
    try:
        gen_url()
    except rospy.ROSInterruptException:
        pass