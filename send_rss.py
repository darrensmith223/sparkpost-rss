"""
Script to pull RSS data and pass into SparkPost as substitution data
"""
import os
import feedparser
import ssl
from sparkpost import SparkPost


def send_rss(rss_url, api_key, **kwargs):
    ssl._create_default_https_context = ssl._create_unverified_context
    feed = feedparser.parse(rss_url)
    items = feed.entries

    # Pack RSS data as substitution_data
    substitution_data = {
        "items": items
    }

    # Prepare Email
    recipients = kwargs.get("recipients")
    template_id = kwargs.get("template_id")
    campaign_id = kwargs.get("campaign_id")

    # Send Email
    sp = SparkPost(api_key)
    sp.transmissions.send(
        campaign=campaign_id,
        recipients=recipients,
        template=template_id,
        substitution_data=substitution_data
    )
