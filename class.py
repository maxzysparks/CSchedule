scheduler = SocialMediaScheduler()

# Schedule some posts
scheduler.schedule_post('Twitter', 'Hello, world!', '2022-01-01 12:00:00')
scheduler.schedule_post('Facebook', 'Hello, world!', '2022-01-01 12:00:01')
scheduler.schedule_post('Instagram', 'Hello, world!', '2022-01-01 12:00:02')

# Print the scheduled posts
print(scheduler.get_scheduled_posts())

# Print the scheduled posts for a specific platform
print(scheduler.get_scheduled_posts_for_platform('Twitter'))

# Print the next post to be published
print(scheduler.get_next_post())

# Publish the next post
scheduler.publish_next_post()

# Print the scheduled posts again
print(scheduler.get_scheduled_posts())
