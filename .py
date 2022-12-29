import datetime

class SocialMediaScheduler:
    def __init__(self):
        self.scheduled_posts = []
    
    def schedule_post(self, platform, message, time):
        # Convert the provided time to a datetime object
        time = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
        
        # Create a dictionary representing the scheduled post
        post = {
            'platform': platform,
            'message': message,
            'time': time
        }
        
        # Append the post to the list of scheduled posts
        self.scheduled_posts.append(post)
        
    def get_scheduled_posts(self):
        return self.scheduled_posts
    
    def get_scheduled_posts_for_platform(self, platform):
        # Filter the list of posts to only include posts for the specified platform
        return [post for post in self.scheduled_posts if post['platform'] == platform]
    
    def get_next_post(self):
        # Sort the list of scheduled posts by time
        self.scheduled_posts.sort(key=lambda post: post['time'])
        
        # Return the first post in the sorted list (which will be the next post to be published)
        return self.scheduled_posts[0]
    
    def publish_next_post(self):
        # Get the next post to be published
        next_post = self.get_next_post()
        
        # Publish the post (in this example, we will just print it to the console)
        print(f'Publishing "{next_post["message"]}" to {next_post["platform"]} at {next_post["time"]}')
        
        # Remove the post from the list of scheduled posts
        self.scheduled_posts.remove(next_post)
