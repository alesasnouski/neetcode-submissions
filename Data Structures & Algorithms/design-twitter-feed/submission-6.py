class Twitter:

    def __init__(self):
        from collections import defaultdict
        self.roster = defaultdict(list)
        self.feed = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.feed.append((tweetId, userId))

    def getNewsFeed(self, userId: int) -> List[int]:
        from collections import deque
        q = deque(maxlen=10)
        friends = self.roster[userId]
        for (tw_id, u_id) in self.feed:
            if u_id in friends or u_id == userId:
                q.append(tw_id)
        result = []
        while len(q) > 0:
            result.append(q.pop())
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.roster[followerId]:
            self.roster[followerId].append(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.roster[followerId]:
            self.roster[followerId].remove(followeeId)
        
