from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.created_at = 0
        self.user_tweets_map = defaultdict(list)
        self.follower_followees_map = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets_map[userId].append([self.created_at, tweetId])
        self.created_at -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        min_heap = []

        self.follower_followees_map[userId].add(userId)

        for followee_id in self.follower_followees_map[userId]:
            if followee_id in self.user_tweets_map:
                tweets_by_followee = self.user_tweets_map[followee_id]
                latest_tweet_index = len(tweets_by_followee) - 1
                created_at, tweet_id = self.user_tweets_map[followee_id][latest_tweet_index]

                min_heap.append([created_at, tweet_id, followee_id, latest_tweet_index - 1])
        
        heapq.heapify(min_heap)

        while min_heap and len(result) < 10:
            created_at, tweet_id, followee_id, latest_tweet_index = heapq.heappop(min_heap)
            result.append(tweet_id)

            if latest_tweet_index >= 0:
                created_at, tweet_id = self.user_tweets_map[followee_id][latest_tweet_index]
                heapq.heappush(min_heap, [created_at, tweet_id, followee_id, latest_tweet_index - 1])

        return result
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower_followees_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follower_followees_map[followerId]:
            self.follower_followees_map[followerId].remove(followeeId)
        
