class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)
        self.ts = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.ts,tweetId))
        self.ts+=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []

        all_follows = list(self.follows[userId])
        if userId not in all_follows:
            all_follows.append(userId) 
        # 12345 23456 34567 45678

        curr_idxs = [len(self.tweets[fl])-1 for fl in all_follows]
        # print(curr_idxs)
        # 2 1 1 0

        for _ in range(10):
            max_ts = -1
            latest_tweet = None
            idx_to_change = None

            for idx, idx_of_followee in enumerate(all_follows):
                idx_of_followee_tweet = curr_idxs[idx]

                if idx_of_followee_tweet < 0:
                    continue

                ts, tw_id = self.tweets[idx_of_followee][idx_of_followee_tweet]
                if ts > max_ts:
                    max_ts = ts
                    latest_tweet = tw_id
                    idx_to_change = idx

            if latest_tweet:
                tweets.append(latest_tweet)
                curr_idxs[idx_to_change]-=1

        return tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        print(self.follows[followerId])
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        # print(self.follows[followerId])
