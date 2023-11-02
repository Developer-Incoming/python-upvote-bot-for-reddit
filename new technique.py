import requests
requests.utils.default_user_agent = lambda: "some user agent, idk leave it like this. default one doesn't work"

def votePost(auth, postId, upvote):
    headers = {
        **requests.utils.default_headers(),
        **{
            "authorization": auth
        }
    }
    params = {
        "redditWebClient": "desktop2x",
        "app": "desktop2x-client-production",
        "raw_json": "1",
        "gilding_detail": "1",
    }
    data = {
        "id": postId,
        "dir": "1" if upvote else "0",
        "api_type": "json",
    }

    requests.post("https://oauth.reddit.com/api/vote", params=params, headers=headers, data=data)


votePost(
    auth="IMPORTANT, PUT YOUR AUTHENTICATION HERE, AKA TOKEN HERE!",
    postId="t3_17lsrb0",
    upvote=False
)