class Twitter:

    def __init__(self):
        self.followers = defaultdict(set)
        self.tweets = defaultdict(list)
        self.ts = 0

    def _inc(self):
        self.ts+=1
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.ts, tweetId))
        self._inc()
        
    def getNewsFeed(self, userId: int) -> List[int]:
        all_followers = list(self.followers[userId]) + [userId]

        latest_tweets = []
        cur_uid_idx = defaultdict(lambda:-2)

        for _ in range(10):
            curr_max = -1
            cur_tweet = None
            curr_uid = -1

            for uid in all_followers:
                curr_idx = cur_uid_idx[uid]
                
                if curr_idx==-2:
                    cur_uid_idx[uid] = len(self.tweets[uid])-1
                
                curr_idx = cur_uid_idx[uid]
                # print(uid, curr_idx, 'idx')
                # print(self.tweets[uid][curr_idx], 'tweets')

                if curr_idx >= 0:
                    ts, tw = self.tweets[uid][curr_idx]
                    # print(ts,tw)

                    if ts > curr_max:
                        curr_max = ts
                        cur_tweet = tw
                        curr_uid = uid
            
            # print(curr_max)
            if curr_max != -1:
                latest_tweets.append(cur_tweet)
                cur_uid_idx[curr_uid]-=1

        return latest_tweets
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        
