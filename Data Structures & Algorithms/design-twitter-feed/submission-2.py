class Twitter:

    def __init__(self):
        self.followees = {}
        self.tweets = []
        self.latest = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.tweets, (-self.latest, -tweetId, userId))
        self.latest += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        temp = []
        #print("Start")
        if userId not in self.followees:
            self.followees[userId] = {}
        for _ in range(10):
            if not self.tweets:
                break
            if self.tweets:
                l, tweet, uid = heapq.heappop(self.tweets)
                tweet = -tweet
                #print(tweet, uid)
                temp.append((l, tweet, uid))
           
            while self.tweets and uid not in self.followees[userId] and uid != userId:
               # print(userId)
                l, tweet, uid = heapq.heappop(self.tweets)
                tweet = -tweet
                temp.append((l, tweet, uid))
            #print(uid, tweet, userId)
            if uid in self.followees[userId] or uid == userId:
                feed.append(tweet)

        for l, t, u in temp:
            heapq.heappush(self.tweets, (l, -t, u))
        #print("end")
        return feed



    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followees:
            self.followees[followerId] = {}
        self.followees[followerId][followeeId] = 1
       

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followees[followerId]:
            del self.followees[followerId][followeeId]
        
