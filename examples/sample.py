from RSS_to_substitution import send_rss

# ----------------------
# Sample script
# ----------------------

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
