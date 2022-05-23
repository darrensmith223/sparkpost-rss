# sparkpost-rss
Project demonstrating how to pull RSS Data as Substitution Data within SparkPost

# How to Use

Clone this repo.

Import `send_rss()` from `RSS_to_substitution.py`

```python
from RSS_to_substitution import send_rss
```

Define the URL where the RSS data can be found.

```python
# Initialize
rss_url = "https://www.nasa.gov/rss/dyn/lg_image_of_the_day.rss"
api_key = os.getenv("API_KEY")
recipients = ['example@example.com']
template_id = "template-id"
campaign_id = "test_rss"

send_rss(
    rss_url=rss_url,
    api_key=api_key,
    recipients=recipients,
    template_id=template_id,
    campaign_id=campaign_id
)
```

The script passes the RSS data to SparkPost as substitution data under the array `items`.   Use the SparkPost Template Language to refer to the RSS fields.  For instance, the field "title" can be referenced with `{{ var_loop.title }}`

A sample SparkPost template can be found in `rss_template.html`.
